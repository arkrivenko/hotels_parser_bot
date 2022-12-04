from database.database_functions import get_dates_flag, get_guests_count_flag


def flags_checker(user_id):
    dates_flag = get_dates_flag(user_id)
    guests_count_flag = get_guests_count_flag(user_id)

    if dates_flag == 1 and guests_count_flag == 1:
        return 0
    elif dates_flag == 0:
        return 1
    else:
        return 2
