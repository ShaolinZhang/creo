import os
import pytest
from dotenv import load_dotenv
import mysql.connector
from server import app as flask_app

load_dotenv('.env.dev')


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
    )
    return connection


def execute_query(connection, query):
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    connection.commit()
    return cursor


def test_connection():
    return create_connection(
        os.getenv("HOSTNAME"),
        os.getenv("USERNAME"),
        os.getenv("PASSWORD"),
        os.getenv("DATABASE_NAME")
    )


def test_user_table():
    return execute_query(
        create_connection(
            os.getenv("HOSTNAME"),
            os.getenv("USERNAME"),
            os.getenv("PASSWORD"),
            os.getenv("DATABASE_NAME")
        ),
        "SELECT 1 FROM user;"
    )


def test_deal_table():
    return execute_query(
        create_connection(
            os.getenv("HOSTNAME"),
            os.getenv("USERNAME"),
            os.getenv("PASSWORD"),
            os.getenv("DATABASE_NAME")
        ),
        "SELECT 1 FROM deal;"
    )


def test_contact_table():
    return execute_query(
        create_connection(
            os.getenv("HOSTNAME"),
            os.getenv("USERNAME"),
            os.getenv("PASSWORD"),
            os.getenv("DATABASE_NAME")
        ),
        "SELECT 1 FROM contact;"
    )


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
