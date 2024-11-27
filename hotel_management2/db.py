import sqlite3

def create_connection():
    """Создание подключения к базе данных SQLite."""
    try:
        conn = sqlite3.connect('hotel_clients.db')
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def create_table():
    """Создание таблицы для клиентов, если она не существует."""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                passport_data TEXT,  -- Используем TEXT для паспортных данных
                phone_number TEXT,   -- Используем TEXT для номера телефона
                patronymic TEXT,
                birth_date TEXT,
                check_in_date TEXT,
                check_out_date TEXT
            );
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при создании таблицы: {e}")
        finally:
            conn.close()

def add_client(first_name, last_name, patronymic, passport_data, phone_number, birth_date, check_in_date, check_out_date):
    """Добавление нового клиента в базу данных."""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO clients (first_name, last_name, patronymic, passport_data, phone_number, birth_date, check_in_date, check_out_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (first_name, last_name, patronymic, passport_data, phone_number, birth_date, check_in_date, check_out_date))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении клиента: {e}")
        finally:
            conn.close()

def get_all_clients():
    """Получение списка всех клиентов."""
    conn = create_connection()
    clients = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM clients')
            clients = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при получении клиентов: {e}")
        finally:
            conn.close()
    return clients
