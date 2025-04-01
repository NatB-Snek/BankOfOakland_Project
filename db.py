import os
import sqlite3

# Get the absolute path to the same folder this script lives in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "bank.db")

def initializeDB():
    if not os.path.exists("bank.db"):
        print("🛠️ Creating new database...")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            address TEXT,
            birthday TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Create cards table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            card_number TEXT UNIQUE NOT NULL,
            cvv TEXT NOT NULL,
            expiry_date TEXT NOT NULL,
            balance REAL DEFAULT 0.00,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        """)

        # Create transactions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_id INTEGER NOT NULL,
            transaction_type TEXT NOT NULL,
            amount REAL NOT NULL,
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (card_id) REFERENCES cards(id) ON DELETE CASCADE
        )
        """)

        conn.commit()
        conn.close()
        print("✅ All tables created in bank.db!")
    else:
        print("db already exists!")

if __name__ == "__main__":
    initializeDB()