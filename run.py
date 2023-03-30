from backup import Backup

a = 1
b = 'Test'
c = 3.14

b1 = Backup('create', a, name='Inteiro')
b3 = Backup('read', id=1)
print(b3.name)
b2 = Backup('update', b, id=1, name='String')
b3 = Backup('read', id=1)
print(b3.name)