chance = 0

while chance <= 2:
	input_password = input('enter ur password: ')
	#print (input_password)
	if input_password == 'a123456':
		print ('登入成功！')
		break
	else:
		print ('密碼錯誤！還有'+ str(2-chance) +'次機會。')
	chance += 1