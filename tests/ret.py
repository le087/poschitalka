# -*- coding: utf-8 -*-
###########################################################
#------ GNU GPL2 -----------------------------------------#
###########################################################
#
#проверка использования возвращения значений функцией

b = int(raw_input())
stroka = 'Радость'
nt = 'Печаль'

def test():
    if b == 1:
        return stroka
    else:
        return nt


d = 0
while d <> 1:
    p = test()
    print p
    d = int(raw_input('Для выхода введите 1: '))

