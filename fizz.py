def fizz_buzz(x,y):
	fizz_list = x + y
	list1 = len(fizz_list)

	if list1 % 3 == 0:
		return "fizz"
	elif list1 % 5 ==0:
		return "buzz"
	elif list1 % 3 == 0 and list1 % 5 == 0:
		return "fizzbuzz"
	else:
		return fizz_list
print(fizz_buzz([1,2,3],[ ]))