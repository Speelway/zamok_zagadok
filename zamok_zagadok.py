class Vopros:
    def __init__(self, zagadka):
        self.zagadka = zagadka
    def use(self):
        pass        

class Vopros1(Vopros):
    def __init__(self, zagadka):
        super().__init__(zagadka)
    def use(self):
        print(self.zagadka)
        
class Vopros2(Vopros):
    def __init__(self, zagadka):
        super().__init__(zagadka)
    def use(self):
        print(self.zagadka)

class Vopros3(Vopros):
    def __init__(self, zagadka):
        super().__init__(zagadka)
    def use(self):
        print(self.zagadka)
     
class Vopros4(Vopros):
    def __init__(self, zagadka):
        super().__init__(zagadka)
    def use(self):
        print(self.zagadka)

class Vopros5(Vopros):
    def __init__(self, zagadka):
        super().__init__(zagadka)
    def use(self):
        print(self.zagadka)

a = Vopros1("Без чего ничего никогда не бывает?")
b = Vopros2("Что принадлежит вам, но другие используют это чаще?")
c = Vopros3("Каких камней нет ни в одном море?")
d = Vopros4("Где вода стоит столбом?")
e = Vopros5("Что можно видеть с закрытыми глазами?")
num = 5
print('вы попали в замок загадок, чтобы выбраться вам нужно ответить на все вопросы правильно (на каждый вопрос дается лишь 2 попытки!!!)')
a.use()
h = input()
h = h.lower()
if h == 'названия':
    num -= 1
    print('верно! проходите дальше вам осталось', num, 'комнаты до выхода из замка')
    print('переход в новую комнату...')
    b.use()
else:
    print('неверный ответ(, подумайте еще')
    m = input()
    m = m.lower()
    if m == 'названия':
        num -= 1
        print('верно! проходите дальше вам осталось', num, 'комнаты до выхода из замка')
        print('переход в новую комнату...')
        b.use()
    else:
        print('эта ошибка была ФАТАЛЬНОЙ в вашей жизни, вы пропали в бездне этого замка...')
        exit()
j = input()
j = j.lower()
if j == 'имя':
    num -= 1
    print('верно! проходите дальше вам осталось', num, 'комнаты до выхода из замка')
    print('переход в новую комнату...')
    c.use()
else:
    print('неверный ответ(, подумайте еще')
    n = input()
    n = n.lower()
    if n == 'имя':
        num -= 1
        print('верно! проходите дальше вам осталось', num, 'комнаты до выхода из замка')
        print('переход в новую комнату...')
        c.use()
    else:
        print('эта ошибка была ФАТАЛЬНОЙ в вашей жизни, вы пропали в бездне этого замка...')
        exit()
k = input()
k = k.lower()
if k == 'сухих':
    num -= 1
    print('верно! проходите дальше вам осталось', num, 'комнаты до выхода из замка')
    print('переход в новую комнату...')
    d.use()
else:
    print('неверный ответ(, подумайте еще')
    p = input()
    p = p.lower()
    if p == 'сухих':
        num -= 1
        print('верно! проходите дальше вам осталось', num, 'комнаты до выхода из замка')
        print('переход в новую комнату...')
        d.use()
    else:
        print('эта ошибка была ФАТАЛЬНОЙ в вашей жизни, вы пропали в бездне этого замка...')
        exit()
l = input()
l = l.lower()
if l == 'в стакане':
    num -= 1
    print('верно! проходите дальше вам осталось', num, 'комната до выхода из замка')
    print('переход в новую комнату...')
    e.use()    
else:
    print('неверный ответ(, подумайте еще')
    u = input()
    u = u.lower()
    if u == 'в стакане':
        num -= 1
        print('верно! проходите дальше вам осталось', num, 'комната до выхода из замка')
        print('переход в новую комнату...')
        e.use()
    else:
        print('эта ошибка была ФАТАЛЬНОЙ в вашей жизни, вы пропали в бездне этого замка...')
        exit()
z = input()
z = z.lower()
if z == 'сон':
    print('верно! вы ответили на все загадки и можете покинуть это странное место.')
else:
    print('неверный ответ(, подумайте еще')
    t = input()
    t = t.lower()
    if t == 'сон':
        print('верно! вы ответили на все загадки и можете покинуть это странное место!!!')
    else:
        print('эта ошибка была ФАТАЛЬНОЙ в вашей жизни, вы пропали в бездне этого замка...')
        exit()
input()
    
