'''num = 458189
expoente = 5
not_cient = "{:.8e}".format(num * 10**(-expoente))
print(not_cient)'''

a = 458189 * 10e-6
print('% .8e' % a)