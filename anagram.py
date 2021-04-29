def anagram(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    if l1!=l2:
        print("these strings of two diffrent length")
    else:
        str1 = list(str1)
        str2 =list(str2)
        m = str1.sort()
        n = str2.sort()
        for i in range(len(str1)):
            if str1[i]==str2[i]:
                pass
                
            else:
                return False


a = anagram("loyal", "alloy")
if a == False:
    print("strings are not anagram")
else:
    print("strings are anagram")
            
        
