#only find by name in fantasy way
from pathlib import Path
import  argparse

parser=argparse.ArgumentParser()

parser.add_argument('start',type=str)
parser.add_argument('-n','--name',type=str)
parser.add_argument('-t','--type',type=str)

args=parser.parse_args()
print(args)

#断点
start_path=Path(args.start[0])#address

for f in start_path.rglob(args.name):#name
	print(f)
