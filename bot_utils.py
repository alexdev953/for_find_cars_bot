from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def format_msg_lp(data: list, number_lp: str):
    if data:
        vin_keyboard = InlineKeyboardMarkup(row_width=1)
        answer_list = []
        for val in data:
            number_plate = val['number_plate']
            operation = val['operation']
            date_operation = val['date_operation']
            dep_name = val['dep_name']
            person_type = val['person_type']
            addres_person = val['addres_person']
            vin_code = val['vin_code']
            vin_code_id = val['vin_code_id']
            brand = val['brand']
            model = val['model']
            year = val['year']
            fuel = val['fuel']
            color = val['color']
            kind = val['kind']
            body = val['body']
            purpose = val['purpose']
            capacity = val['capacity']
            weight = val['weight']
            total_weight = val['total_weight']
            message = f'{number_plate}\n{operation}\n{date_operation}\n{dep_name}\n{person_type}\n{addres_person}\n' \
                      f'{vin_code}\n{brand}\n{model}\n{year}\n{fuel}\n{color}\n{kind}\n{body}\n{purpose}\n{capacity}' \
                      f'{weight}\n{total_weight}'
            if vin_code_id != '1951':
                vin_keyboard.add(InlineKeyboardButton('Перевірити по VIN', callback_data=f"v@{vin_code_id}"))
            answer_list.append((message, vin_keyboard))
        return answer_list

    else:
        answer = f'По номеру {number_lp}, нічого не знайдено'
        return [answer]

def format_msg_vin(data: list):
    if data:
        answer_list = []
        for val in data:
            number_plate = val['number_plate']
            operation = val['operation']
            date_operation = val['date_operation']
            dep_name = val['dep_name']
            person_type = val['person_type']
            addres_person = val['addres_person']
            vin_code = val['vin_code']
            brand = val['brand']
            model = val['model']
            year = val['year']
            fuel = val['fuel']
            color = val['color']
            kind = val['kind']
            body = val['body']
            purpose = val['purpose']
            capacity = val['capacity']
            weight = val['weight']
            total_weight = val['total_weight']
            message = f'{number_plate}\n{operation}\n{date_operation}\n{dep_name}\n{person_type}\n{addres_person}\n' \
                      f'{vin_code}\n{brand}\n{model}\n{year}\n{fuel}\n{color}\n{kind}\n{body}\n{purpose}\n{capacity}' \
                      f'{weight}\n{total_weight}'
            answer_list.append(message)
        return answer_list

    else:
        answer = f'По VIN нічого не знайдено'
        return [answer]
