import sys, getopt

method_names = ['secant', 'simplified_newtons', 'sim', 'lobachevsky']
equasions_avaliable = [5, 34]

def help():
	print('main.py -m <method name> -e <equasion_number> -a <num> -b <num>' )
	print('main.py --method=<method name> --equasion=<equasion_number> --a=<num> --b=<num>')
	print('avaiable equasion numbers are:', equasions_avaliable, "(not for lobachesky method)")
	print('avaliable methods are:', method_names)
	sys.exit(2)

def check_options(options):
	if options['method_name'] == 'lobachevsky':
		if options['equasion_num'] != -1 :
			print("this equasion is not avaliable for lobachesky method")
			help()
		else:
			return
	if options['method_name'] == "":
		print("you must specify method name")
		help()
	if not options['method_name'] in method_names:
		print("wrong method name:", options['method_name'])
		help()
	if options['equasion_num'] == "":
		print("you must specify equasion number")
	if not options['equasion_num'] in equasions_avaliable:
		print("wrong equasion number:", options['equasion_num'])
		help()
	if options['a'] == "" or options['b'] == "":
		print("you must specify a and b")
		help()
	if options['a'] == options['b']:
		print("a and b must be different")
		help()

def parse_and_validate_options(argv):
	options = {}
	options['equasion_num'] = ""
	options['method_name'] = ""
	options['a'] = ""
	options['b'] = ""

	try:
		opts, args = getopt.getopt(
			argv, 
			"hm:e:a:b:", 
			["method=", "equasion=", "a=", "b="]
		)
	except getopt.GetoptError:
		help()

	for opt, arg in opts:
		if opt == '-h':
			help()
		elif opt in ("-e", "--equasion"):
			options['equasion_num'] = int(arg)
		elif opt in ("-a", "--a"):
			options['a'] = float(arg)
		elif opt in ("-b", "--b"):
			options['b'] = float(arg)
		elif opt in ("-m", "--method"):
			options['method_name'] = arg
	check_options(options)
	return options

