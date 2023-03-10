#source code nomor 1

print('Numbers from 1 to 100:')
for n in range(1, 101):
    print(n, end=' ')

#source code nomor 2

for i in range(1, 101):
    if i % 2 == 0:
        continue
    else:
        print(i)