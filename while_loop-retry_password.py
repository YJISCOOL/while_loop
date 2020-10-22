chance = 3

while chance > 0:
	input_password = input('enter ur password: ')
	chance -= 1
	if input_password == 'a123456':
		print ('登入成功！')
		break
	else:
		if chance > 0:
			print ('密碼錯誤！還有'+ str(chance) +'次機會。')
		else:
			print ('你忘記就去按忘記密碼啊，很難嗎')
	
	