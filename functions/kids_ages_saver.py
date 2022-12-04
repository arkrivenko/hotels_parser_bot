from database.database_functions import get_kids_ages, set_kids_ages


def kids_ages_saver(kid_age, user_id):
    current_kids_ages = get_kids_ages(user_id)
    if current_kids_ages:
        updated_kids_ages = '_'.join([current_kids_ages, kid_age])
        set_kids_ages(updated_kids_ages, user_id)
    else:
        set_kids_ages(kid_age, user_id)
