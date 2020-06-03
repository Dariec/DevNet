# coding : utf-8


d = {1: 100, 2: 200, 3: 300}
'''
username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')


while True:
	if len(password) < 8:
		print('Пароль слишком короткий')
	elif username.lower() in password.lower():
		print("Пароль содержит имя пользователя")
	elif not '@' in password:
		print('В пароле должна быть собака @')
	else:
		print('Пароль для пользователя {} установлен'.format(username))
		break
		#continue Тоже самое что и break
	password = input('Введите пароль еще раз: ')
'''



try:
	print(d[5])
except KeyError:
	print('Такого ключа неееееееееет!!!!!!!!')

