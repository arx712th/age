driving = input('請問有沒有開過車?　')

if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = int(input('請問你的年齡?　'))

if driving == "有":
	if age >= 18:
		print('通過測驗')
	else:
		print('阿捏母湯喔')

elif driving == "沒有":
	if age >=18:
		print('應該可以考駕照了')
	else:
		print('再等', 18-age,'年')
else:
	print('只能輸入有或沒有')
