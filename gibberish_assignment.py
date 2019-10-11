# Gibberish Assignment
# Author Jack Kelly, c18500896
# Date: 09/10/19

game = 1
while game == 1:
    # Prompting for and taking in the first syllable
    print("Enter your first Gibberish syllable (add * for the vowel substitute)\n ")
    syll_str1 = input("Syllable must only contain letters or a wildcard ('*')\n")

    # Prompting for and taking in the second syllable
    print("Enter your second Gibberish syllable (add * for the vowel substitute)\n ")
    syll_str2 = input("Syllable must only contain letters or a wildcard ('*')\n")

    # Prompting for and taking in the word to be translated
    word_str = input("Enter the word you wish to translate!")

    vowels = 'aeiouAEIOU'
    new_word = ''
    switch = 0

    for i in word_str:
        # The switch variable will change once the first syllable has been used
        if switch == 0:
            # Adding the first syllable to the first vowel
            if i in vowels:
                # Changing the wildcard to a vowel
                if '*' in syll_str1:
                    syll_str1 = i + syll_str1[1::]

                new_word = new_word + syll_str1 + i
                switch = 1
            else:
                new_word = new_word + i
        else:
            # Adding the second syllable to the remaining vowels as long as the don't come directly after another vowel
            if i in vowels:
                # Changing the wildcard to a vowel
                if '*' in syll_str2:
                    syll_str2 = i + syll_str2[1::]

                new_word = new_word + syll_str2 + i
            else:
                new_word = new_word + i

    # Prints there translated word
    print("Your translated word is", new_word)

    # Asks whether or not they would like to end the game
    end = input("Would you like to end the game? (y/n)")
    if end == 'y':
        game = 0