import json
import string

f = open('words.json')

words = json.load(f)
lettersNotIn = []
lettersIn = []
known_to_be_right = [None, None, None, None, None]
known_to_be_wrong = [[], [], [], [], []]
possible = []


def check_positions(word):
    count_ktbr = 0
    count_ktbw = 0
    for x in range(5):
        if known_to_be_right[x] is None or word[x] == known_to_be_right[x]:
            count_ktbr += 1
        if not any(letter == word[x] for letter in known_to_be_wrong[x]):
            count_ktbw += 1

    return count_ktbr == 5 == count_ktbw


def check_word(word):
    if all(letter in word for letter in lettersIn) and not any(letter in word for letter in lettersNotIn):
        if check_positions(word):
            possible.append(word)


def main():
    possible.clear()
    for let in string.ascii_uppercase:
        for i in words[let]:
            check_word(i)
    print(possible)




if __name__ == "__main__":
    main()

# run()
# print(possible)
# print(len(possible))

f.close()
