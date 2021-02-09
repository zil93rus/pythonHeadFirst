my_dictionary = {}

my_dictionary['new key1'] = 'test1'
my_dictionary['new key2'] = 'test2'
my_dictionary['new key3'] = 'test3'
my_dictionary['new key4'] = 'test4'
my_dictionary['new key5'] = [1, 2, 3]

terminals = '123'

for key in list(my_dictionary):
    summa = 0
    if key == 'new key5':
        for i in my_dictionary[key]:
            summa += i

print(summa)