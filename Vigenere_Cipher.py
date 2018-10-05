# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 00:15:52 2017

@author: ameanasad

"""


import string
import itertools as it

class Cipher(object):
    
    def __init__(self, text, keyword):
        self.text = text
       
    def get_text(self):
        return self.text
    
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26
    
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        LowerCase = string.ascii_lowercase;
        
        Dictionary = {}
        shifterLower = LowerCase[shift:]+ LowerCase[:shift];
        
        for y in LowerCase:
            Dictionary[y] = shifterLower[LowerCase.index(y)];
    
        return Dictionary 
           
    def construct_shift(self):
        letters = string.ascii_lowercase;
        dict_table = {}
        encompass = []
        for x in range(len(letters)):
        
            encompass.append(self.build_shift_dict(x))
            
            dict_table[letters[x]] = encompass[x]
        
        return dict_table       
    
    def get_shift_dict(self, keyword):
    
        dicted = self.construct_shift()
        shift_dict = {}
        
        for x in keyword:
            shift_dict[x] = dicted[x]
            
        return shift_dict
    
    def apply_shift(self, keyword, message):
        ciphered = ''
        shift_dict = self.get_shift_dict(keyword)
        keyword_cycle = it.cycle(keyword)
        for letter in message:
            if letter in string.ascii_lowercase:
                for char in keyword_cycle:
                    dict_used = shift_dict[char]
                    ciphered = ciphered + dict_used[letter]
                    
                    break
        
        return ciphered
                
    def decrypt(self, keyword, encrypted_text):
        decrypted = ''
        shift_dict = self.get_shift_dict(keyword)
        keyword_cycle = it.cycle(keyword)
        for letter in encrypted_text:
            if letter in string.ascii_lowercase:
                for char in keyword_cycle:
                    dict_used = shift_dict[char]
                    inv_dict= {v: k for k, v in dict_used.items()}
                    decrypted = decrypted + inv_dict[letter]
                    
                    break
        return decrypted
    
    
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


def construct_shift():
    letters = string.ascii_lowercase;
    dict_table = {}
    encompass = []
    for x in range(len(letters)):
        
        encompass.append(build_shift_dict(x))
        
        dict_table[letters[x]] = encompass[x]
        
    return dict_table
    

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
             another letter (string). 
    '''
    LowerCase = string.ascii_lowercase;
    
    Dictionary = {}
    shifterLower = LowerCase[shift:]+ LowerCase[:shift];
    
    for y in LowerCase:
        Dictionary[y] = shifterLower[LowerCase.index(y)];
    
    return Dictionary 
           

def get_shift_dict(keyword):
    
    dicted = construct_shift()
    shift_dict = {}
    
    for x in keyword:
        shift_dict[x] = dicted[x]
    return shift_dict

def apply_shift(keyword, message):
    ciphered = ''
    shift_dict = get_shift_dict(keyword)
    keyword_cycle = it.cycle(keyword)
    for letter in message:
        if letter in string.ascii_lowercase:
            for char in keyword_cycle:
                dict_used = shift_dict[char]
                ciphered = ciphered + dict_used[letter]
                
                break
    
    return ciphered
                
def decrypt(keyword, encrypted_text):
    decrypted = ''
    shift_dict = get_shift_dict(keyword)
    keyword_cycle = it.cycle(keyword)
    for letter in encrypted_text:
        if letter in string.ascii_lowercase:
            for char in keyword_cycle:
                dict_used = shift_dict[char]
                inv_dict= {v: k for k, v in dict_used.items()}
                decrypted = decrypted + inv_dict[letter]
                
                break
    return decrypted
