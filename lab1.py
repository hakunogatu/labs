def arithmetic_operation(operation):
    if operation == "+":
        return lambda x, y: x + y
    if operation == "-":
        return lambda x, y: x - y
    if operation == "*":
        return lambda x, y: x * y
    if operation == "/":
        return lambda x, y: x / y
    else:
        return print("Неверная операция")

operation = arithmetic_operation("+")
print(operation(1, 4))




# 2
def simple_map(transformation, values):
    result = []
    for value in values:
        result.append(transformation(value))
    return result


values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(*simple_map(operation, values))




# 3
one = 4
two = 5

RomanNumbers = {'M': 1000, 'CM': 900, 'D': 500,
'CD': 400, 'C': 100, 'XC': 90,
'L': 50, 'XL': 40, 'X': 10,
'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

def num_to_roman(num):
    result = ""
    while num > 0:
        for key, value in RomanNumbers.items():
            if num >= value:
                result += key
                num -= value
                break
    return result

def roman():
    global three
    three = one + two
    roman_one = num_to_roman(one)
    roman_two = num_to_roman(two)
    roman_three = num_to_roman(three)
    print(roman_one, "+", roman_two, "=", roman_three)

roman()




# 4
call_counts = {}
def get_transactions(t):
    if t == "print_it":
        for key, value in call_counts.items():
            sum_result = value[0]
            counter = value[1]
            print(counter, key, sum_result)
        return

    tel = t.split('-')[0]
    type = t.split('-')[1].split(':')[0]
    sum = int(t.split('-')[1].split(':')[1])

    if type in call_counts:
        myValues = call_counts[type]
        myValues[0] += sum
        myValues[1] += 1
    else:
        call_counts[type] = [sum, 1]


get_transactions("880005553535-перевод:100")
get_transactions("111111111-перевод:1000")
get_transactions("880005553535-оплата_жкх:10000")
get_transactions("89065664312-перевод:50000000")
get_transactions('print_it')




# 5
def same_by(characteristic, objects):
    for obj in objects:
        if characteristic(obj) == characteristic(objects[0]):
            continue
        else:
            return False
    return True

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')