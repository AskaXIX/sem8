# w - перезапись
# r - чтение
# a - дозапись

file = open('new.txt', 'r', encoding = 'UTF-8')
# file.write('start123')
# file.close()

data = file.readlines()
file.close()

data = list(map(lambda x: x.strip(), data))
print(data)

data[1] = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
data = '\n'.join(data)

file = open('new.txt', 'w', encoding = 'UTF-8')
file.write('start123')
file.close()