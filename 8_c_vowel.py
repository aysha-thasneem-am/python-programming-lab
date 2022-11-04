word=input("enter a word:")
word=word.lower()
vowel_list=[]
for i in word:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vowel_list.append(i)
print(vowel_list)
        
