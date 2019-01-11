#改进版
#输入101:3500 102:7000 103:13000 104:25000
#输出ID:税后收入
import sys
from collections import namedtuple

TaxRate = namedtuple('TaxRate',['start_point','rate','cost'])

TaxRateTable = [
    TaxRate(80000, 0.45, 13505),
    TaxRate(55000, 0.35, 5505),
    TaxRate(35000, 0.30, 2755),
    TaxRate(9000, 0.25, 1005),
    TaxRate(4500, 0.20, 555),
    TaxRate(1500, 0.10, 105),
    TaxRate(0, 0.03, 0)]


#根据落入的税率区间，按照对应的税率参数计算税率
def TaxCalculation(income):
	num = income * (1 - 0.165) - 3500
	for item in TaxRateTable:
		if num > item.start_point:
			tax = num * item.rate - item.cost
			return '{:.2f}'.format(tax), '{:.2f}'.format(income * (1 - 0.165) - tax)
	return '0.00', '{:.2f}'.format(income * (1 - 0.165))

def main():
	for item in sys.argv[1:]:
		id, salary = item.split(':')
		try:
			income = int(salary)
		except ValueError:
			print('Parameter Error')
			continue
			
		_, remain = TaxCalculation(income)
		print('{}:{}'.format(id, remain))

if __name__ == '__main__':
	main()



