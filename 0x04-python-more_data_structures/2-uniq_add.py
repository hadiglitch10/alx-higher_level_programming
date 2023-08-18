#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    total_sum = 0

    for num in unique_numbers:
        total_sum += num
    return total_sum
