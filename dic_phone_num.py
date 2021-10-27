

"""
User can input names and their phone numbers.
Then they can look for the phone numbers by the name.
"""


dic_number = {}
n = 1


while True:
	name = input('Please enter the  %d name(enter -1 to exit):' %(n))

	if name == '-1':
		print(dic_number)
		break

	else:
		number = input('Please enter the %d phone number:' %(n))
		dic_number.setdefault(name,number)
		n += 1


search = input('Please enter the name:')

print(dic_number.get(search))















