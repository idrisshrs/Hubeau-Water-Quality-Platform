"""PostgreSQL connection helper for the academic Hub'Eau project.

Connection settings are read from environment variables so that credentials and
local network addresses are not committed to the public repository.
"""

import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    required = {
        "DB_NAME": os.getenv("DB_NAME"),
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD"),
        "DB_HOST": os.getenv("DB_HOST"),
        "DB_PORT": os.getenv("DB_PORT", "5432"),
    }
    missing = [key for key, value in required.items() if not value]
    if missing:
        raise RuntimeError(
            "Missing database configuration: " + ", ".join(missing) +
            ". Copy .env.example to .env and provide local values."
        )

    return psycopg2.connect(
        database=required["DB_NAME"],
        user=required["DB_USER"],
        password=required["DB_PASSWORD"],
        host=required["DB_HOST"],
        port=required["DB_PORT"],
    )


if __name__ == "__main__":
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM commune;")
            print("Data from database:", cursor.fetchall())
    finally:
        connection.close()
