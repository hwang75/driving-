password = ('a123456')
x = 0
while x < 3:
	enter = input('请输入您的密码：')
	if enter == password:
		print('success')
		break
	else:
		x = x + 1
		print('password wrong, you have', 3 - x,'chance')
