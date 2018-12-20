import sys, getopt

demo_names = [
	'1: LU factorisation with main diagonal of ones on L: SLE #1', 
	'2: LQ decomposition: SLE #1', 
	'3: Holetsky method: SLE #2', 
	'4: Gaussian elimination: SLE #2',
	'5: Tomas algorithm: SLE #3',
	'6: LU factorisation with main diagonal of ones on U: SLE #3'
]


def help():
	print('main.py -d <demo_number>')
	print('main.py --demo=<demo_number>')
	print('\n\navaiable demos are:\n')
	for demo in demo_names:
		print(demo)
	sys.exit(2)

def parse_options(argv):
	demo_num = -1

	try:
		opts, args = getopt.getopt(
			argv, 
			"d:", 
			["demo="]
		)
	except getopt.GetoptError:
		help()

	for opt, arg in opts:
		if opt == '-h':
			help()
		elif opt in ("-d", "--demo"):
			demo_num = int(arg)
	if demo_num <= 0 or demo_num > 6:
		help()
	return demo_num