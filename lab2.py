# 1
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    def intersection(self, other):
        x1 = max(self.x, other.get_x())
        y1 = max(self.y, other.get_y())
        x2 = min(self.x + self.w, other.get_x() + other.get_w())
        y2 = min(self.y + self.h, other.get_y() + other.get_h())

        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2 - x1, y2 - y1)
        else:
            return None


rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(10, 0, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
print()


# # 2
# class LeftParagraph:
#     def __init__(self, width):
#         self.width = width
#         self.text = ""
#
#     def add_word(self, word):
#         lines = self.text.split("\n")
#         if len((lines[-1] + word)) >= self.width + 1:
#             self.text += "\n"
#         self.text += word + " "
#
#     def end(self):
#         lines = self.text.split("\n")
#         for line in lines:
#             print(line)
#         self.text = ""
#
#
# class RightParagraph:
#     def __init__(self, width):
#         self.width = width
#         self.text = ""
#
#     def add_word(self, word):
#         lines = self.text.split("\n")
#         if len((lines[-1] + word)) >= self.width + 1:
#             self.text += "\n"
#         self.text += word + " "
#
#     def end(self):
#         lines = self.text.split("\n")
#         for line in lines:
#             while len(line) <= self.width:
#                 line = " " + line
#             print(line)
#         self.text = ""
#
#
# lp = LeftParagraph(8)
# lp.add_word('abc')
# lp.add_word('defg')
# lp.add_word('hi')
# lp.add_word('jklmnopq')
# lp.add_word('r')
# lp.add_word('stuv')
# lp.end()
# print()
#
# rp = RightParagraph(8)
# rp.add_word('abc')
# rp.add_word('defg')
# rp.add_word('hi')
# rp.add_word('jklmnopq')
# rp.add_word('r')
# rp.add_word('stuv')
# rp.end()
# print()
#
#
#
#
# # 3
# class SeaMap:
#     def __init__(self):
#         self.map = [[None] * 10 for _ in range(10)]
#
#     def shoot(self, row, col, result):
#         self.map[row][col] = result
#         if result == 'sink':
#             for i in range(max(0, row - 1), min(len(self.map), row + 2)):
#                 for j in range(max(0, col - 1), min(len(self.map[row]), col + 2)):
#                     if self.map[i][j] == self.map[row][col]:
#                         self.map[i][j] = 'hit'
#                         continue
#                     self.map[i][j] = 'miss'
#
#     def cell(self, row, col):
#         if self.map[row][col] == None:
#             return '.'
#         elif self.map[row][col] == 'hit':
#             return 'x'
#         elif self.map[row][col] == 'miss':
#             return '*'
#
#
# sm = SeaMap()
# sm.shoot(2, 0, 'sink')
# sm.shoot(6, 9, 'hit')
# for row in range(10):
#     for col in range(10):
#         print(sm.cell(row, col), end='')
#     print()
#
#
#
#
# #4
# import math
# class Weapon:
#     def __init__(self, name, damage, range):
#         self.name = name
#         self.damage = damage
#         self.range = range
#
#     def __str__(self):
#         print(self.name)
#
#     def hit(self, actor, target):
#         if target.hp <= 0:
#             print('Враг уже повержен')
#         else:
#             distance = self.calculate_distance(actor, target)
#             if distance > self.range:
#                 print(f"Враг слишком далеко для оружия {self.name}")
#             else:
#                 print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
#                 target.get_damage(self.damage)
#
#     def calculate_distance(self, actor, target):
#         dx = actor.pos_x - target.pos_x
#         dy = actor.pos_y - target.pos_y
#         return math.sqrt(dx ** 2 + dy ** 2)
#
# class BaseCharacter:
#     def __init__(self, pos_x, pos_y, hp):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.hp = hp
#
#     def move(self, delta_x, delta_y):
#         self.pos_x += delta_x
#         self.pos_y += delta_y
#
#     def is_alive(self):
#         if self.hp > 0:
#             return True
#         else:
#             return False
#
#     def get_damage(self, amount):
#         self.hp -= amount
#
#     def get_coords(self):
#         coords = [self.pos_x, self.pos_y]
#         return coords
#
#
# class BaseEnemy(BaseCharacter):
#     def __init__(self, pos_x, pos_y, weapon, hp):
#         super().__init__(pos_x, pos_y, hp)
#         self.weapon = weapon
#
#     def __str__(self):
#         print(f'Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}')
#
#     def hit(self, target):
#         if isinstance(target, MainHero):
#             self.weapon.hit(self, target)
#         else:
#             print('Могу ударить только Главного героя')
#
#
# class MainHero(BaseCharacter):
#     def __init__(self, pos_x, pos_y, name, hp):
#         super().__init__(pos_x, pos_y, hp)
#         self.name = name
#         self.my_weapons = []
#         self.weapon = None
#         self.max_hp = 200
#
#     def hit(self, target):
#         if not self.weapon:
#             print('Я безоружен')
#         else:
#             if isinstance(target, BaseEnemy):
#                 self.weapon.hit(self, target)
#             else:
#                 print('Могу ударить только врага')
#
#     def add_weapon(self, weapon):
#         if isinstance(weapon, Weapon):
#             if not self.my_weapons:
#                 self.weapon = weapon
#                 self.my_weapons.append(weapon)
#             else:
#                 self.my_weapons.append(weapon)
#             print(f'Подобрал {weapon.name}')
#         else:
#             print('Это не оружие')
#
#     def next_weapon(self):
#         if not self.my_weapons:
#             print('Я безоружен')
#         elif len(self.my_weapons) == 1:
#             print('У меня только одно оружие')
#         else:
#             self.my_weapons.append(self.my_weapons.pop(0))
#             self.weapon = self.my_weapons[0]
#             print(f'Сменил оружие на {self.weapon.name}')
#
#     def heal(self, amount):
#         self.hp += amount
#         if self.hp > self.max_hp:
#             self.hp = self.max_hp
#
#
# weapon1 = Weapon("Короткий меч", 5, 1)
# weapon2 = Weapon("Длинный меч", 7, 2)
# weapon3 = Weapon("Лук", 3, 10)
# weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
# princess = BaseCharacter(100, 100, 100)
# archer = BaseEnemy(50, 50, weapon3, 100)
# armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
# archer.hit(armored_swordsman)
# armored_swordsman.move(10, 10)
# print(armored_swordsman.get_coords())
# main_hero = MainHero(0, 0, "Король Артур", 200)
# main_hero.hit(armored_swordsman)
# main_hero.next_weapon()
# main_hero.add_weapon(weapon1)
# main_hero.hit(armored_swordsman)
# main_hero.add_weapon(weapon4)
# main_hero.hit(armored_swordsman)
# main_hero.next_weapon()
# main_hero.hit(princess)
# main_hero.hit(armored_swordsman)
# main_hero.hit(armored_swordsman)


# 5

# class MailServer:
#     all_servers_mails = []
#
#     def __init__(self):
#         self.mails = {}
#         MailServer.all_servers_mails.append(self.mails)
#
#     def receive_data(self):
#         print(self.mails)
#
#
# class MailClient:
#     all_users = []
#
#     def __init__(self, server, user):
#         self.server = server
#         self.user = user
#         MailClient.all_users.append(user)
#
#     def send_mail(self, server, receiver, message):
#         if receiver in MailClient.all_users:
#             key = self.user + " - " + receiver
#             if key in server.mails:
#                 server.mails[key].append(message)
#             else:
#                 server.mails[key] = [message]
#         else:
#             print('Данного пользователя не существует')
#
#     def receive_mail(self):
#         for server in MailServer.all_servers_mails:
#             server_keys = list(server.keys())
#             for key in server_keys:
#                 sender = key.split(' - ')[0]
#                 receiver = key.split(' - ')[1]
#                 if receiver == self.user:
#                     for sender_messages in server[key]:
#                         print('Message from ', sender, ': ', sender_messages, sep='')
#                     del server[key]
#
# server1 = MailServer()
# server2 = MailServer()
#
# client1 = MailClient(server1, "test@mail.ru")
# client1.send_mail(server1, "unknown", "hello")
#
# client2 = MailClient(server1, "user@mail.ru")
#
# client1.send_mail(server1, "user@mail.ru", "123")
# client1.send_mail(server1, "user@mail.ru", "asdasdf")
#
# client2.send_mail(server1, "test@mail.ru", "privet")
# client2.send_mail(server1, "test@mail.ru", "kak dela")
# client2.send_mail(server2, "test@mail.ru", "msg from server2")
#
# client1.receive_mail()