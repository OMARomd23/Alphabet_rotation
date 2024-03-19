text=input("Put your text here:  ")
print(f'old: {text}')

alpha= list("abcdefghijklmnopqrstuvwxyz")

alphadict=dict([(alpha[alpha.index(x)],alpha.index(x)) for x in alpha])

def rot13(text):

    global alphadict

    global alpha

    rot=int(input("Enter the rotation number: "))

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

                if abs(k) > 25:

                    j=(abs(k)%26)-1

                    if j < 0:k=(25+abs(j))%26

                    else:k=25-j

                else:k=25+k

                cipher.append(alpha[k])

            else: cipher.append(alpha[k])

    return ''.join(cipher)

print(f'new: {rot13(text)}')

