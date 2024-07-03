CREATE TABLE places (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    address VARCHAR(255) NOT NULL,
    city_id VARCHAR(60) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    host_id VARCHAR(60) NOT NULL,
    number_of_rooms INTEGER NOT NULL,
    number_of_bathrooms INTEGER NOT NULL,
    price_per_night FLOAT NOT NULL,
    max_guests INTEGER NOT NULL,
    amenity_ids VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(id)
);