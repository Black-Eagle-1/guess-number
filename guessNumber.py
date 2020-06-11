import random

print("歡迎來到猜終極密碼")
print("輸入1進入一般模式")
print("輸入2進入自訂模式")




while True:
	mode = input("請選擇模式: ")
	mode = int(mode)
	count = 0

	if mode == 1:
		asw = random.randint(1, 100)
		print("已進入一般模式")

		number = input("請輸入號碼: ")
		number = int(number)

		while number != asw:
			count = count + 1
			if asw < number:
				print("答錯，再嘗試看看  答案比", number, "小")
				number = input("請輸入號碼: ")
				number = int(number)
			elif asw > number:
				print("答錯，再嘗試看看  答案比", number, "大")
				number = input("請輸入號碼: ")
				number = int(number)
		print("恭喜答對  總共花費:", count, "次")
		break


	elif mode == 2:
		big = input("請輸入範圍最大值: ")
		small = input("請輸入範圍最小值: ")
		big = int(big)
		small = int(small)
		asw = random.randint(small, big)
		print("已進入自訂模式")

		number = input("請輸入號碼: ")
		number = int(number)
		

		while number != asw:
			count = count + 1
			if asw < number:
				print("答錯，再嘗試看看  答案比", number, "小")
				number = input("請輸入號碼: ")
				number = int(number)
			elif asw >number:
				print("答錯，再嘗試看看  答案比", number, "大")
				number = input("請輸入號碼: ")
				number = int(number)
		print("恭喜答對  總共花費:", count + 1, "次")
		break

	else:
		print("只能輸入1或2")


