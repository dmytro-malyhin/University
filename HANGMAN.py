print('You star to play')
word = list(str(input('Please, input the word for second player - ')))
massive_light = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
Attempt = 5
letter = []

while True:
    for element in word:
        if element in massive_light:
            letter.append(element)
        elif element not in massive_light:
            letter.append('_')
    print(letter)
    break
print()

while Attempt > 0:
    word_vvod = str((input('Please input the letter in the word - ')))

    if word_vvod not in word:
        Attempt = Attempt - 1
        print('This letter is not in the hidden word ')
        print('Your attempts: ', Attempt)
        if Attempt < 5:
            print('\n  |  ')
        if Attempt < 4:
            print('  O  ')
        if Attempt < 3:
            print(' /|\ ')
        if Attempt < 2:
            print('  |  ')
        if Attempt < 1:
            print(' / \ ')
        if Attempt == 0:
            print('Game over')
    elif word_vvod in word:
        letter.pop(int(word.index(word_vvod)))
        letter.insert(int(word.index(word_vvod)), word_vvod)
        print(letter)
        if letter == word:
            print('You win')
