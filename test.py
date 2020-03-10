#os.system("lava-test-case %s --result %s" % (name, result))
#print("%s --result %s" % (name, result))

import os

def main():
	output = os.popen('uname -a').read()

	if 'Linux' in output:
#		print('Pass')
		return True
	else:
#		print('Fail')
		return False

if __name__ == '__main__':
	result = main()

	if result:
		print('pass')
		#os.system("lava-test-case pTest --result pass")
		print("pTest --result pass")
	else:
		print('fail')
		#os.system("lava-test-case pTest --result fail")
		print("pTest --result fail")

