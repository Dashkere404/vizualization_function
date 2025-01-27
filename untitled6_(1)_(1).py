# -*- coding: utf-8 -*-
"""Untitled6 (1) (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qKVVgPRZlyF0DrkNW4VzJVgQoMSV5ZLn
"""

from matplotlib import pyplot as plt
def f(a, x, y, b):
  g = 1.0 - a*x*x + y
  h = b*x
  return g, h
x = 0
y = 0
x, y = f(1.2, x, y, 0.3)
print('For x = 0 next x =', x, '\nFor y = 0 next y =', y)

from matplotlib import pyplot as plt
def f(a, x, y, b):
  g = 1.0 - a*x*x + y
  h = b*x
  return g, h
def graph(a, b):
  x = 0
  y = 0
  print ("First 5 coordinates for a =", a, "b =", b)
  print('\nx =',x, 'y =', y)
  list_x = []
  list_y = []
  list_x.append(x)
  list_y.append(y)
  plt.figure(figsize=(8,8))
  for i in range (1000):
    x, y = f(a, x, y, b)
    if (i<4):
      print('\nx =',x, 'y =', y)
    list_x.append(x)
    list_y.append(y)
  plt.plot(list_x, list_y, color = 'red')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('a = ' + str(a) + ' b = ' + str(b))
  plt.show()
graph(0.8, 0.3)
graph(1.25, 0.04)
graph(1.42, 0.26)

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def f(A, B, C, x, y, z):
  g = y
  h = z
  m = B*x + C*y + A*z - y*y
  return g, h, m
def graph(A, B, C):
  x = 0.1
  y = 0.01
  z = 0.001
  print ("First 5 coordinates for A =", A, "B =", B, "C =", C)
  print('\nx =',x, 'y =', y, 'z =', z)
  list_x = []
  list_y = []
  list_z = []
  list_x.append(x)
  list_y.append(y)
  list_z.append(z)
  plt.figure(figsize=(8,8))
  for i in range (1000):
    x, y, z = f(A, B, C, x, y, z)
    if (i<4):
      print('\nx =', x, 'y =', y, 'z =', z)
    list_x.append(x)
    list_y.append(y)
    list_z.append(z)
  ax = plt.axes(projection="3d")
  ax.plot(list_x, list_y, list_z, color='purple')
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('z')
  ax.set_title('A = ' + str(A) + ' B = ' + str(B) + 'C = ' + str(C))
  plt.show()
graph(0.61, -0.5, 0.13)
graph(-0.12, -0.5, -0.89)
graph(-0.42, -0.5, -1.38)

from matplotlib import pyplot as plt
import numpy as np
def f(r, x):
  return r*x*(1-x)
r_values=np.linspace(2.4, 4.0, 1000)
list_r=[]
list_x=[]
c=0
for r in r_values:
  x=0.01
  for i in range (9999):
    x=f(r, x)
    if i>8998:
      list_r.append(r)
      list_x.append(x)
plt.plot(list_r, list_x, color = 'green')
plt.xlabel('r')
plt.ylabel('x')
plt.show()