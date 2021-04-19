import hashlib

word_list = []
hash_word = []
word_list2 = open('test.txt').read().split()
for item in word_list2:
	result = hashlib.md5(item.encode())
	hash_word.append(result.hexdigest())
	word_list.append(item)

chars = set('.?')

sentence_list = []
hash_sentence = []
s = ""
for i in word_list:
	if any((c in chars) for c in i):
		s+=i
		sentence_list.append(s)
		result_sentence = hashlib.md5(s.encode())
		hash_sentence.append(result_sentence.hexdigest())
		s = ""
		continue
	s+=i


with open("test.txt", "r") as f:
    input_ = f.read().split("\n") 

para = []

for i in range(len(input_)):
    w = ""
    for j in input_[i]:
        w += j
    para.append(w)

combine_para = []
for i in para:
    i = i.replace("\\", "") 
    v = ""
    for j in i:
        if (j == ' '):
            continue;
        v += j
    combine_para.append(v);

hash_para = []
for i in combine_para:
	result = (hashlib.md5(i.encode())).hexdigest()
	hash_para.append(result)


TT = int(input("Enter the number for the service you want to utilize \n 1 - To find first occurrence of a word \n 2 - To find all the occurrences of a word \n 3 - To find the occurence of a line \n 4 - To find the occurence of a paragraph\n ====> "))

if (TT == 1):
## --------> This is for first occurence of the word <--------
	InputWord = input("Enter word : ")
	InputWordHash = (hashlib.md5(InputWord.encode())).hexdigest()
	idx = 1
	found = False
	for rs in hash_word:
		if (InputWordHash == rs):
			print(" ===> {} was found at {} position.".format(InputWord, idx))
			found = True
			break;
		idx += 1
	if (not found):
		print(" ===> The paragraph doesn't have the entered string.")


elif (TT == 2):
## ===========> This is for multiple occurences of the word <==========
	InputWord = input("Enter word : ")
	InputWordHash = (hashlib.md5(InputWord.encode())).hexdigest()
	idx = 1
	found = False
	for rs in hash_word:
		if (InputWordHash == rs):
			print(" ===> {} was found at {} position.".format(InputWord, idx))
			found = True
		idx += 1
	if (not found):
		print(" ===> The paragraph doesn't have the entered string.")


elif (TT == 3):
## ----------> This is for sentence <-----------
	InputSentence = input("Enter the sentence you want to search : ")
	SentenceWords = InputSentence.split()
	x = ""
	for i in SentenceWords:
		x += i
	InputSentenceHash = (hashlib.md5(x.encode())).hexdigest()
	idx = 1
	found = False
	for rs in hash_sentence:
		if (InputSentenceHash == rs):
			print(" ===> The entered sentence is at {} position".format(idx))
			found = True
			break
		idx += 1
	if (not found):
		print(" ===> The entered sentence doesn't exist.")


elif (TT == 4):
## ----------> This is for Paragraph <-----------
	InputParagraph = input("Enter the paragraph you want to search : ")
	ParaWords = InputParagraph.split()
	g = ""
	for i in ParaWords:
		g += i;
	InputParaHash = (hashlib.md5(g.encode())).hexdigest()
	idx = 1;
	found = False
	for rs in hash_para:
		if (rs == InputParaHash):
			print(" ===> The entered paragraph is at {} position".format(idx))
			found = True
			break
		idx += 1
	if (not found):
		print(" ===> The entered sentence doesn't exist.")
