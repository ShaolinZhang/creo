from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import os, sys, math, time, datetime, uuid

load_dotenv()

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

conn = create_connection(os.getenv("HOSTNAME"), os.getenv("USERNAME"), os.getenv("PASSWORD"), os.getenv("DATABASE_NAME"))

create_user_table = """
CREATE TABLE IF NOT EXISTS user(
	username varchar(255) NOT NULL UNIQUE,
	email varchar(255) NOT NULL UNIQUE,
	password varchar(255) NOT NULL,
	PRIMARY KEY (username),
	CONSTRAINT UC_USER UNIQUE (username, email)
);
"""

create_deal_table = """
CREATE TABLE IF NOT EXISTS deal(
	ID int NOT NULL AUTO_INCREMENT,
	addedBy varchar(255) NOT NULL,
	projectName text NOT NULL UNIQUE,
	projectScore text,
	teamScore text,
	projectStatus text,
	industry varchar(255),
	memo longtext,
    fileUpload text,
	PRIMARY KEY (ID),
	FOREIGN KEY (addedBy) REFERENCES user(username)
);
"""

create_contact_table = """
CREATE TABLE IF NOT EXISTS contact(
    ID int NOT NULL AUTO_INCREMENT,
    addedBy varchar(255) NOT NULL,
    contactName text NOT NULL,
    contactMethod text,
    contactNote longtext,
    PRIMARY KEY (ID),
    FOREIGN KEY (addedBy) REFERENCES user(username)
);
"""

execute_query(conn, create_user_table)
execute_query(conn, create_deal_table)
execute_query(conn, create_contact_table)

print("Database initialization successful")
