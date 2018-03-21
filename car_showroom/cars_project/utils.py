# -*- coding: utf-8 -*-


def digit_from_list(list_item):

    l = len(list_item)
    int_id_list = []
    i = 0
    while i < l:
        s_int = ''
        a = list_item[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = list_item[i]
            else:
                break
        i += 1
        if s_int != '':
            int_id_list.append(int(s_int))
    return int_id_list