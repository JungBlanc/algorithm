a, b, c = 21, 3, 7

m = a*b*c
m_list = list(str(m))
print(m_list)
for i in range(10):
    count = m_list.count(str(i))
    print(count)
