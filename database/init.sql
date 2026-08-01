CREATE TABLE users (
    user_id INTEGER PRIMARY KEY autoincrement,
    username VARCHAR(32) UNIQUE NOT NULL,
    password VARCHAR(64) NOT NULL,
    color VARCHAR (32),
    is_admin BOOLEAN default false
);

CREATE TABLE forum (
    entry_id INTEGER PRIMARY KEY autoincrement,
    entry_username VARCHAR(32) NOT NULL,
    entry_contents VARCHAR(250) NOT NULL
);
