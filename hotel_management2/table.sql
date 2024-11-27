CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    patronymic TEXT,
    passport_data TEXT, 
    phone_number TEXT,
    birth_date TEXT,         
    check_in_date TEXT,       
    check_out_date TEXT    
);
