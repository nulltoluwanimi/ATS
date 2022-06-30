import random
import sys

global guess_word


# sys.getrecursionlimit(10000)

def guess(word, dash):
    global guess_word
    trails = 8
    count = 0
    for y in range(8):
        if count != 8:
            guess_letter = str(input('try guessing a letter: '))
            print(len(guess_letter))

            if len(guess_letter) > 1:
                print('Only one letter can be entered at a time')
                return guess(word, dash)
            else:
                if guess_letter in word:
                    indices = [i for i, c in enumerate(word) if c == guess_letter]
                    for i in indices:
                        dash[i] = guess_letter
                    if '_' not in dash:
                        print(f'Congratulations🌟🌟🌟, you won, the word is {word}, and you guess in {count} trails')
                        return
                    guess_word = dash
                    count += 1
                    str1 = ''.join(str(e) for e in dash)
                    print(str1, f'you have {trails - count} trails remaining')
                if guess_letter not in word:
                    count += 1
                    print()
                    print(f'you guessed wrong! 🥲🥲, you have {trails - count} trails left')
        if count == 8:
            str1 = ''.join(str(e) for e in guess_word)
            print(
                f'you failed to complete word in 8 trails, the word is {word} and you filled {str1} in {count} trails ')
            sys.exit()


def main():
    word_list = []
    with open('words.txt', 'r') as words:
        word_list = [line.strip() for line in words]
    choose_word = random.choice(word_list)
    dash_words = []
    for i in range(len(choose_word)):
        dash_words.append('_')
    print(choose_word)
    print(f'the hangman word has {len(dash_words)} letters {"".join(dash_words)}')
    guess(choose_word.lower(), dash_words)


if __name__ == '__main__':
    main()
