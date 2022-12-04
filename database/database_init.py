import sqlite3


def db_create():
    db = sqlite3.connect("users.db", check_same_thread=False)
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users_data(
        user_id INT PRIMARY KEY,
        check_in DATE,
        check_out DATE,
        adults_count TINYINT,
        kids_ages TEXT,
        dates_flag TINYINT,
        guests_count_flag TINYINT,
        request JSON
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS users_requests(
        user_id INT,
        date_of_request DATETIME,
        request JSON
        )""")

    db.commit()
    db.close()
