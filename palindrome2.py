import re


def main():
    user_input= input("give me some words to see if they are palindrome  ")

    if is_palindrome(user_input) == True:
        print("It is one")
    else:
        print("it's not one")
#if True: #    print("it is one")
#if False: #    print("it is not one")

def is_palindrome(user_input):

    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # include characters in input that are also in alphabet_list
    mod_input = []
    for letter in user_input.lower():
        if letter in alphabet_list:
            mod_input.append(letter)


# if len(sentence) = 0 or = 1 then it's TRUE a palindrome (length <= to 1)
    if len(mod_input) <= 1:
        return True

    #now i need to deal with phrases longer than 1 letter in length
    elif mod_input[0] == mod_input[-1]: #compare 1st character and last character and if equal procede

        return is_palindrome(mod_input[1:-1]) # run the function again using previous answer but slice the sentence
    else:
        return False


if __name__ == '__main__':
   main()
