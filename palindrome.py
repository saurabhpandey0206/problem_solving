#check string is palindrome or not
def palin(string):
    str1 = string[::-1]
    if str1 == string:
        print("string is palindrome")
    else:
        print("sring isn't palindrome")


a = input(" enter a string::")
palin(a)
