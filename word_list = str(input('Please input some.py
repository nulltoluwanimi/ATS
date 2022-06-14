# word_list = str(
#     input('Please input some value to check if its palindrome or not: '))

# # if(len(word_list) > 5):
# #     print('Input can not be greater than 5, please input 5 characters only')

# word_index = 0

# for y in reversed(word_list):
#     # print(y, word_list[word_index], word_index)
#     if(y != word_list[word_index]):
#         print('Word is not palindrome')
#         break
#     word_index = word_index + 1

# def func(x: int) -> int:
#     print(x)


# func("c")

word_to_encrpyt = input('Enter a word to encrypt')

vowel_encrypt = {
    "a": "#",
    "e": "&",
    "i": "!",
    "o": "~",
    "u": "#"
}

check_char = 0
for i in word_to_encrpyt:
    if (i == vowel_encrypt[check_char]):
        word_to_encrpyt.replace(i, vowel_encrypt[check_char])
        check_char = + 1

print(vowel_encrypt)
