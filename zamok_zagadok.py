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

a = Vopros1("��� ���� ������ ������� �� ������?")
b = Vopros2("��� ����������� ���, �� ������ ���������� ��� ����?")
c = Vopros3("����� ������ ��� �� � ����� ����?")
d = Vopros4("��� ���� ����� �������?")
e = Vopros5("��� ����� ������ � ��������� �������?")
num = 5
print('�� ������ � ����� �������, ����� ��������� ��� ����� �������� �� ��� ������� ��������� (�� ������ ������ ������ ���� 2 �������!!!)')
a.use()
h = input()
h = h.lower()
if h == '��������':
    num -= 1
    print('�����! ��������� ������ ��� ��������', num, '������� �� ������ �� �����')
    print('������� � ����� �������...')
    b.use()
else:
    print('�������� �����(, ��������� ���')
    m = input()
    m = m.lower()
    if m == '��������':
        num -= 1
        print('�����! ��������� ������ ��� ��������', num, '������� �� ������ �� �����')
        print('������� � ����� �������...')
        b.use()
    else:
        print('��� ������ ���� ��������� � ����� �����, �� ������� � ������ ����� �����...')
        exit()
j = input()
j = j.lower()
if j == '���':
    num -= 1
    print('�����! ��������� ������ ��� ��������', num, '������� �� ������ �� �����')
    print('������� � ����� �������...')
    c.use()
else:
    print('�������� �����(, ��������� ���')
    n = input()
    n = n.lower()
    if n == '���':
        num -= 1
        print('�����! ��������� ������ ��� ��������', num, '������� �� ������ �� �����')
        print('������� � ����� �������...')
        c.use()
    else:
        print('��� ������ ���� ��������� � ����� �����, �� ������� � ������ ����� �����...')
        exit()
k = input()
k = k.lower()
if k == '�����':
    num -= 1
    print('�����! ��������� ������ ��� ��������', num, '������� �� ������ �� �����')
    print('������� � ����� �������...')
    d.use()
else:
    print('�������� �����(, ��������� ���')
    p = input()
    p = p.lower()
    if p == '�����':
        num -= 1
        print('�����! ��������� ������ ��� ��������', num, '������� �� ������ �� �����')
        print('������� � ����� �������...')
        d.use()
    else:
        print('��� ������ ���� ��������� � ����� �����, �� ������� � ������ ����� �����...')
        exit()
l = input()
l = l.lower()
if l == '� �������':
    num -= 1
    print('�����! ��������� ������ ��� ��������', num, '������� �� ������ �� �����')
    print('������� � ����� �������...')
    e.use()    
else:
    print('�������� �����(, ��������� ���')
    u = input()
    u = u.lower()
    if u == '� �������':
        num -= 1
        print('�����! ��������� ������ ��� ��������', num, '������� �� ������ �� �����')
        print('������� � ����� �������...')
        e.use()
    else:
        print('��� ������ ���� ��������� � ����� �����, �� ������� � ������ ����� �����...')
        exit()
z = input()
z = z.lower()
if z == '���':
    print('�����! �� �������� �� ��� ������� � ������ �������� ��� �������� �����.')
else:
    print('�������� �����(, ��������� ���')
    t = input()
    t = t.lower()
    if t == '���':
        print('�����! �� �������� �� ��� ������� � ������ �������� ��� �������� �����!!!')
    else:
        print('��� ������ ���� ��������� � ����� �����, �� ������� � ������ ����� �����...')
        exit()
input()
    
