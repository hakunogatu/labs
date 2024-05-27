# 1 Задание

# import sys
#
# try:
#     if len(sys.argv) != 3:
#         raise ValueError
#
#     num1 = int(sys.argv[1])
#     num2 = int(sys.argv[2])
#     result = num1 + num2
#
#     print(result)
#
# except Exception:
#     print(0)





# 2 Задание

# import sys
#
#
# class ParamsError(Exception):
#     pass
#
#
# try:
#     if len(sys.argv) == 1:
#         raise ParamsError
#
#     result = 0
#     for i in range(1, len(sys.argv)):
#         if i % 2 == 1:
#             result += int(sys.argv[i])
#         else:
#             result -= int(sys.argv[i])
#
#     print(result)
#
# except ParamsError:
#     print('NO PARAMS')
#
# except Exception as e:
#     print(type(e).__name__)





# 3 Задание

# import sys
#
# try:
#     if len(sys.argv) != 4:
#         raise ValueError
#
#     num1 = float(sys.argv[1])
#     num2 = float(sys.argv[3])
#     operation = sys.argv[2]
#
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         result = num1 / num2
#
#     print(result)
#
# except Exception as e:
#     print(type(e).__name__)





# 4 Задание

# import sys
#
# my_dict = {}
# for arg in sys.argv[1:]:
#     if '=' in arg:
#         key, value = arg.split('=')
#         my_dict[key] = value
#
# if '--sort' in sys.argv:
#     my_dict = dict(sorted(my_dict.items()))
#
# for key, value in my_dict.items():
#     print(f'Key: {key} Value: {value}')






# 5 Задание

# import sys
#
# line_list = []
#
# try:
#     file_path = sys.argv[-1]
#     with open(file_path) as file:
#         for line in file:
#             line = line.rstrip('\n')
#             line_list.append(line)
#
#     if '--sort' in sys.argv:
#         line_list.sort()
#
#     if '--num' in sys.argv:
#         for i in range(0, len(line_list)):
#             print(i, line_list[i])
#
#     else:
#         for line in line_list:
#             print(line)
#
#     if '--count' in sys.argv:
#         rows_count = len(line_list)
#         print('rows count:', rows_count)
#
#
# except Exception:
#     print("ERROR")