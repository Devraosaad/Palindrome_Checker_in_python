def is_palindrome(r):
    # Remove spaces and convert to lowercase
    r = r.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return r == r[::-1]


word = input("enter the word :")
sum= is_palindrome(r)
print(sum )
#for i in word :
 #print(i[:: -1])
 #print(i[-1 ::])


