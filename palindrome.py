import re


def main():
    user_input= input("give me some words to see if they are palindrome  ")

    if is_palindrome(user_input) == True:
        print("It is one")
    if is_palindrome(user_input) == False:
        print("it's not one")
#if True: #    print("it is one")
#if False: #    print("it is not one")

def is_palindrome(user_input):

    mod_input= re.sub(r'[^A-Za-z]', "", user_input).lower()
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
