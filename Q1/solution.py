n = input()
n_str = input().split(' ')
m = input()
m_request = input().split(' ')

strings = [x for x in n_str]
requests = [x for x in m_request]
output = ""

con1 = False
con2 = False
con3 = False
con4 = False

if (int(n) >= 1) and (int(n) <= 1000):
    con1 = True

for string in strings:
    if string.count('X') > 1000 or string.count('L') > 1000:
        con2 = False
        break
    else:
        con2 = True

if (int(m) > 0) and (int(n) >= int(m)):
    con3 = True
else:
    con3 = False

if len(requests) == int(m):
    con4 = True

if (con1 and con2 and con3 and con4) == True:
    print('Yes')
else:
    print('No')


