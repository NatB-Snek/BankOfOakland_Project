CREATE DATABASE boo_db;
USE boo_db;

-- Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    birthday DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cards table
CREATE TABLE cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    card_number VARCHAR(16) UNIQUE NOT NULL,
    cvv VARCHAR(4) NOT NULL,
    expiry_date DATE NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Transactions table
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_id INT NOT NULL,
    transaction_type ENUM('deposit', 'withdrawal', 'purchase', 'transfer') NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (card_id) REFERENCES cards(id) ON DELETE CASCADE
);

--Data for testing
INSERT INTO users (username, password_hash, email, phone, address, birthday) 
VALUES ('user1', '123', 'user@oakland.edu', '1234567890', '123 Test St', '2003-04-25');

INSERT INTO cards (user_id, card_number, cvv, expiry_date, balance) 
VALUES (1, '1234567812345678', '123', '2026-12-31', 1000.00);

INSERT INTO transactions (card_id, transaction_type, amount, description) 
VALUES (1, 'deposit', 500.00, 'Initial deposit');
