import random

choice = random.randint(0, 2)
user_choice = ''
if choice == 0:
    random_choice = "камень"
elif choice == 1:
    random_choice = "ножницы"
else:
    random_choice = "бумага"
while user_choice != 'камень' and user_choice != 'ножницы' and user_choice != 'бумага':
    user_choice = input('камень, ножницы, бумага: ')
if random_choice == user_choice:
    print(f"Компьютер - {random_choice} Вы - {user_choice} - НИЧЬЯ")
elif random_choice == "камень" and user_choice == "ножницы":
    print(f"Компьютер - {random_choice} Вы - {user_choice} - Вы проиграли")
elif random_choice == "ножницы" and user_choice == "бумага":
    print(f"Компьютер - {random_choice} Вы - {user_choice} - Вы проиграли")
elif random_choice == "бумага" and user_choice == "камень":
    print(f"Компьютер - {random_choice} Вы - {user_choice} - Вы проиграли")
else:
    print(f"Компьютер - {random_choice} Вы - {user_choice} - Вы победили")

user_choice = ''
ls = ["камень", "ножницы", "бумага"]
while user_choice != 'Q':
    pc_choice = random.choice(ls)
    user_choice = int(input('1 - камень, 2 - ножницы, 3 - бумага, Q - выход: '))
    if pc_choice == ls[user_choice -1]:
        print(f"Компьютер - {pc_choice} Вы - {ls[user_choice -1]} - НИЧЬЯ")
    elif pc_choice == "камень" and ls[user_choice - 1] == "ножницы":
        print(f"Компьютер - {pc_choice} Вы - {ls[user_choice -1]} - Вы проиграли")
    elif pc_choice == "ножницы" and ls[user_choice -1] == "бумага":
        print(f"Компьютер - {pc_choice} Вы - {ls[user_choice -1]} - Вы проиграли")
    elif pc_choice == "бумага" and ls[user_choice -1] == "камень":
        print(f"Компьютер - {pc_choice} Вы - {ls[user_choice -1]} - Вы проиграли")
    else:
        print(f"Компьютер - {pc_choice} Вы - {ls[user_choice -1]} - Вы победили")

characters = ['t', 'a', 'c', 'o']

output = ''
length = len(characters)
i = 0
while i < length:
    output = output + characters[i]
    i += 1

length = length * -1
i = - 2

while i >= length:
    output = output + characters[i]
    i = i - 1
print(output)

smoothies = ['кокосовый', 'клубничный', 'банавый', 'тропичесикй', 'ягодный']
lenght = len(smoothies)
for i in range(lenght):
    print(f'Мы подаем {i + 1} {smoothies[i]}')


def get_attribute(query, default):
    question = f'{query}? По умолчанию - {default}:'
    answer = input(question)
    if answer == '':
        answer = default
    print(f'Вы набрали {answer}')
    return answer


hair = get_attribute('Цвет волос', 'темные')
hair_length = get_attribute('Длина волос', 'короткие')
eye = get_attribute('Цвет глаз', 'голубые')
gender = get_attribute('Пол', 'женский')
glasses = get_attribute('Носит очки', 'нет')
beard = get_attribute('Носит бороду', 'нет')

def drink_me(param):
    msg = f'Выпиваем {param} стакан'
    print(msg)
    param = "пустой"

glass = 'полный'
drink_me(glass)
print('Стакан', glass)

# def sort_list(ls1, ls2):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(ls1)-1):
#             if ls1[i] < ls1[i+1]:
#                 tmp = ls1[i]
#                 ls1[i] = ls1[i+1]
#                 ls1[i+1] = tmp
#                 tmp = ls2[i]
#                 ls2[i] = ls2[i+1]
#                 ls2[i+1] = tmp
#                 swapped = True
#
# list1 = [7, 2, 6, 8, 1, 6, 7, 3, 4]
# list2 = list(range(1, len(list1) +1))
# sort_list(list1, list2)
# print(list1)
# print(list2)
# for i in range(len(list1)-1):
#     print(f'Рейтинг - {list1[i]}. Раствор №{list2[i]}')
