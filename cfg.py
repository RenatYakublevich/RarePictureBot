from vedis import Vedis
import config
import os.path

gg = 0


def update_list():
    path = './picture'
    countd = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))
    return countd
update_list()
count_fr_count = 1
picture_list = []
while update_list() >= count_fr_count:
    picture_list.append(count_fr_count)
    count_fr_count +=1
# Пытаемся узнать из базы «состояние» пользователя
def get_current_state(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id].decode() # Если используете Vedis версии ниже, чем 0.7.1, то .decode() НЕ НУЖЕН
        except KeyError:  # Если такого ключа почему-то не оказалось
            return config.States.S_START.value  # значение по умолчанию - начало диалога

# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False
