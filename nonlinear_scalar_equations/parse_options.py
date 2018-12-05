import sys, getopt

method_names = ['secant', 'simplified_newtons', 'sim', 'lobachevsky']
equasions_avaliable = [5, 34]

def help():
	print('main.py -e <equasion_number> -m <method name>')
	print('avaiable equasion numbers are:', equasions_avaliable, "(not for lobachesky method)")
	print('avaliable methods are:', method_names)
	sys.exit(2)

def check_options(options):
	if not options['equasion_num'] in equasions_avaliable:
		if not options['method_name'] == 'lobachevsky':
			print("wrong equasion number:", options['equasion_num'])
			help()
	if options['method_name'] == "":
		print("you must specify method name")
		help()
	if not options['method_name'] in method_names:
		print("wrong method name:", options['method_name'])
		help()
	if options['method_name'] == 'lobachevsky':
		if options['equasion_num'] != -1 :
			print("this equasion is not avaliable for lobachesky method")
			help()

def parse_and_validate_options(argv):
	options = {}
	options['equasion_num'] = -1
	options['method_name'] = ""

	try:
		opts, args = getopt.getopt(argv, "hm:e:", ["method=","equasion="])
	except getopt.GetoptError:
		help()

	for opt, arg in opts:
		if opt == '-h':
			help()
		if opt in ("-e", "--equasion"):
			options['equasion_num'] = int(arg)
		if opt in ("-m", "--method"):
			options['method_name'] = arg
	check_options(options)
	return options