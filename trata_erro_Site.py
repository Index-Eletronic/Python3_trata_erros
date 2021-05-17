'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except urllib.error.URLError:
    print('O Site Pudim não está acessivel no momento')
else:
    print('Tudo OK.')
    print(site.read())