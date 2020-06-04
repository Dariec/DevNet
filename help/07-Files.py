# coding : utf-8

'''
with open('r1.txt') as config:	# Открыли файл для чтения
	for line in config:
		print(line.rstrip())
'''

with open('r1.txt') as config:	# Открыли файл для чтения
	for line in config:		# Переборали все линии в congif
		if line.startswith('service'):	# Вывести все строки начинающиеся с service
			print(line.rstrip())



'''
f = open('new_file.txt', 'w')	# Открыли файл на запись
'''
'''	# Посчитать количество "\n"
content = f.read()
print(content.count('\n'))
'''

'''	# Записываем в файл + \n
f.write('test1\n')
f.write('test2\n')
f.write('test4\n')
f.write('test7\n')
'''







