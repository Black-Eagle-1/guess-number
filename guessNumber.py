import random

asw = random.randint(1, 100)
count = 0

while True:
	number = input("請輸入號碼: ")
	number = int(number)
	count = count + 1
	if asw == number:
		print("恭喜答對  總共花費:", count, "次")
		break
	elif asw < number:
		print("答錯，再嘗試看看  比", number, "小")
	elif asw >number:
		print("答錯，再試看看 比", number, "大")

