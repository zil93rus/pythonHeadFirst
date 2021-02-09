import ch1text

def syllables_in_word(word):
    count = 0
    processed_word = ''
    last_char = word[-1]
    ending = '.,;!?:'
    if last_char in ending:
        processed_word = word[:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1

    if processed_word[-1] in 'eE':
        processed_word = processed_word[:-1]


    vowels = 'aeiouAEIOU'
    prev_char = False
    for i in processed_word:
        if i in vowels:
            if not prev_char:
                count += 1
            prev_char = True
        else:
            prev_char = False

    if processed_word[-1] in 'yY':
        count += 1

    return count

def sentences(text):
    count = 0
    terminals = '.?!'
    for i in text:
        if i in terminals:
            count += 1
    return count

def scan_text(text):
    words = text.split()
    total_words = len(words)
    total_sentences = sentences(text)
    total_syllables = syllables(words)

    return print(f'Всего слов - {total_words}. Всего предложений - {total_sentences}. Всего слогов - {total_syllables}')

def syllables(word):
    count = 0
    for i in word:
        total = syllables_in_word(i)
        count += total
    return count

my_text = ch1text.text2
scan_text(my_text)
# word = test2.text



# vowels = 'aeiouAEIOU'
# count = 0
# two_vowels = False
# for i in word:
#     if not two_vowels:
#         if i in vowels:
#             count += 1
#         two_vowels = True
#     else:
#         two_vowels = False
#
# print(count)
