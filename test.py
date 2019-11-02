

import sys

for line in sys.stdin:
    ab.sp

def show_number(number):
    if number % 2 == 0:
        print(str(number) + " even")
    elif number == 0:
        print(str(number) + " zero")
    else:
        print(str(number) + " odd")



show_number(10)

import os
import psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)  # in bytes