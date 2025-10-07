s="abaa"
i=0
j=len(s)-1
while i<=j:
    if s[i]!=s[j]:
        s_l=s[i+1:j+1]
        s_r=s[i:j]
        if(s_l==s_l[::-1] or s_r==s_r[::-1]):
            print(True)
            break
        else:
            print(False)
            break
    i+=1
    j-=1
else:
    print(True)

