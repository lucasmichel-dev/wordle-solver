import random

from english_words import english_words_lower_alpha_set

five_letter_words = [word for word in english_words_lower_alpha_set if len(word) == 5]

current_word = random.choice(five_letter_words)
lettersIn = set()
lettersNotIn = set()
known_to_be_right = [None, None, None, None, None]
known_to_be_wrong = [set(), set(), set(), set(), set()]
wrong_words = []


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
    if word not in wrong_words \
            and all(letter in word for letter in lettersIn) \
            and not any(letter in word for letter in lettersNotIn):
        if check_positions(word):
            return word
    return None


def analyze_sets(correct, present, absent):
    process_correct(correct)
    process_present(present)
    process_absent(absent)


def process_correct(items):
    for item in items:
        letter_index = item.split(":")
        known_to_be_right[int(letter_index[1])] = letter_index[0]
        lettersIn.add(letter_index[0])


def process_present(items):
    for item in items:
        letter_index = item.split(":")
        known_to_be_wrong[int(letter_index[1])].add(letter_index[0])
        lettersIn.add(letter_index[0])


def process_absent(items):
    for item in items:
        if item not in lettersIn:
            lettersNotIn.add(item)


def check_done():
    return len(five_letter_words) <= 1


def remove_wrong_word(word):
    five_letter_words.remove(word)


def main(correct, present, absent):
    analyze_sets(correct, present, absent)
    filtered_list = []
    for word in five_letter_words:
        passed = check_word(word)
        if passed:
            filtered_list.append(passed)
    five_letter_words.clear()
    five_letter_words.extend(filtered_list)


def get_current_word():
    return random.choice(five_letter_words)


if __name__ == "__main__":
    main()
