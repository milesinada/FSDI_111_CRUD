CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE vehicle_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(64)
);

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(45) NOT NULL,
    license_plate VARCHAR(45) NOT NULL,
    v_type INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (v_type) REFERENCES vehicle_types(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);


INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jane",
    "Doe",
    "Skiing"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "John",
    "Doe",
    "Surfing"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jane",
    "Roe",
    "Skating"
);

INSERT INTO vehicle_type (description) VALUES ("motorcycle");
INSERT INTO vehicle_type (description) VALUES ("car");
INSERT INTO vehicle_type (description) VALUES ("truck");
INSERT INTO vehicle_type (description) VALUES ("SUV");


INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id
) VALUES (
    "red",
    "HELL01",
    2,
    1
);
INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id
) VALUES (
    "white",
    "HELL02",
    3,
    1
);
INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id
) VALUES (
    "blue",
    "KHJGBG",
    4,
    2
);

SELECT user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.license_plate,
        vehicle.color,
        vehicle.v_type as vehicle_type
FROM user INNER JOIN vehicle 
ON user.id = vehicle.user_id;


--Join three tables: user, vehicle and vehicle type:
SELECT user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.license_plate,
        vehicle.color,
        vehicle_type.description 
FROM user 
INNER JOIN vehicle ON user.id = vehicle.user_id
INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id;
