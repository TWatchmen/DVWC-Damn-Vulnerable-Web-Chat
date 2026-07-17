CREATE TABLE users (
    user_id INTEGER PRIMARY KEY autoincrement,
    username VARCHAR(32) NOT NULL,
    password VARCHAR(64) NOT NULL,
    is_admin BOOLEAN default false
);
