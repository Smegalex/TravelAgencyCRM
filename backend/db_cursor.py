
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
def select_records(table_name, record_id=None):
    # Отримуємо підключення та курсор
    conn, cursor = None, None
    try:
        conn, cursor = get_db_cursor()

        # Якщо передано id, створюємо SQL запит для вибірки по id
        if record_id is not None:
            sql_query = f"SELECT * FROM {table_name} WHERE id = :id"
            cursor.execute(sql_query, {"id": record_id})
        else:
            # Якщо id не передано, вибираємо всі записи
            sql_query = f"SELECT * FROM {table_name}"
            cursor.execute(sql_query)

        # Отримуємо результати
        records = cursor.fetchall()

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
    placeholders = ', '.join([f":{key}" for key in record_data.keys()])  # Підготовка плейсхолдерів для значень

    # Створюємо SQL запит для вставки в вказану таблицю
    sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

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
