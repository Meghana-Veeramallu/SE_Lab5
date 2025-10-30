"""Inventory Management System"""

import json
#import logging
from datetime import datetime

# Global variable
stock_data = {}

#add docstrings to all functions
def add_item(item, qty, logs=None):
    '''Add an item with the specified quantity'''
    if logs is None:
        logs = []   #mutuable default argument fix

    if item in stock_data:
        stock_data[item] += qty
    else:
        stock_data[item] = qty
    logs.append(f"Added {qty} of {item}")
    print(f"Added {qty} of {item}")

def remove_item(item, qty):
    '''Remove an item or reduce quantity'''
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:    #Bare except
        pass

def get_qty(item):
    '''Return quantity of given item'''
    return stock_data[item]

def load_data(file="inventory.json"):
    '''Load inventory data from JSON file'''
    f = open(file, "r")
    global stock_data
    stock_data = json.loads(f.read())
    f.close()

def save_data(file="inventory.json"):
    '''Save inventory data to JSON file'''
    f = open(file, "w")
    f.write(json.dumps(stock_data))
    f.close()

def print_data():
    '''Display all items and their quantities'''
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def check_low_items(threshold=5):
    '''Return list of items below given threshold'''
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    '''Run inventory test simulation'''
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("eval used")  # replaced unsafe eval

main()
