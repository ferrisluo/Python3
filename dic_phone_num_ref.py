
# contact number searching app

contact = {}
i = 1
name = ''
while (name != '-1'):
	name = input('please enter the %d name(enter -1 to exit):' %(i))
	if (name == '-1'):
		break
	phone = input('Please enter the %d phone number:' %(i))
	contact[name]=phone    # use name as key and phone as value in the contact dic.
	i += 1

search = input('please enter the name you want to search:')
print(contact.get(search,'the name is not in the records'))








