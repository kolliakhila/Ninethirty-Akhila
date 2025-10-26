def freq_char(str):
    freq={}
    for i in str:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
str="akhilakolli"
print(freq_char(str))


s="mynameisakhilakolli"
freq={}
for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
for ch,count in freq.items():
    print(f"{ch}:{count}")