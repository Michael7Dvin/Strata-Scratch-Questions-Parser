import psycopg2

connection = psycopg2.connect(dbname="scraper_db", host="127.0.0.1", user="m7d", password="123", port="5432")


def add_question_to_db(question):
    schema_name = question_name_to_schema_name(question.description.name)
    create_schema(schema_name)


def question_name_to_schema_name(name):
    name = name.replace(" ", "_")
    name = name.lower()
    return name


def create_schema(name):
    with connection:
        with connection.cursor() as cursor:
            query = f'CREATE SCHEMA IF NOT EXISTS {name}'
            cursor.execute(query)


def close_connection():
    connection.close()
