import psycopg2

connection = psycopg2.connect(dbname="scraper_db", host="127.0.0.1", user="m7d", password="123", port="5432")


def add_question_to_db(question):
    schema_name = question.description.name.replace(" ", "_").lower()

    create_schema(schema_name)
    create_tables(schema_name, question.tables)


def create_schema(schema_name):
    with connection:
        with connection.cursor() as cursor:
            query = f'CREATE SCHEMA IF NOT EXISTS {schema_name}'
            cursor.execute(query)


def convert_column_type(column_type):
    match column_type:
        case 'datetime':
            return 'date'
        case _:
            return column_type


def create_tables(schema_name, tables):
    for table in tables:
        query = f'create table if not exists {schema_name}.{table.name}('

        for column_name, column_type in table.columns.items():
            converted_column_type = convert_column_type(column_type)
            query += f'{column_name} {converted_column_type},'

        query = query[:-1]
        query += ');'

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)


def close_connection():
    connection.close()
