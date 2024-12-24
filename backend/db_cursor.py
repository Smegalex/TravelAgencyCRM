import oracledb


def get_db_cursor():
    # Establish connection
    conn = oracledb.connect(
        user="web_crm",
        password="1",
        dsn="localhost:1521/xepdb1"
    )

    # Check if connection is successful
    print("Connection successful!")

    # Create a cursor to interact with the database
    cursor = conn.cursor()

    return conn, cursor

# Функція для вибірки даних з довільної таблиці за id або всі записи з обробкою помилок


def select_records(table_name, record_id=None, where=None):
    # Отримуємо підключення та курсор
    conn, cursor = None, None
    try:
        conn, cursor = get_db_cursor()

        # Створюємо основний SQL запит
        sql_query = f"SELECT * FROM {table_name}"
        params = {}
        # Якщо передано id, додаємо умову для вибірки по id
        if record_id is not None:
            sql_query += f" WHERE id = :id"
            params = {"id": record_id}
        elif where is not None:
            # Якщо передано where, додаємо його до умови
            sql_query += f" WHERE {where}"
            params = {}

        # Якщо id та where не передано, вибираємо всі записи
        sql_query += " ORDER BY id ASC"

        # Виконуємо запит
        cursor.execute(sql_query, params)

        # Отримуємо результати
        records = cursor.fetchall()
        print(records)
        # Повертаємо отримані записи
        return records

    except Exception as e:
        # Виводимо повідомлення про помилку
        print(f"Error occurred while querying {table_name}: {e}")
        return None

    finally:
        # Переконуємося, що з'єднання буде закрито навіть у разі помилки
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# Функція для вставки нового елемента в таблицю
def insert_new_record(table_name, record_data):
    # Отримуємо підключення та курсор
    conn, cursor = get_db_cursor()

    # Формуємо динамічний SQL запит для вставки даних
    columns = ', '.join(record_data.keys())  # Підготовка імен стовпців
    # Підготовка плейсхолдерів для значень
    placeholders = ', '.join([f":{key}" for key in record_data.keys()])

    # Створюємо SQL запит для вставки в вказану таблицю
    sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    print(sql_query)
    try:
        # Виконання запиту
        cursor.execute(sql_query, record_data)

        # Збереження змін у базі даних
        conn.commit()

        print(f"New record inserted into {table_name} successfully")

    except Exception as e:
        # Виведення помилки, якщо щось пішло не так
        print(f"Error inserting record into {table_name}: {e}")
        conn.rollback()

    finally:
        # Закриваємо курсор і підключення
        cursor.close()
        conn.close()


def get_last_id(table_name):
    if not table_name:
        print("Table name must be provided.")
        return None

    conn, cursor = get_db_cursor()
    if conn is None or cursor is None:
        print("Failed to establish database connection or cursor.")
        return None

    try:
        # Define the query to get the first row's ID ordered by ID DESC
        query = f"""
        SELECT id
        FROM {table_name}
        WHERE ROWNUM = 1
        ORDER BY id DESC
        """

        # Execute the query
        cursor.execute(query)

        # Fetch the result (it should return a single row)
        row = cursor.fetchone()
        print(row[0])

        if row:
            return row[0]  # Return the ID value from the query result
        else:
            print("No rows found.")
            return None

    except oracledb.DatabaseError as e:
        print(f"Error executing the query: {e}")
        return None

    finally:
        # Ensure the connection is closed after the operation
        if conn:
            conn.close()
            print("Connection closed.")


def update_row_in_table(table_name, row_id, row_data):
    if not table_name:
        print("Table name must be provided.")
        return None

    if not row_data or not isinstance(row_data, dict):
        print("Row data must be a non-empty dictionary.")
        return None

    # Get database connection and cursor
    conn, cursor = get_db_cursor()
    if conn is None or cursor is None:
        print("Failed to establish database connection or cursor.")
        return None

    try:
        # Prepare the column names and values for the update query
        columns = ', '.join(f"{key} = :{key}" for key in row_data.keys())

        # Create the SQL query to update the row
        sql = f"UPDATE {table_name} SET {columns} WHERE id = :row_id"

        # Execute the query with the data
        cursor.execute(sql, {**row_data, 'row_id': row_id})

        # Commit the transaction
        conn.commit()

        print(f"Row with id {row_id} updated successfully in {table_name}!")

    except oracledb.DatabaseError as e:
        print(f"Error executing the query: {e}")
        return None

    finally:
        # Ensure the cursor and connection are closed after the operation
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if conn:
            conn.close()
            print("Connection closed.")


def delete_row_from_table(table_name, row_id):
    if not table_name:
        print("Table name must be provided.")
        return None

    if not row_id:
        print("Row ID must be provided.")
        return None

    # Get database connection and cursor
    conn, cursor = get_db_cursor()
    if conn is None or cursor is None:
        print("Failed to establish database connection or cursor.")
        return None

    try:
        # Create the SQL query to delete the row
        sql = f"DELETE FROM {table_name} WHERE id = :row_id"

        # Execute the query
        cursor.execute(sql, {'row_id': row_id})

        # Commit the transaction
        conn.commit()

        print(f"Row with id {row_id} deleted successfully from {table_name}!")

    except oracledb.DatabaseError as e:
        print(f"Error executing the query: {e}")
        return None

    finally:
        # Ensure the cursor and connection are closed after the operation
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if conn:
            conn.close()
            print("Connection closed.")


def check_user_credentials(email, password):
    """
    Перевіряє облікові дані користувача за email та паролем.
    """
    conn, cursor = get_db_cursor()
    try:
        # Виконання запиту для перевірки користувача
        sql_query = """
        SELECT COUNT(*) 
        FROM managers 
        WHERE email = :email AND password = :password
        """
        cursor.execute(sql_query, {"email": email, "password": password})
        result = cursor.fetchone()

        # Повернення True, якщо знайдено запис, інакше False
        return result[0] > 0

    except Exception as e:
        print(f"Error checking credentials: {e}")
        return False

    finally:
        # Закриваємо курсор і підключення
        if cursor:
            cursor.close()
        if conn:
            conn.close()
