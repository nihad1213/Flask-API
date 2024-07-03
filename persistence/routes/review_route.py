from flask import Blueprint, jsonify, request
from models.ReviewModel import Review
from models.PlaceModel import Place
from models.UserModel import User
from sqlalchemy.orm.exc import NoResultFound
from db import db

reviewRoutes = Blueprint('review_routes', __name__)

# Utility function to convert Review object to dictionary
def review_to_dict(review):
    return {
        'id': review.id,
        'user_id': review.user_id,
        'place_id': review.place_id,
        'rating': review.rating,
        'comment': review.comment,
        'created_at': review.created_at,
        'updated_at': review.updated_at
    }

# Create a new review for a specific place
@reviewRoutes.route('/places/<string:place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.json
    user_id = data.get('user_id')
    rating = data.get('rating')
    comment = data.get('comment')

    # Validation
    if not all([user_id, rating, comment]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if not (1 <= int(rating) <= 5):
        return jsonify({'error': 'Invalid rating. Rating must be between 1 and 5'}), 400

    try:
        place = Place.query.filter_by(id=place_id).one()
    except NoResultFound:
        return jsonify({'error': 'Place not found'}), 404
    
    new_review = Review(
        user_id=user_id,
        place_id=place_id,
        rating=rating,
        comment=comment
    )

    db.session.add(new_review)
    db.session.commit()

    return jsonify(review_to_dict(new_review)), 201

# Retrieve all reviews written by a specific user
@reviewRoutes.route('/users/<string:user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    reviews = Review.query.filter_by(user_id=user_id).all()
    return jsonify([review_to_dict(review) for review in reviews]), 200

# Retrieve all reviews for a specific place
@reviewRoutes.route('/places/<string:place_id>/reviews', methods=['GET'])
def get_place_reviews(place_id):
    reviews = Review.query.filter_by(place_id=place_id).all()
    return jsonify([review_to_dict(review) for review in reviews]), 200

# Retrieve a specific review by ID
@reviewRoutes.route('/reviews/<string:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review_to_dict(review)), 200

# Update an existing review
@reviewRoutes.route('/reviews/<string:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json

    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    review.rating = data.get('rating', review.rating)
    review.comment = data.get('comment', review.comment)

    if 'rating' in data:
        if not (1 <= int(data['rating']) <= 5):
            return jsonify({'error': 'Invalid rating. Rating must be between 1 and 5'}), 400

    db.session.commit()
    return jsonify(review_to_dict(review)), 200

# Delete a specific review
@reviewRoutes.route('/reviews/<string:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    db.session.delete(review)
    db.session.commit()
    return '', 204
