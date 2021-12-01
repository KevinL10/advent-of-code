# Access the utils folder
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../utils")

from utils import *

write_input('input.txt', year=2020, day=3)