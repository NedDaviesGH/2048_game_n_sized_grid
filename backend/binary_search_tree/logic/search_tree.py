from random import choice
import numpy as np
import pandas as pd
import time
import random
from .node import Node

def lookup_tree_value(value, node, counter=1):
    if value > node.value:
        counter += 1
        return lookup_tree_value(value, node.right, counter=counter+1)
    elif value < node.value:
        counter += 1
        return lookup_tree_value(value, node.left, counter=counter+1)
    elif value == node.value:
        return counter

def lookup_list(value, list, counter=1):
    for e in list:
        if e == value:
            break
        counter += 1
    return counter
    

def tree_report(value, storage):
    if type(storage) == Node:
        lookup_func = lookup_tree_value
    elif type(storage) == list:
        lookup_func = lookup_list


    start_time = time.time()
    steps = lookup_func(value, storage)
    end_time = time.time()

    return steps, end_time - start_time

def benchmark_search(num_data_points = 10, min=1, max=5, storage_type='node'):
    sizes_list = list(np.logspace(start=min, stop=max, num=num_data_points, dtype=int))
    steps_list = []
    times_list = []
    for size in sizes_list:
        test_data = [n for n in range(size)]
        if storage_type == 'node':
            storage = Node(test_data)
        elif storage_type == 'list':
            storage = [n for n in test_data]
            random.shuffle(storage)
            
        steps, time = tree_report(value = choice(test_data), storage = storage)
        steps_list.append(steps)
        times_list.append(time)
    return sizes_list, steps_list, times_list


def aggregate_results(benchmark_search_node, benchmark_search_list):
    sizes_tree, steps_tree, times_tree = benchmark_search_node
    sizes_list, steps_list, times_list = benchmark_search_list
    df = pd.DataFrame(data={
        'size_tree': sizes_tree, 
        'steps_tree': steps_tree, 
        'time_tree': times_tree,
        'size_list': sizes_list, 
        'steps_list': steps_list, 
        'time_list': times_list,    
    })
    
    df['log_size_tree'] = np.log10(df['size_tree'])
    df['log_size_list'] = np.log10(df['size_list'])
    
    return df