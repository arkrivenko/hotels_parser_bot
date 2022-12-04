from loader import bot
from utils.set_bot_commands import set_default_commands
from database.database_init import db_create
import functions


if __name__ == "__main__":
    db_create()
    print('db created')
    set_default_commands(bot)
    print('commands added')
    bot.infinity_polling()
