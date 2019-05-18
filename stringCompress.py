#Implement a method to perform basic string compression using the counts of repeated characters. 
#For example, the string aabcccccaaa would become a2blc5a3.

def stringCompress(s):
    temp = s[0]
    count =0
    out =''
    index =0
    for i in s:
        index +=1
        if temp ==i:
            count +=1
        else:
            out +=temp+str(count)
            temp =i
            count =1
        
        if index == len(s):
            out +=temp+str(count)
    return out
    
def strCompress(s):
    count = 0
    out = ''
    for i in range(len(s)):
        count+=1
        if i+1>= len(s):
            out += s[i]+str(count)
            break
        if s[i] != s[i+1]:
            out += s[i]+str(count)
            count =0
    return out
print strCompress("aabcccccaaabb")
print stringCompress("aabcccccaaabb")
