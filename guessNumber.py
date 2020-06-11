import random

asw = random.randint(1, 100)

while True:
	number = input("請輸入號碼: ")
	number = int(number)
	if asw == number:
		print("恭喜答對")
		break
	elif asw < number:
		print("答錯，再嘗試看看  比", number, "小")
	elif asw >number:
		print("答錯，再試看看 比", number, "大")

