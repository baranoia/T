# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 23:46:34 2018

@author: User
"""


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def test():
    for n in range(2, 10):
        for x in range(2, n):
            print("n={},x={}".format(n,x))
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
            else:
                # loop fell through without finding a factor
                print(n, 'is a prime number')


#・可変長引数あり関数「*引数名」
def method1(name, price, *args):
    print(type(args))
    for a in args:
        print(a)

print('--------')
print('可変長引数あり関数「*引数名」')
method1("ペン",100,"よくかける","0.4ミリで細い","書いて消せる",'色がそれなりにある','いい感じのペン','フリクション')

#・・キーワード可変長付き引数「**引数名」
def method2(name, price, **kwargs):
    print(type(kwargs))
    for a,b in kwargs.items():
        print(a,b)
print('--------')
print('キーワード可変長付き引数「**引数名」')
method2("ああ",1000, **{"add1":"ss","add2":"sss"}) 

#・可変長引数あり関数「*引数名」
def method1cs(name, price, *args, last_key):
    print(type(args))
    for a in args:
        print(a)
    print(last_key)

print('--------')
print('可変長引数あり関数「*引数名」')
method1cs("ペン",100,"よくかける","0.4ミリで細い","書いて消せる",'色がそれなりにある','いい感じのペン','フリクション', last_key = 'hoge')
