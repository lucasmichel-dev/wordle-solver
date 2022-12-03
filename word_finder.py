from english_words import english_words_lower_alpha_set

five_letter_words = [word for word in english_words_lower_alpha_set if len(word) == 5]

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
    last_possible = possible
    possible.clear()
    for word in (five_letter_words if not last_possible else last_possible):
        check_word(word)


if __name__ == "__main__":
    main()
