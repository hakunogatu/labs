# 1-2 Задание

# def is_palindrome(data):
#     data = data.lower().replace(' ', '')
#
#     if data == data[::-1]:
#         return True
#     else:
#         return False
#
# string = input('Введите строку: ')
#
# if is_palindrome(string):
#     print('YES')
# else:
#     print('NO')





# 3-4 Задание

# def  is_correct_mobile_phone_number_ru(number):
#     number = number.replace(' ', '').replace('-', '')
#
#     if number.startswith('8'):
#         number = number[1:]
#     elif number.startswith('+7'):
#         number = number[2:]
#     else:
#         return False
#
#     if number[0] == '(' and number[4] == ')':
#         number = number[1:4] + number[5:]
#
#     if number.isdigit() and len(number) == 10:
#         return True
#
#
# num = input('Введите телефонный номер: ')
#
# if is_correct_mobile_phone_number_ru(num):
#     print('YES')
# else:
#     print('NO')




# 5-6 Задание

# def strip_punctuation_ru(data):
#     punctuation = ',.:;!?-()[]{}\/"'
#     clear_data = ''.join([ch for ch in data if ch not in punctuation])
#     return clear_data
#
# string = input('Введите строку: ')
# print(strip_punctuation_ru(string))




# 7 Задание

# import unittest
# from reverse import reverse
#
# class TestReverseFunction(unittest.TestCase):
#     def test_empty_string(self):
#         self.assertEqual(reverse(''), '')
#
#     def test_single_character_string(self):
#         self.assertEqual(reverse('a'), 'a')
#
#     def test_palindrome_string(self):
#         self.assertEqual(reverse('radar'), 'radar')
#
#     def test_non_palindrome_string(self):
#         self.assertEqual(reverse('hello'), 'olleh')
#
#     def test_non_string_object(self):
#         with self.assertRaises(TypeError):
#             reverse(123)
#
#     def test_iterable_non_string_object(self):
#         with self.assertRaises(TypeError):
#             reverse([1, 2, 3])
#
# if __name__ == '__main__':
#     unittest.main()





# 8 Задание

# import pytest
# from reverse import reverse
#
# def test_empty_string():
#     assert reverse('') == ''
#
# def test_single_character_string():
#     assert reverse('a') == 'a'
#
# def test_palindrome_string():
#     assert reverse('radar') == 'radar'
#
# def test_non_palindrome_string():
#     assert reverse('hello') == 'olleh'
#
# def test_non_string_object():
#     with pytest.raises(TypeError):
#         reverse(123)
#
# def test_iterable_non_string_object():
#     with pytest.raises(TypeError):
#         reverse([1, 2, 3])





# 9-10 Задание

# import pytest
#
# def count_char(s):
#     if type(s) != str:
#         raise TypeError
#
#     chars_dict = {}
#     s = s.lower()
#
#     for char in s:
#         if char not in chars_dict:
#             chars_dict[char] = 1
#         else:
#             chars_dict[char] += 1
#
#     return chars_dict
#
#
# def test_empty_string():
#     assert count_char('') == {}
#
# def test_single_character_string():
#     assert count_char('a') == {'a': 1}
#
# def test_many_character_string():
#     assert count_char('hello') == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#
# def test_non_string_object():
#     with pytest.raises(TypeError):
#         count_char(123)
#
# def test_iterable_non_string_object():
#     with pytest.raises(TypeError):
#         count_char([1, 2, 3])