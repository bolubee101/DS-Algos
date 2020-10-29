# check for palindromes

def palindrome(word):
    #using the start,stop,step we check if the string in reverse order is equal to
    #the original string
    if word[::] == word[-1::-1]:
        return 'Palindrome'
    else:
        return 'Not palindrome'
word = input('enter a palindrome: ')
print(palindrome(word))
