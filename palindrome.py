def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    ##if len(sentence) = 0 or = 1 then it's TRUE a palindrome (length <= to 1)
    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    sentence = []
    for letter in user_input.lower():
        if letter in alphabet_list:
            sentence.append(letter)
    if len(sentence) <= 1:
        return True

    #now i need to deal with phrases longer than 1 letter in length
    elif (is_palindrome(sentence[1:-1]) and sentence[0] == sentence[-1]):
        return True

    else:
        return False





#reversed_list = user_letters[::-1]




def main():
    user_input = input("give me some words to see if they are palindrome  ")

    is_palindrome(user_input)
#if True:
#    print("it is one")
#if False:
#    print("it is not one")

if __name__ == '__main__':
   main()
