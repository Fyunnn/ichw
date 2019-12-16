#!/usr/bin/env python3

"""tile.py: Show all the possibilities of placing tiles.

__author__ = "Jin-Yu Fu"
__pkuid__  = "1900011813"
__email__  = "Fyun@pku.edu.cn"
"""

m = int(input("length of your wall"))
n = int(input("width of your wall"))
a = int(input("length of your tile"))
b = int(input("width of your tile"))

# 首先，将m*n个空位按照0到m*n-1编号

def hengpu(m, n, a, b, k):  # 一定情况下，向右下角横铺所有占有的位置列表
    if k%m > m-a or k//m > n-b:  # 排除错误情况
        return("k_wrong")
    else:
        lst = []
        for i in range(b):
            z = k+m*i
            lst.extend(list(range(z, z+a)))
        return(lst)

def shupu(m, n, a, b, k):  # 同理竖铺
    return(hengpu(m, n, b, a, k))

# 设法列出n次横（0）或竖（1）的所有可能性，储存在poss中
num = int(m*n/a/b)
poss = []
for i in range(2**num):
    poss.append([])

for i in range(num):
    for (nn, val) in enumerate(poss):
        if (nn//(2**i))%2 == 0:
            poss[nn].append(0)
        else:
            poss[nn].append(1)

# 开始铺砖，0=横铺，1=竖铺，每次都从序号最小的位置开始铺
ans = []  # 注意a是否与b相等，这会影响到后面方案的数量！
if a != b:
    for pos in poss:
        others = list(range(m*n))  # 每一个pos是一种方式，先重置参数
        mayans = []
        for hs in pos:
            wrong = 0
            if hs == 0:  # 横着一块一块铺
                for unit in hengpu(m, n, a, b, min(others)):
                    if unit not in others:
                        wrong = wrong + 1
                if wrong == 0:
                    zhuan = hengpu(m, n, a, b, min(others))
                    mayans.append(zhuan)
                    for used in zhuan:
                        others.remove(used)
            if hs == 1:  # 竖着
                for unit in shupu(m, n, a, b, min(others)):
                    if unit not in others:
                        wrong = wrong + 1
                if wrong == 0:
                    zhuan = shupu(m, n, a, b, min(others))
                    mayans.append(zhuan)
                    for used in zhuan:
                        others.remove(used)
        if len(mayans) == int(m*n/a/b):
            ans.append(mayans)
else:
    if m%a == 0 and n%a == 0:
        mayans = []
        others = list(range(m*n))
        for i in range(int(m*n/a/b)):
            zhuan = hengpu(m, n, a, b, min(others))
            mayans.append(zhuan)
            for used in zhuan:
                others.remove(used)
        ans.append(mayans)
    

# 交互节面：输出所有可能，用户选择方案
for i in ans:
    print(i)
print("There are", len(ans), "(recorded as x) plans to choose, as listed above")

x = int(input("choose one plan from all these; use a integer between 0 and x-1:"))
ansi = ans[x]


# 作图部分
import turtle

li = turtle.Turtle()
sc = turtle.Screen()
li.speed(0)
sc.screensize(30*(m+1), 30*(n+1))
li.ht()

def loc(k):  # 在长m宽n的墙中（单元宽30），找到序号为k的墙单元左下角的位置
    return(((k%m)*30, (k//m)*30))

def drawsquare(k):  # 边长30，输入点的序号，使li以其为左下角画正方形
    x0 = loc(k)[0]
    y0 = loc(k)[1]
    li.up()
    li.goto(x0, y0)
    li.down()
    li.seth(0)
    li.fd(30)
    li.lt(90)
    li.fd(30)
    li.lt(90)
    li.fd(30)
    li.lt(90)
    li.fd(30)

# 画每一块砖并标号

for huazhuan in ansi:
    # 先画内部蓝线并标号
    li.color("blue")
    li.pensize(1)
    for k in huazhuan:  
        drawsquare(k)
        li.up()
        li.goto(loc(k)[0]+10, loc(k)[1]+10)
        li.write(str(k))
    # 再画外面黑线
    xs = []
    ys = []
    for k in huazhuan:
        xs.append(loc(k)[0])
        ys.append(loc(k)[1])
    x1 = min(xs)
    y1 = min(ys)
    li.up()
    li.goto(x1, y1)
    li.down()
    li.color("black")
    li.pensize(5)
    li.seth(0)
    li.fd(max(xs)-min(xs)+30)
    li.lt(90)
    li.fd(max(ys)-min(ys)+30)
    li.lt(90)
    li.fd(max(xs)-min(xs)+30)
    li.lt(90)
    li.fd(max(ys)-min(ys)+30)

# 以上即每一块砖的画法

turtle.exitonclick()  # 保持住屏幕，点击鼠标才退出


def main():
    """main module
    """
    print("everything goes well")


if __name__ == "__main__":
    main()
