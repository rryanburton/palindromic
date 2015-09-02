def is_palindrome(sentence): # TODO: return True or False if the sentence is or isn't a palindrome
    #if len(sentence) = 0 or = 1 then it's TRUE a palindrome (length <= to 1)
    if len(sentence) <= 1:
        return TRUE
    
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
user_input= "test $sentence with punctuation, !$"


# include characters in input that are also in alphabet_list, but exclude everything not in alphabet_list
sentence = []
for letter in user_input.lower():
    if letter in alphabet_list:
        sentence.append(letter)
#reversed_list = user_letters[::-1]




def main():
    user_input = input("give me some words to see if they are palindrome") # TODO: put your input/output code here



if __name__ == '__main__':
    main()
