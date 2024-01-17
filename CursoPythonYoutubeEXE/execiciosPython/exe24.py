c  = str(input('Digite em qual cidade você nasceu : '))
c = c.strip()
c = c.lower()
c = c.split()
if c[0] == 'santo':
    print('Sua cidade começa com o nome santo!')
else:
    print('sua cidade não começa com o nome santo')
