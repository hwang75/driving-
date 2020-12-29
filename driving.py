region = input ('请问你来自哪个国家')
age = input('请输入你的年龄')
age = int(age)
if region == '台湾':
	if age > 18:
		print('你可以考驾照')
	else:
		print('你还不可以')
elif region == '美国':
	if age >= 16:
		print('你可以考驾照')
	else:
		print('不可以')
