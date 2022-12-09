import sqlite3
import json
from datetime import datetime


def set_start_data(user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""INSERT OR IGNORE INTO users_data (user_id) VALUES (?);""", (user_id,))
        c.execute("""UPDATE users_data SET (check_in, check_out, adults_count, kids_ages, dates_flag, 
                    guests_count_flag, request) 
            = (NULL, NULL, NULL, NULL, 0, 0, NULL) WHERE user_id = ?;""", (user_id,))
        db.commit()


def set_adults_count(adults_number, user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""UPDATE users_data SET adults_count = ? WHERE user_id = ?;""", (adults_number, user_id))
        db.commit()


def get_adults_count(user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        adults_count = c.execute("""SELECT adults_count FROM users_data WHERE user_id = ?;""", (user_id,)).fetchone()[0]
    return adults_count


def set_check_in_date(date, user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""UPDATE users_data SET check_in = ? WHERE user_id = ?;""", (date, user_id))
        db.commit()


def get_check_in_date(user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""SELECT check_in FROM users_data WHERE user_id = ?;""", (user_id,))
        check_in_date = datetime.strptime(c.fetchone()[0], '%Y-%m-%d').date()
    return check_in_date


def set_check_out_date(date, user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""UPDATE users_data SET check_out = ? WHERE user_id = ?;""", (date, user_id))
        db.commit()


def get_check_out_date(user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""SELECT check_out FROM users_data WHERE user_id = ?;""", (user_id,))
        check_out_date = datetime.strptime(c.fetchone()[0], '%Y-%m-%d').date()
    return check_out_date


def set_dates_flag(flag, user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""UPDATE users_data SET dates_flag = ? WHERE user_id = ?;""", (flag, user_id))
        db.commit()


def get_dates_flag(user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""SELECT dates_flag FROM users_data WHERE user_id = ?;""", (user_id,))
        dates_flag = c.fetchone()[0]
    return dates_flag


def set_guests_count_flag(flag, user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""UPDATE users_data SET guests_count_flag = ? WHERE user_id = ?;""", (flag, user_id))
        db.commit()


def get_guests_count_flag(user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""SELECT guests_count_flag FROM users_data WHERE user_id = ?;""", (user_id,))
        guests_count_flag = c.fetchone()[0]
    return guests_count_flag


def set_current_request(request_data, user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""UPDATE users_data SET request = ? WHERE user_id = ?;""", (json.dumps(request_data), user_id))
        db.commit()


def get_current_request(user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        payload = json.loads(c.execute("""SELECT request FROM users_data WHERE user_id = ?;""",
                                       (user_id,)).fetchone()[0])
    return payload


def set_history_data(command, hotels_dict, user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""INSERT INTO users_requests (user_id, date_of_request, command, request) VALUES (?,?,?,?);""",
                  (user_id, datetime.now(), command, json.dumps(hotels_dict)))
        db.commit()


def get_history_data(user_id, starting_day=0):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        history_data = c.execute("""SELECT date_of_request, command, request FROM users_requests 
        WHERE user_id = ? AND datetime(date_of_request) > ? ORDER BY datetime(date_of_request) DESC;""",
                                 (user_id, starting_day)).fetchall()
    return history_data


def set_kids_ages(ages, user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        c.execute("""UPDATE users_data SET kids_ages = ? WHERE user_id = ?;""", (ages, user_id))
        db.commit()


def get_kids_ages(user_id):
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
        current_kids_ages = c.execute("""SELECT kids_ages FROM users_data WHERE user_id = ?;""",
                                      (user_id,)).fetchone()[0]
    return current_kids_ages
