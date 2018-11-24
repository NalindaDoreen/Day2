def vowel(letter):

    letters = 'aeiou'
    no_duplicates = set(letter)
    duplicates = len(letter)-len(no_duplicates)
    vowels = ""

    for i in letters:
        if i in no_duplicates:
            vowels += i

    return (vowels, duplicates)


    if __name__ == "__main__":
        print(vowel('doreennalinda'))