country = input('please enter your nationality:')
age = input('please enter your age:')
age = int(age)
if country == 'taiwan':
	if age >= 18:
		print('you can get a licence')
	else:
		print('you cannot get a licence')