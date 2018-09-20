#only can find  by name in a  unfantancy way
from pathlib import Path
from sys import argv

_,start,query=argv

start_path=Path(start)

for  f in start_path.rglob(query):
	print(f)
