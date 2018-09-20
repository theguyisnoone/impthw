#put all the things into  def()
from  pathlib import  Path
import argparse
import sys


def  parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('start',type=str,nargs=1)
    parser.add_argument('-n','--name',type=str)
    parser.add_argument('-t','--type',type=str)

    return parser.parse_args()


def find_file(args):
    start_path=Path(args.start[0])
    if args.name and not args.type:
        name_find(start_path,args)
    elif args.type:
        type_find(start_path,args)
    else:
        print("please print -n or -t")
        sys.exit(1)



def name_find(start_path,args):
    for f in start_path.rglob(args.name):
        print(f)

def type_find(start_path,args):
    if args.type not in ['d','f']:
        print("unknown type：{args.type}")
        sys.exit(1)
    for f in start_path.rglob('*' or args.name):
        if args.type== "d" and f.is_dir():
            print(f)
        elif args.type== "f" and f.is_file():
            print(f)

find_file(parse_args())
