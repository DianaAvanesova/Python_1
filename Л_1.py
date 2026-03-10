import os
import re

filename = '1.txt'
word_to_find = input('Введите слово для поиска: '.lower()) #нижний регистр

if not os.path.exists(filename):
    print(f"Файл '{filename}' не найден.")
else:
    with open(filename, encoding='utf-8') as file:
        text = file.read().strip()
        
    # Удаляет знаки препинания и цифры
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    words_list = cleaned_text.split()
    
    # Количество вхождений заданного слова
    count = 0
    for word in words_list:
        if word == word_to_find:
            count += 1
            
    print(f"Слово '{word_to_find}' найдено {count} раз.")