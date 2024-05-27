# Задание 1

# def has_consecutive(password):
#     keyboard_layouts = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
#                         'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
#     for i in range(len(password) - 2):
#         triple = password[i:i+3].lower()
#         for layout in keyboard_layouts:
#             if triple in layout:
#                 return True
#     return False
#
#
# digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# password = input('Введите пароль: ')
# conditions = [len(password) > 8,
#               any(c.islower() for c in password),
#               any(c.isupper() for c in password),
#               any(c in digits for c in password),
#               not has_consecutive(password)]
#
# if all(conditions):
#     print('ok')
# else:
#     print('error')



# Задание 2

# class PasswordError(Exception):
#     pass
#
# class LengthError(PasswordError):
#     pass
#
# class LetterError(PasswordError):
#     pass
#
# class DigitError(PasswordError):
#     pass
#
# class SequenceError(PasswordError):
#     pass
#
#
# def has_consecutive(password):
#     keyboard_layouts = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
#                         'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
#     for i in range(len(password) - 2):
#         triple = password[i:i+3].lower()
#         for layout in keyboard_layouts:
#             if triple in layout:
#                 return True
#     return False
#
#
# def check_password(password):
#     if len(password) < 9:
#         raise LengthError("Длина пароля должна быть не менее 9 символов")
#
#     if password.islower() or password.isupper():
#         raise LetterError("Пароль должен содержать символы обоих регистров")
#
#     if not any(char.isdigit() for char in password):
#         raise DigitError("Пароль должен содержать хотя бы одну цифру")
#
#     if has_consecutive(password):
#         raise SequenceError("Комбинация из 3 буквенных символов, стоящих рядом")
#
#     return 'ok'
#
#
# try:
#     password = input("Введите пароль: ")
#     print(check_password(password))
# except PasswordError as e:
#     print("Ошибка в пароле:", e)




# Задание 3

# def has_consecutive(password):
#     keyboard_layouts = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
#                         'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
#     for i in range(len(password) - 2):
#         triple = password[i:i+3].lower()
#         for layout in keyboard_layouts:
#             if triple in layout:
#                 return True
#     return False
#
#
# def check_password(password):
#     try:
#         assert len(password) >= 9, "Длина пароля должна быть не менее 9 символов"
#
#         assert any(c.islower() for c in password) and any(
#             c.isupper() for c in password), "Пароль должен содержать символы верхнего и нижнего регистра"
#
#         assert any(c.isdigit() for c in password), "Пароль должен содержать цифры"
#
#         assert not has_consecutive(password), "Пароль не должен содержать 3 подряд идущих символа"
#
#         return "ok"
#     except AssertionError as e:
#         return "error: " + str(e)
#     except Exception as e:
#         return "error: " + str(e)
#
#
# password = input("Введите пароль: ")
# result = check_password(password)
# print(result)




# Задание 4


# class PasswordError(Exception):
#     pass
#
# class LengthError(PasswordError):
#     pass
#
# class LetterError(PasswordError):
#     pass
#
# class DigitError(PasswordError):
#     pass
#
# class SequenceError(PasswordError):
#     pass
#
#
# def has_consecutive(password):
#     keyboard_layouts = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
#                         'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
#     for i in range(len(password) - 2):
#         triple = password[i:i+3].lower()
#         for layout in keyboard_layouts:
#             if triple in layout:
#                 return True
#     return False
#
#
# def check_password(password):
#     if password == 'Ctrl+Break':
#         raise KeyboardInterrupt
#
#     elif len(password) < 9:
#         raise LengthError("Длина пароля должна быть не менее 9 символов")
#
#     elif password.islower() or password.isupper():
#         raise LetterError("Пароль должен содержать символы обоих регистров")
#
#     elif not any(char.isdigit() for char in password):
#         raise DigitError("Пароль должен содержать хотя бы одну цифру")
#
#     elif has_consecutive(password):
#         raise SequenceError("Комбинация из 3 буквенных символов, стоящих рядом")
#
#     return 'ok'
#
#
# while True:
#     try:
#         password = input("Введите пароль: ")
#         print(check_password(password))
#         break
#
#     except KeyboardInterrupt:
#         print("Bye-Bye")
#         break
#
#     except PasswordError as e:
#         print("Ошибка в пароле:", e)





# Задание 5

# class DefaultList(list):
#     def __init__(self, default_value, *args):
#         self.default_value = default_value
#         super().__init__(*args)
#
#     def __getitem__(self, index):
#         try:
#             return super().__getitem__(index)
#         except IndexError:
#             return self.default_value
#
# # Пример использования
# my_list = DefaultList(0, [1, 2, 3])
#
# print(my_list[1])
# print(my_list[10])