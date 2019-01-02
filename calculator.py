import sys

def main():
	#检查命令行参数合法性，并转换为正确类型
	if len() != 2:
		print('Parameter Error')
		exit()
	try:
		salary = int(sys.argv[1])
	except ValueError:
		print('Parameter Error')
		exit()

	#扣税起征点
	valvue = salary - 3500
	
	#根据落入的税率区间，按照对应的税率参数计算税率
	if valvue <= 0:
		tax = 0
	elif valvue <= 1500:
		tax =valvue * 0.03 - 0
	elif valvue <= 4500:
		tax =valvue * 0.10 - 105
	elif valvue <= 9000:
		tax =valvue * 0.20 - 555
	elif valvue <= 35000:
		tax =valvue * 0.25 - 1005
	elif valvue <= 55000:
		tax =valvue * 0.30 - 2755
	elif valvue <= 80000:
		tax =valvue * 0.45 - 13505

	#打印结果
	print('{:.2f}'.format(tax))


if __name__ == '__main__':
	main()
