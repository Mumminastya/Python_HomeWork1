# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

happy = input ('Введите номер билета: ')
i = 0
sum1 = 0
sum2 = 0
while i <=2:
    sum1 = sum1 + int(happy[i])
    i = i+1
while i <=5:
    sum2 = sum2 + int(happy[i])
    i = i+1
if(sum1 == sum2):
    print('Счастье есть!')
else:
    print('Не сегодня!')