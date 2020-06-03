#!/usr/bin/env python3

ip = '255.255.252.248'
bin_octets = []
vlans = [1, 3, 10, 25, 255, 666]

octets = ip.split('.')



'''
	# Перебрать и перевести октеты в бинарный формат
bin_octets.append('{:08b}'.format(int(octets[0])))
bin_octets.append('{:08b}'.format(int(octets[1])))
bin_octets.append('{:08b}'.format(int(octets[2])))
bin_octets.append('{:08b}'.format(int(octets[3])))
'''

'''
for idx in [0,1,2,3]:
	bin_oct = '{:08b}'.format(int(octets[idx]))
	bin_octets.append(bin_oct)
'''

'''
for octet in octets:
	bin_octets.append('{:08b}'.format(int(octet)))
print(bin_octets)
'''

'''
	# Перебрать интерфейсы с 0 до 9
for num in range(9):
	print('interface Gi0/{}'.format(num))
'''


	# Сгенерировать две строки с VLAN из списка VLANS
for vlan in vlans:
	print('vlan {}'.format(vlan))
	print(' name VLAN_{:04}'.format(vlan))





