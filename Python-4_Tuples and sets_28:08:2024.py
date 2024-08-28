Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup = (21,36,14,25)
>>> tup
(21, 36, 14, 25)
>>> tup[1]
36
>>> tup[1] = 33
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup[1] = 33
TypeError: 'tuple' object does not support item assignment
>>> # tuple is like a list but you cannot change it value
>>> 
>>> # curly brackets are for sets
>>> s = {22,25,14,21,5}
>>> s
{5, 21, 22, 25, 14}
>>> s = {25,14,98,63,75}
>>> s
{98, 25, 75, 14, 63}
>>> s = {25,14,98,63,75,98}
>>> s
{98, 25, 75, 14, 63}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> # set it will not make a sequence and it not support to pick a values
