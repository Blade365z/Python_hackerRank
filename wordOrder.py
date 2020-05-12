from collections import OrderedDict
words = OrderedDict()
result = 0
for items in range(int(input())):
        word = input()
        words.setdefault(word,0)
        words[word] +=1
        
print(len(words))
print(*words.values()) 
