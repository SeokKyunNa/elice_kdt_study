'''
A+B -5
'''
import sys
input = sys.stdin.readline

while 1:
    a, b = map(int, input().split())
    if a==0 and b==0:
        exit()
    print(a+b)