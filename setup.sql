CREATE TABLE user (
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
); VALUES (
    "Jane",
    "Doe",
    "Skiing"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
); VALUES (
    "John",
    "Doe",
    "Surfing"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
); VALUES (
    "Jane",
    "Roe",
    "Skating"
);