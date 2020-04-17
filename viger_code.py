abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


input_txt = 'Attack at dawn'
code_word = 'Lemon'
output_txt = []


input_txt = input_txt.lower()
input_txt = input_txt.replace(' ','')
code_input = []

code_word = code_word.lower()

res = []

for j in input_txt:
 	y = abc.index(j)
 	code_input.append(y)

for i in code_word:
	x = abc.index(i)
	abc_head = abc[x::]
	abc_tail = abc[:x:]
	abc_new = [abc_head + abc_tail]
	abc_new = [i for i in abc_new for i in i]
	print(code_input)
	print(abc_new)
	for i in code_input:
		s = abc_new[i]
		print(s)
		res.append(s)
		print(res)
		code_input.remove(i)
		print(code_input)
		break

# print(output_txt)

"""LXFOPVEFRNHR"""