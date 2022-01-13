#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:54:18 2018

@author: ameanasad
"""

from inventory_database import inventory_dat
from slackclient import SlackClient
from weather import Weather, Unit
from datetime import datetime
import random
import time
import re 

# instantiate Slack client
slack_client =SlackClient('xoxb-360721473333-WP1kh8rfZncwHaJF51YSCApV')
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
CHANNEL_ID = "CALH3MAQJ"
 
members_list = {}


members = slack_client.api_call("users.list")
for person in members['members']:   
    members_list[person['id']] = person['real_name']

   
bot_name = 'kingtut'

def get_bot_id(name):
       api_call = slack_client.api_call("users.list")
       if api_call.get('ok'):
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == name:
                    return "<@" + user.get('id') + ">"
             
       return None

bot_id = get_bot_id(bot_name)

def get_date():
     date= datetime.now().strftime('%H:%M:%S')  
     date_split = date.split(':')    
     hour = int(date_split[0])
     minutes = int(date_split[1])
     seconds = int(date_split[2])
     return hour,minutes,seconds
        
def get_event():
    
    if slack_client.rtm_connect(with_team_state=False):
            print("Successfully connected, listening for commands")
            while True:
                hour,minutes,seconds = get_date()
                if hour ==11 and minutes == 22 and seconds ==1:
                    print("success")
                    kt = bot()      
                    text = kt.get_weather()
                    post_message(text, CHANNEL_ID)
                    time.sleep(1)
                
                event = slack_client.rtm_read()
                
                wait_for_event(event)
                 
                time.sleep(1)
    else:
        exit("Error, Connection Failed")
            

def post_message(message,channel_id):
    print("Posting message")
    slack_client.api_call(
      "chat.postMessage",
      channel= channel_id,
      text= message
      )
    
    return None
 
    
def wait_for_event(event):
    
    if len(event) > 0:
        print("Waiting for event" + "\n")
        if 'text' in event[0]:
            print("text in event" + "\n")
            if bot_id in event[0]['text']:
                                
                channel = event[0]['channel']
                user = members_list[str(event[0]['user'])]
                text = event[0]['text']
                handle_message(text, user, channel)
                
  
def handle_message(text, user, channel):
    print("Handling Message")
    text_list = text.split(" ")
    command = bot()
    
    if text_list[1] == "search":
        command.search(str(text_list[3]), channel)
    if "remove" in text_list:
        command.logging_remove(text,user,channel)
    if "add" in text_list:
        command.logging_add(text,user,channel)
           
    return text_list 
    

class bot(object):
#    def __init__(self):
#        
#        self.text_list = text_list
#        self.user = user
#        self.channel = channel
#        pass
    def search(self,keyword,channel):
        """
        Search algorithm, that searches for an item using a name or a string. 
        Be careful with uppercase and lowercase letters.
        Returns all the relevant items with the name searches for, including the 
        ID, Quantity, and Bin_no
        """
    
    
        print("Searching for " + "'" + keyword + "'")
        found = False
        inventory = " "
        data = inventory_dat.get_datum()
        for item in data:
            if str(keyword.lower()) in item.lower():
                found = True
                string = "Item: " +item + " | "+ "ID: " + str(data[item][0])+" | "+"Quantity: " + str(data[item][1]) + " | " + "Bin No: " + str(data[item][2])
                inventory = inventory + string + "\n"
        if found == False:
            text = "No Matches Found"
            post_message(text,channel)
            return "No Matches Found"
        else:
            text = inventory
            post_message(text,channel)
            return inventory
        
            
    def logging_add(self, text, user, channel):
        
        logging_ints = []
        text_modified = text.split(' ', 1)[1]
        mapped = map(int, re.findall(r'\d+', text_modified))
        for num in mapped:
            logging_ints.append(num)
        
        new_quantity = int(logging_ints[0]) + inventory_dat.get_value(logging_ints[1])
        
        inventory_dat.modify(logging_ints[1],new_quantity)
        
        text =  (user + " returned "+str(logging_ints[0])+' '+ str(inventory_dat.get_item(logging_ints[1])) 
        + "\n" + " Remaining: " + str(inventory_dat.get_value(logging_ints[1])))
        post_message(text,channel)
    
    def logging_remove(self, text,user, channel):
        
        logging_ints = []
        text_modified = text.split(' ', 1)[1]

        mapped = map(int, re.findall(r'\d+', text_modified))
        
        
        for num in mapped:
            logging_ints.append(num)
        
        if int(inventory_dat.get_value(logging_ints[1])) - int(logging_ints[0]) < 0:
           
            text =( "Sorry " + user + ", there's only "+str(inventory_dat.get_value(logging_ints[1])) +
                   ' '+str(inventory_dat.get_item(logging_ints[1]))+" remaining in the inventory")
            post_message(text,channel)

        else:     
            new_quantity =  inventory_dat.get_value(logging_ints[1]) - int(logging_ints[0])
            
            inventory_dat.modify(logging_ints[1],new_quantity)
            
            text= (user + " used "+str(logging_ints[0])+' '+str(inventory_dat.get_item(int(logging_ints[1]))) 
            +'\n'+ " Remaining: " + str(inventory_dat.get_value(int(logging_ints[1]))))
               
            post_message(text,channel)
    
        
  
get_event() 

