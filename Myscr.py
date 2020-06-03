#!/usr/bin/env python3

from sys import argv

interface = input('Введите тип и номер интерфейса: ')
vlan = input('Введите номер VLAN: ')


access_template = [
'switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']


print('\n' + '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))

