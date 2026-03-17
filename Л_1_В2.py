filename = '1.txt'
word_to_find = input('Введите слово для поиска: ').lower()

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()
clean_text = ''.join(char for char in text if char.isalnum() or char.isspace()).lower()
words_list = clean_text.split()
count = words_list.count(word_to_find)

print(f"Слово '{word_to_find}' найдено {count} раз.")