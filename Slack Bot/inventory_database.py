#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 21:34:20 2018

@author: ameanasad
"""

import csv


"""
Dictionary that saves items based on a name as a key and the value is a list 
of three values: ID, Quantity, and Bin_no.

EX: items["insert name"] = [ID, Quantity, Bin_no]

"""
f =  open('Backroom_Inventory_2017_Sheet1.csv', 'rt', encoding='utf')
reader = csv.reader(f)
next(reader)

items = {}
item_id = 0
for row in reader:
    item_name = row[0]
    items[item_name] = [0,0,0]
    try:
        item_quantity = int(row[1])
    except ValueError:
        item_quantity = str(row[1])
    
    items[item_name][0] = item_id
    items[item_name][1] = item_quantity
    
    bin_number = row[2]
    
    items[item_name][2] = bin_number
 
    item_id = item_id + 1
"""
---------------------------------------------------
"""   

def search(items,keyword):
    """
    Search algorithm, that searches for an item using a name or a string. 
    Be careful with uppercase and lowercase letters.
    Returns all the relevant items with the name searches for, including the 
    ID, Quantity, and Bin_no
    """
    
    
    print("Searching for " + "'" + keyword + "'")
    found = False
    inventory = " "
    for item in items:
        if str(keyword.lower()) in item.lower():
            found = True
            string = "Item: " +item + " | "+ "ID: " + str(items[item][0])+" | "+"Quantity: " + str(items[item][1]) + " | " + "Bin No: " + str(items[item][2])
            inventory = inventory + string + "\n"
    if found == False:
        return "No Matches Found"
    
    else:
        return inventory
    
        


"""
--------------------------------------------------------------------
"""
    
"""
Dictionary that stores items based with a specific id as a key. 
The values returned are the Item name, quantity, and bin_no. 
Use the search algorithm to find an id, and use the dicitonary to use that id
to perform operations on the item list. 
"""

n =  open('Backroom_Inventory_2017_Sheet1.csv', 'rt', encoding='utf')
datum = csv.reader(n)
next(datum)
id_num = 0  
items_data = {}
for r in datum: 
    items_data[id_num] = [0,0,0]
    item_name1 = r[0]
    
    items_data[id_num][0] = item_name1

    try:
        item_quantity1 = int(r[1])
    except ValueError:
        item_quantity1 = str(r[1])
    
    items_data[id_num][1] = item_quantity1

    bin_number1 = r[2]
     
    items_data[id_num][2] = bin_number1
    
    id_num = id_num +1
 




"""
--------------------------------------------------------------------
""" 


class Database(object):
    def __init__(self):
        
        self.database = {}
        self.datum = {}
        self.item_id = 0
    
    def add_item(self, name, quantity, bin_no):
        
        for item in self.datum:
            if name == item:
                return "Item already exists in inventory"
        else:
            try:
                item_quantity = int(quantity)
            except ValueError:
                item_quantity = str(quantity)
            self.database[self.item_id] = [name,item_quantity, int(bin_no)]
            self.datum[name] = [self.item_id,item_quantity, int(bin_no)]
            self.item_id = self.item_id + 1
            
    
    def show_by_id(self):
        for item in self.database:
            print("item", self.database[item])
            print("id", item)
    
    def delete(self,item_id):
        name = self.database[item_id][1]
        del self.datum[name]
        del self.database[item_id]
        
    def get_item(self,item_id):
        
        return self.database[item_id][0]
    
    def get_value(self, item_id):
        return self.database[item_id][1]
    
    def get_datum(self):
        return self.datum

    
    def modify(self,item_id, quantity):
        self.database[item_id][1] = int(quantity)
        self.datum[self.database[item_id][0]][1] = quantity
        return None
               
    def get_database(self):
        return self.database


#    def search(self,keyword):
#        """
#        Search algorithm, that searches for an item using a name or a string. 
#        Be careful with uppercase and lowercase letters.
#        Returns all the relevant items with the name searches for, including the 
#        ID, Quantity, and Bin_no
#        """
#    
#    
#        print("Searching for " + "'" + keyword + "'")
#        found = False
#        inventory = " "
#        for item in self.datum:
#            if str(keyword.lower()) in item.lower():
#                found = True
#                string = "Item: " +item + " | "+ "ID: " + str(self.datum[item][0])+" | "+"Quantity: " + str(self.datum[item][1]) + " | " + "Bin No: " + str(self.datum[item][2])
#                inventory = inventory + string + "\n"
#        if found == False:
#            return "No Matches Found"
#        
#        else:
#            return inventory
    

