text=input("Put your text here:  ")
alpha= list("abcdefghijklmnopqrstuvwxyz")
alphadict=dict([(alpha[alpha.index(x)],alpha.index(x)) for x in alpha])
def rot13(text):
    global alphadict
    global alpha
    rot=int(input("Enter teh rotation number: "))
    cipher=[]
    for i in text:
        if i.lower() not in alpha:
            cipher.append(i)
        else:
            k=alphadict[i.lower()]+rot
            if k > 25:
                k=k%26
                cipher.append(alpha[k])
            elif k < 0:
                k=26-abs(k)
                cipher.append(alpha[k])
            else: cipher.append(alpha[k])
    return ''.join(cipher)
print(rot13(text))
