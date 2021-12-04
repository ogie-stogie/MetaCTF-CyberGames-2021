if __name__ == "__main__":
    with open("Word_Lists/2_letter_words.csv", "r") as f:
        two_letter_words = [line.strip().lower() for line in f.readlines()]
    with open("Word_Lists/3_letter_words.csv", "r") as f:
        three_letter_words = [line.strip().lower() for line in f.readlines()]
    with open("Word_Lists/5_letter_words.csv", "r") as f:
        five_letter_words = [line.strip().lower() for line in f.readlines()]
    with open("Word_Lists/7_letter_words.csv", "r") as f:
        seven_letter_words = [line.strip().lower() for line in f.readlines()]
    print(list(two_letter_words))
    input = "yzhsufo_rh_nb_uze_wdziu"
    print(len(set(input)))
    # remove line 14 and you will see all possible 7 letter words
    seven_letter_words = ["bashful"]
    seven_letter_words_passed = []
    searchspace = []
    for seven_letter_word in seven_letter_words:
        if len(set(seven_letter_word)) == 7:
            for first_two_letter_word in two_letter_words:
                if (seven_letter_word[2] == first_two_letter_word[1]) and (len(set(seven_letter_word + first_two_letter_word)) == 8):
                    for second_two_letter_word in two_letter_words:
                        if (len(set(seven_letter_word + first_two_letter_word + second_two_letter_word)) == 10):
                            for three_letter_word in three_letter_words:
                                if (len(set(three_letter_word)) == 3) and (three_letter_word[0] == seven_letter_word[4]) and (three_letter_word[1] == seven_letter_word[1]) and (len(set(seven_letter_word + first_two_letter_word + second_two_letter_word + three_letter_word)) == 11):
                                    for five_letter_word in five_letter_words:
                                        if (len(set(five_letter_word)) == 5) and (five_letter_word[2] == seven_letter_word[1]) and (five_letter_word[4] == seven_letter_word[4]) and (len(set(seven_letter_word + first_two_letter_word + second_two_letter_word + three_letter_word + five_letter_word)) == 14):
                                            print(f"{seven_letter_word}_{first_two_letter_word}_{second_two_letter_word}_{three_letter_word}_{five_letter_word}")
                                            searchspace += [f"{seven_letter_word}_{first_two_letter_word}_{second_two_letter_word}_{three_letter_word}_{five_letter_word}"]
                                            seven_letter_words_passed += [seven_letter_word]
    seven_letter_words_passed = list(set(seven_letter_words_passed))
    print(len(searchspace))
    print(seven_letter_words_passed)