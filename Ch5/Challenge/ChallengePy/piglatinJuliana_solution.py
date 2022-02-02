import enum


def topiglatin(sentence):
    vowels = "AEIOUaeiou"
    plwords = []
    curwords = sentence.split()

    for word in curwords:
        # If the word start with a vowel, add "way" to the end
        if vowels.__contains__(word[0]):
            plwords.append(word + "way")
        else:
            #Find position of the first vowel, then move the consonants
            #up to that point to the end of the word
            for i, c in enumerate(word):
                ind = vowels.find(c)
                if ind != -1:
                    pref = word[0:i]
                    suff = word[i:]
                    newword = suff + pref + "ay"
                    plwords.append(newword)
                    break

    return " ".join(plwords)

print("Enter a string to convert to PigLatin:")
inputstr = input()
piglatinstr = topiglatin(inputstr)
print("The result is: ", piglatinstr)
