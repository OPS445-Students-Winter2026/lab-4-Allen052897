#!/usr/bin/env python3

def join_lists(l1, l2):
    result = []
    for item in l1:
        if item not in result:
            result.append(item)
    for item in l2:
        if item not in result:
            result.append(item)
    return result


def match_lists(l1, l2):
    result = []
    for item in l1:
        if item in l2 and item not in result:
            result.append(item)
    return result


def diff_lists(l1, l2):
    result = []
    for item in l1:
        if item not in l2 and item not in result:
            result.append(item)
    for item in l2:
        if item not in l1 and item not in result:
            result.append(item)
    return result


if __name__ == '__main__':
    list1 = list(range(1, 10))
    list2 = list(range(5, 15))

    print('list1:', list1)
    print('list2:', list2)
    print('join:', join_lists(list1, list2))
    print('match:', match_lists(list1, list2))
    print('diff:', diff_lists(list1, list2))

