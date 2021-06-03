# import pygame
# from pygame.locals import *
import os
os.system('cls')


def my_namespace():
    x = 43
    print('-F' * 30)
    print(f'LOCALS:\n{locals()}\n')
    print(f'GLOBALS:\n{globals()}')
    print(f'x = {x}   id(x) = {id(x)}    id(34) = {id(34)}    id(35) = {id(35)}')
    print('-F' * 30, '\n')


x = 34
my_namespace()

print('-M' * 30)
print(f'LOCALS:\n{locals()}\n')
print(f'GLOBALS:\n{globals()}\n')
print(f'x = {x}   id = {id(x)}')
print('-M' * 30, '\n')

print()
print(f'x = {x}   id(x) = {id(x)}    id(34) = {id(34)}    id(35) = {id(35)}')
x = x + 1
print(f'x = {x}   id(x) = {id(x)}    id(34) = {id(34)}    id(35) = {id(35)}')
print()


print(locals()['x'])
print(id(locals()['x']))
