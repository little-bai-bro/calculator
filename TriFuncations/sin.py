from math import pi

def factorial(n):#求阶乘
	result = 1
	for i in range(1,n+1):
		result *= i
	return result

def sin(x):
	#输入角度值，返回角度值对应的sin值,精度到计算50次为止
	radian = x/180*pi#将角度转化为弧度值
	result = radian
	for j in range(1, 50):#计算50次幂函数
		if j%2 == 0:
			result += (radian**(2*j+1))/factorial(2*j+1)
		else:
			result -= (radian**(2*j+1))/factorial(2*j+1)
	return round(result,2)#返回百分位精度的结果

