#!usr/bin/env python3
# -*- coding: utf-8 -*-


def decorate(func):
    def dct(lst1, lst2):
        keys, items = func(lst1, lst2)
        result = dict()
        for i, item in enumerate(keys):
            result[item] = items[i]
        return result
    return dct


@decorate
def lst(l1=' ', l2=' '):
    l1 = l1.split(' ')
    l2 = l2.split(' ')
    return l1, l2


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(lst(s1, s2))
