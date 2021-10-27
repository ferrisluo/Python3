



import random

num = random.randint(1, 1000)
count = 0

while True:
	guess = input('請猜一個數字(1~1000):')
	guess = int(guess)
	if (guess == num):
		count += 1
		print('你答對了！')
		print('你一共猜了%d次' %(count))
		break
	elif (guess > num):
		count += 1
		print('比答案大')
		print('這是你猜的第%d次' %(count))
	elif (guess < num):
		count += 1
		print('比答案小')
		print('這是你猜的第%d次' %(count))



