import sys
from parse_options import parse_options
from demos import get_demo

num = parse_options(sys.argv[1:])
demo = get_demo(num)

demo()