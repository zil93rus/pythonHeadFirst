def count_syllables_in_word(word):
    count = 0

    endings = '.,;!?:'
    last_char = word[-1]

    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1

    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]

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


def count_syllables(words):
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count += word_count
    return count


def count_sentences(text):
    count = 0
    terminals = '.?!'
    for i in text:
        if i in terminals:
            count += 1
    return count


def output_results(score):
    if score >= 90:
        print("Уровень 5-го класса")
    elif score >= 80:
        print("Уровень 6-го класса")
    elif score >= 70:
        print("Уровень 7-го класса")
    elif score >= 60:
        print("Уровень 8-9-го класса")
    elif score >= 50:
        print("Уровень 10-11-го класса")
    elif score >= 30:
        print("Уровень студента ВУЗА")
    else:
        print('Уровень выпусника ВУЗА')


def compute_readability(text):

    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)
    score = 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)
    print(f'{total_words} - слов. {total_sentences} - предложений. {total_syllables} - слогов. {int(score)} - рейтинг')
    output_results(score)

if __name__ == '__main__':
    import ch1text
    print('Текст главы 1: ')
    compute_readability(ch1text.text)