#we can use f !!
from  pathlib import  Path
import argparse
import sys

parser=argparse.ArgumentParser()
parser.add_argument('start',type=str,nargs=1)
parser.add_argument('-n','--name',type=str)
parser.add_argument('-t','--type',type=str)

args=parser.parse_args()
print(args)

start_path=Path(args.start[0])
if args.name:
    for f in start_path.rglob(args.name):
        print(f)

elif args.type:
    if args.type not in ['d','f']:
        print("unknown type：{args.type}")
        sys.exit(1)
    for f in start_path.rglob('*' or args.name):
        if args.type== "d" and f.is_dir():
            print(f)
        elif args.type== "f" and f.is_file():
            print(f)

else:
    print("please print -n or -t")
    sys.exit(1)
