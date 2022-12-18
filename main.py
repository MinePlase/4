message = input("Введите текст: ")
length = len(message)
print("Количество букв в слове:", length)
print("Вторая буква вашего слова:", message[1])
print("Последняя буква вашего слова:", message[-1])
print("Первые 3 буквы: ", message[0:3])
print("Последние 3 буквы: ", message[-3:])
print("Раскраска: \033[35m", message)
chiper_one = message.replace('и', 'о')
print("Шифр 1:", chiper_one)
chiper_two = message[::-1]
print("Шифр 2:", chiper_two)
chiper_three = message[::2] + message[1::2]
print("Шифр 3:", chiper_three)
chiper_four = message[-1] + message[1:-1] + message[0]
print("Шифр 4:", chiper_four)
half_length = len(message)//2
cipher_five = message[half_length:] + message[:half_length]
print("Шифр 5:", cipher_five)
decoder_one = chiper_one.replace('о', 'и')
print("Расшифровка 1: ", decoder_one)
decoder_two = chiper_two[::-1]
print("Вторая расшифровка:", decoder_two)
result = " "
if length % 2 == 0:
    half_one = chiper_three[0:half_length]
    half_two = chiper_three[half_length:]
else:
    half_one = chiper_three[0:half_length + 1]
    half_two = chiper_three[half_length + 1:]
for char in range(len(half_one)):
        result += half_one[char]
        if char < len(half_two):
            result += half_two[char]
print("Расшифровка 3:", result)
decoder_four = chiper_four[-1] + chiper_four[1:-1] + chiper_four[0]
print("Расшифровка 4: ", decoder_four)
decoder_five = cipher_five[:half_length] + cipher_five[half_length:]
print("Расшифровка 5:", decoder_five)
