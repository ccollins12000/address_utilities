#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:50:16 2021

@author: charlescollins
"""

import csv
import re



with open('street_suffix_abbreviations.csv', mode='r') as abbr_file:
    reader = csv.reader(abbr_file)
    all_street_suffixes = {rows[0]:rows[1] for rows in reader}

with open('secondary_address_abbreviations.csv', mode='r') as abbr_file:
    reader = csv.reader(abbr_file)
    secondary_address_abbreviations = {rows[0]:rows[1] for rows in reader}
    
with open('directional_abbreviations.csv', mode='r') as abbr_file:
    reader = csv.reader(abbr_file)
    directional_abbreviations = {rows[0]:rows[1] for rows in reader}  
    
def standardize_directions(address_line):
    """Replaces common directional indicators with their abbreviation. Example: NORTH with N
    
    args:
        address_line (str): The address line (example: '1234 main st' )
    
    """
    for direction_name, direction_abbreviation in directional_abbreviations.items():
        address_line = re.sub(r'\b' + direction_name + r'\b', direction_abbreviation, address_line)
    
    return address_line
    

def standardize_street_suffixes(address_line1):
    """Replaces common street suffixes with the standard US postal abbreviation. Suffix must appear
    at the end of the stinrg
    
    args:
        address_line1 (str): The address line1 (example: '1234 main st' )
    
    """
    for suffix_name, suffix_abbreviation in all_street_suffixes.items():
        address_line1 = re.sub(r'\b' + suffix_name + r'$', suffix_abbreviation, address_line1)
    
    return address_line1
    
    
def standardize_secondary_indicators(address_line2):
    """Replaces common street suffixes with the standard US postal abbreviation. Suffix must appear
    at the end of the stinrg
    
    args:
        address_line2 (str): The address line1 (example: 'APARTMENT 2' )
    
    """
    for secondary_address_indicator, secondary_address_abbreviation in secondary_address_abbreviations.items():
        address_line2 = re.sub(r'\b' + secondary_address_indicator + r'\b', secondary_address_abbreviation, address_line2)
    
    return address_line2


