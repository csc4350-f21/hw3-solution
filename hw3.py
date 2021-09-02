import time
import math
from typing import Dict, List, Str
import csv
import tempfile


def fizzbuzz():
    start = time.time()
    for i in range(1,101):
        if i % 5 == 0 and i % 3 == 0:
            print("Fizzbuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
    end = time.time()
    print(f"Elapsed time (s): {end - start}")


def sphere_volume(radius: int):
    return math.pi * 4 / 3 * radius ** 3


def dict_to_csv(d: Dict[str , List[Str]]): 
    columns = list(d.keys())
    with open('books.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(fieldnames=columns)
        writer.writeheader()
        for i in range(len(d[columns[0]])):
            writer.write_row({k: d[k][i] for k in d.keys()})


def csv_to_dict(csvfile: str):
    result = {}
    with open(csvfile, "r") as f:
        lines = f.readlines()
        lists = []
        columns = lines[0].strip().split(",")
        column_map = {i: col for (i, col) in enumerate(columns)
        for col in columns:
            result[col] = []
        for line in lines[1:]:
            fields = line.strip().split(",")
            for i, val in enumerate(fields):
                result[column_map[i]].append(val)
    return result


def combine_them(d: Dict[str, List[str]]):
    with tempfile.NamedTemporaryFile() as f:
        columns = list(d.keys())
        with open(f.name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(fieldnames=columns)
            writer.writeheader()
            for i in range(len(d[columns[0]])):
                writer.write_row({k: d[k][i] for k in d.keys()})
        
    result = {}
    with open(f.name, "r") as f:
        lines = f.readlines()
        lists = []
        columns = lines[0].strip().split(",")
        column_map = {i: col for (i, col) in enumerate(columns)
        for col in columns:
            result[col] = []
        for line in lines[1:]:
            fields = line.strip().split(",")
            for i, val in enumerate(fields):
                result[column_map[i]].append(val)
    return result
