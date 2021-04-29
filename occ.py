def frqnc(string):
    num = {}
    temp = 0
    k=''
    
    for i in string:
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    for i in num:
        if num[i]>temp:
            temp = num[i]
            k = i
            
    print('character:'+k,temp)
    
            
        












frqnc("aabcdadaacchdjhlslkljdkhdnaaaa")
