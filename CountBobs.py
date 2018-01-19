word = str(raw_input())
count = 0
for i in range(len(word)-2):
	if word[i:i+3] == 'bob':
		count+=1
print("Number of times bob occurs is: " + str(count))
