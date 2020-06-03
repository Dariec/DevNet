#!/usr/bin/env python3

import yaml


config = yaml.load(open('test.yaml'))



ip = '255.255.252.248'
bin_octets = []
vlans = [1, 3, 10, 25, 255, 666]

octets = ip.split('.')


r1 = {
'IOS': '15.4',
'IP': '10.10.10.1',
'hostname': 'london_r1',
'location': '21 New Globe Walk',
'model': '4451',
'vendor': 'Cisco'}

fast_int_vlan = {'0/1': 15, '0/3': 255, '0/5': 777}
commands = ['switchport mode access', 'switchport access vlan', 'spanning-tree portfast', 'spanning-tree bpduguard enable']


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

'''
# Сгенерировать две строки с VLAN из списка VLANS
for vlan in vlans:
	print('vlan {}'.format(vlan))
	print(' name VLAN_{:04}'.format(vlan))
'''

'''
# Перебираем все значения с ключами в словаре
for key, value in r1.items():
	print(key, value)
'''

'''
# Перебираем в цикле интерфейсы и команды для каждого интерфейса с учетом ключей(VLAN)
for intf in fast_int_vlan:
	print('interface Fa{}'.format(intf))
	for command in commands:
		if 'vlan' in command:
			print(command, fast_int_vlan[intf])
		else:
			print(command)
'''


print(config[1])



