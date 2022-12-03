# https://www.acmicpc.net/problem/9375

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cloths = {}

    for _ in range(int(input())):
        c_name, c_class = input().split()
        cloths[c_class] = c_name
        
    print(cloths)