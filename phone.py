class PhoneFormatException(Exception):
    pass

def check_phone(phone):
    operator_codes = {
        "МТС": ["910", "911", "912", "913", "914", "915", "916", "917", "918", "919", "980", "981", "982", "983",
                "984", "985", "986", "987", "988", "989"],
        "МегаФон": ["920", "921", "922", "923", "924", "925", "926", "927", "928", "929", "930", "931", "932",
                    "933", "934", "935", "936", "937", "938", "939"],
        "Билайн": ["902", "903", "904", "905", "906", "960", "961", "962", "963", "964", "965", "966", "967", "968",
                   "969"]
    }

    try:
        phone = "".join(phone.split())
        if phone.find("+7") != 0 and phone.find("8") != 0 and phone.find("+359") != 0 and phone.find("+1") != 0 and phone.find("+55") != 0:
            raise PhoneFormatException("Неверный формат")

        if not all(phone.split("-")):
            raise PhoneFormatException("Неверный формат")
        else:
            phone = phone.replace("-", "")
            start_bt = phone.find("(")
            end_bt = phone.find(")")

        if start_bt > -1:
            if end_bt < start_bt or not phone[start_bt + 1: end_bt].isdigit() or not phone.count("(") == 1 or not phone.count(")") == 1:
                raise PhoneFormatException("Неверный формат")
        elif end_bt > -1:
            raise PhoneFormatException("Неверный формат")

        phone = phone.replace("(", "").replace(")", "")

        if phone.find("8") == 0:
            phone = "+7" + phone[1:]

        if not phone[1:].isdigit():
            raise PhoneFormatException("Неверный формат")

        if phone.find("+7") == 0:
            if len(phone[1:]) != 11:
                raise PhoneFormatException("Неверное количество цифр")

            code = phone[2:5]
            for operator, codes in operator_codes.items():
                if code in codes:
                    raise PhoneFormatException(operator)

            raise PhoneFormatException("Не определяется сотовый оператор")

        elif phone.find("+359") == 0:
            if len(phone[1:]) != 13:
                raise PhoneFormatException("Неверное количество цифр")
            return phone

        elif phone.find("+55") == 0:
            if len(phone[1:]) != 12:
                raise PhoneFormatException("Неверное количество цифр")
            return phone

        elif phone.find("+1") == 0:
            if len(phone[1:]) != 11:
                raise PhoneFormatException("Неверное количество цифр")
            return phone

        else:
            raise PhoneFormatException("Не определяется код страны")

    except PhoneFormatException as e:
        return e

try:
    result = check_phone(input())
    print(result)
except PhoneFormatException as e:
    print(e)