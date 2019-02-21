#拷贝文件实例
#argvtest.py需要导入库，所以必须要在开头指明路径
#!/usr/bin/env python3
import sys

def copy_file(src, dst):
	with open(src, 'r') as src_file:
		with open(dst, 'w') as dst_file:
			dst_file.write(src_file.readlines())

if __name__ == '__main__':
	if len(sys.argv) == 3:
		copy_file(sys.argv[1], sys.argv[2])
	else:
		print('Parameter Error')
		print(sys.argv[0], 'srcfile dstfile')
		sys.exit(-1)
	sys.exit(0)