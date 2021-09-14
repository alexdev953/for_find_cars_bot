from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PERSON_TYPE_DICT = {'P': 'Фізична особа',
                    'J': 'Юридична особа',
                    None: 'Інформація відсутня'}


def format_msg_lp(data: list, number_lp: str):
    if data:
        vin_keyboard = InlineKeyboardMarkup(row_width=1)
        answer_list = []
        for val in data:
            message = message_ans(val)
            vin_code_id = val.get('vin_code_id', 'Пусто')
            if vin_code_id != '1951':
                vin_keyboard.add(InlineKeyboardButton('Перевірити по VIN', callback_data=f"v@{vin_code_id}"))
            answer_list.append((message, vin_keyboard))
        return answer_list

    else:
        answer = f'По номеру {number_lp}, нічого не знайдено'
        return answer


def message_ans(data: dict):
    number_plate = data.get('number_plate', 'Пусто')
    operation = data.get('operation', 'Пусто')
    date_operation = data.get('date_operation', 'Пусто')
    dep_name = data.get('dep_name', 'Пусто')
    person_type = data.get('person_type', None)
    addres_person = data.get('addres_person', 'Пусто')
    vin_code = data.get('vin_code', 'Пусто')
    brand = data.get('brand', 'Пусто')
    model = data.get('model', 'Пусто')
    year = data.get('year', 'Пусто')
    fuel = data.get('fuel', 'Пусто')
    color = data.get('color', 'Пусто')
    kind = data.get('kind', 'Пусто')
    body = data.get('body', 'Пусто')
    purpose = data.get('purpose', 'Пусто')
    capacity = data.get('capacity', 0)
    weight = data.get('weight', 'Пусто')
    total_weight = data.get('total_weight', 'Пусто')
    message = f'<b>Номер авто: </b>{number_plate}\n<b>Операція: </b>{operation}\n<b>Дата операції: </b>{date_operation}\n' \
              f'<b>Сервісний центр: </b>{dep_name}\n<b>Тип особи: </b>{PERSON_TYPE_DICT[person_type]}\n' \
              f'<b>Адреса реєстрації особи: </b>{addres_person}\n' \
              f'<b>VIN:</b> {vin_code}\n<b>Назва авто: </b>{brand}\n<b>Модель:</b> {model}\n<b>Рік випуску: </b>{year}\n<b>Паливо: </b>{fuel}\n' \
              f'<b>Колір:</b> {color}\n<b>Тип авто:</b> {kind}\n<b>Кузов:</b> {body}\n<b>Призначеня: </b>{purpose}\n<b>Об\'єм двигуна: </b>{round(int(capacity)/1000, 1)}\n' \
              f'<b>Вага:</b> {weight}кг.\n<b>Повна вага:</b> {total_weight}кг.'
    return message


def format_msg_vin(data: list):
    if data:
        answer_list = []
        for val in data:
            message = message_ans(val)
            answer_list.append(message)
        return answer_list

    else:
        answer = f'По VIN нічого не знайдено'
        return [answer]
