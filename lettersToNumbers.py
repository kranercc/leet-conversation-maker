numbers = {
	"a": 4,
	"b": 6,
	"e": 3,
	"o": 0,
	"s": 5,
	"t": 7,
	"i": 1
	}

user = input("> ")
print('\n\n\n\n')
for i in user:
	if i in numbers:
		print(numbers[i],end='')
	else:
		print(i.upper(),end='')
print("\n\n")
