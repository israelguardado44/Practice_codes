##practice problem 1

## input : takes a sentence (string) and returns the letters in each word in a sorted order.

def sorted_strings(sentence):
	sentence = sentence.lower()
	lst = sentence.split()
	copy = []
	for i in lst:
		x = sorted(i)
		x = ''.join(x)
		copy.append(x)	
	return ' '.join(copy)



print sorted_strings("This challenge doesn't seem so difficult")

