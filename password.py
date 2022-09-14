# password = 'a123456'
# 使用者重複輸入密碼
# 最多輸入3次
# 正確, 印出"登入成功!"
# 不正確, 印出"密碼錯誤! 還有__次機會"


i = 3
password = 'a123456'
while i > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break # 逃出迴圈
	else:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會')
