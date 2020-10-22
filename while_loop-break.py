x = 5
while x <= 10:
	print ('x還小於10唷！我還在迴圈')
	x += 1
print ('ㄇㄉ終於逃出來了')

y = 1
while y <= 10:
	print ('y還小於10唷！我還在迴圈')
	y += 1
	break #跳出迴圈
print ('一下子就逃出來了')


while True:
	mode = input('請輸入伺服器頻道： ')
	if mode == 'q':
		print ('遊戲離開。')
		break
	elif mode == '1':
		print ('進入伺服器1')
	elif mode == '2':
		print ('進入伺服器2')	
	elif mode == '3':
		print ('進入伺服器3')
	else:
		print ('只有伺服器123或q離開，再鬧就不要玩＼Ａ／')