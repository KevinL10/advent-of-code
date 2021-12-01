from requests import get
from constants import *

# Writes input to specified filename, year/day; uses the dates in constants.py otherwise
def write_input(filename, year=aoc_year, day=aoc_day):
	r = get(f'https://adventofcode.com/{year}/day/{day}/input', cookies = {'session': session})
	with open(filename, 'w') as f:
		f.write(r.text.strip())
	print(f"[+] Wrote day {day}/{year} input to {filename}:")
	print(f"[x] {r.text.split(chr(10))[0]} ")