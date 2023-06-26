import psycopg2
import json
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


def get_db_connection():
    # Establish a connection to the database.
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn


def execute_query(query, params=None):
    # Execute a single query against the database.
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()


def create_table():
    # Create a new table in the database, if it does not already exist.
    query = """
        CREATE TABLE IF NOT EXISTS interfaces(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description VARCHAR(255),
            max_frame_size INTEGER,
            config JSON,
            port_channel_id INTEGER
        )
    """
    execute_query(query)


def insert_interface(interface):
    # Insert a new interface into the database."""
    query = """
        INSERT INTO interfaces (name, description, max_frame_size, config, port_channel_id) 
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (
        interface.name,
        interface.description,
        interface.max_frame_size,
        json.dumps(interface.config),
        interface.port_channel_id
    )
    execute_query(query, params)
