from os import pardir
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Calculates the average number of days required to complete each number of rewinds.")
parser.add_argument("max_day", type=int, help="Highest day achieved", required=True)
parser.add_argument("rewinds", type=int, help="Number of rewinds", required=True)
parser.add_argument("time_jump", type=int, default=0, help="Level of time_jump ability", required=True)
parser.add_argument("fast_rewind", type=bool, default=True, help="True if purchased fast rewind", required=True)
args = parser.parse_args()


portal_distance = np.ceil(args.max_day/500) * 5
if args.fast_rewind: portal_distance *= 2

def portal_chance(day, max_day):
    

if __name__ == '__main__':
    
    if(args.max_day < 0 or args.rewinds < 0 or args.time_jump < 0):
        print("Invalid arguments")
    else:

    