# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'

print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аиеёоуыэюя'
counter = 0
for char in word.lower():
    if char in vowels:
        counter += 1
print(f"The word {word} contains {counter} vowels.")



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

w_count = len(sentence.split())
w_sum = len(''.join(sentence.split()))
print(w_sum / w_count)