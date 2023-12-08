from functions import salary,hello_who
# Тесты с помощью if
if salary != 20:
    print('Error')
if hello_who('Max') != 'Hello,Max':
    print('Failed')
else:
    print('Good')
if hello_who('Leo') != 'Hello,Leo':
    print('Failed')
else:
    print('Amazing')
