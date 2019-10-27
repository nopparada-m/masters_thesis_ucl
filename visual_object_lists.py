#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:18:57 2019

@author: Nopparada (under kind guidance of Sebastian Bobadilla-Suarez)  :)
"""
##Imports WordNet files


import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

##Generates the synsets for items in the first list

words = list(['german_shepherd', 'tibetan_mastiff', 'malamute', 'chow_chow', 'cardigan', 'siamese_cat', 'persian_cat', 'cougar', 
              'american_black_bear', 'fly', 'dung_beetle', 'cricket', 'dragonfly', 'sea_urchin', 'wood_rabbit',
              'fox_squirrel', 'mink', 'echidna', 'macaque', 'squirrel_monkey', 'giant_panda', 'barracouta',
              'academic_gown', 'pail', 'flute', 'cello', 'pier', 'fountain_pen', 'marimba', 'french_horn',
              'poncho', 'bassinet', 'beacon', 'dumbell', 'pickup_truck', 'microphone', 'minibus', 'notebook', 
              'palace', 'airship', 'pretzel', 'mashed_potatoes', 'zucchini', 'acron_squash', 'lemon', 'pineapple',
              'pomegranate', 'broccoli', 'tandem_bicycle', 'fireboat', 'cash_machine', 'desktop_computer', 
              'yurt', 'croquet_ball', 'water_jug', 'tricycle', 'cassett_player', 'letter_opener', 'tractor',
              'petri_dish', 'kerry_blue_terrier', 'spindle', 'shopping_cart', 'dowitcher', 'ruddy_turnstone', 
              'prairie_chicken', 'european_gallinule', 'papillon'])
             
           
for i in words:
    print(wn.synsets(i.lower())) 


##Generates the synsets for items in the second list

words2 =   list(['brittany_spaniel', 'rottweiler', 'bull_mastiff', 'siberian_husky', 'pomeranian', 'pembroke',
                 'tabby_cat', 'lynx', 'jaguar', 'ice_bear', 'bee', 'leaf_beetle', 'grasshopper', 'lacewing',
                 'starfish', 'angora', 'hamster', 'weasel', 'otter', 'baboon', 'spider_monkey', 'lesser_panda', 
                 'eel', 'lab_coat', 'cauldron', 'oboe', 'violin', 'dock', 'syringe', 'organ', 'cornet', 'cloak',
                 'cradle', 'dome', 'barbell', 'jeep', 'joystick', 'mobile_home', 'envelope', 'mosque', 'airliner',
                 'bagel', 'guacamole', 'cucumber', 'bell_pepper', 'orange', 'custard_apple', 'granny_smith', 
                 'cauliflower', 'moped', 'aircraft_carrier', 'dishwasher', 'laptop', 'mountain_tent', 'ping-pong_ball',
                 'teapot', 'tripod', 'CD_player', 'quill', 'harvester', 'tray', 'irish_terrier', 'reel', 'tub',
                 'albatross', 'bittern', 'ptarmigan', 'limpkin', 'japanese_spaniel'])
             
for i in words2:
    print(wn.synsets(i.lower()))    
    
    
##Generates the synsets for items in the third list  
    
words3 = list(['gordon_setter', 'doberman', 'great_dane', 'samoyed', 'lhasa', 'chihuahua', 'egyptian_cat', 'leopard',
               'cheetah', 'brown_bear', 'ant', 'rhinocorous_beetle', 'mantis', 'damselfly', 'sea_cucumber', 
               'hare', 'guinea_pig', 'badger', 'skunk', 'langur', 'titi', 'indri', 'sturgeon', 'trench_coat',
               'bucket', 'bassoon', 'harp', 'apiary', 'matchstick', 'accordion', 'saxophone', 'gown', 'crib',
               'ambulance', 'horizontal_bar', 'minivan', 'ladle', 'fire_engine', 'motarboard', 'church','parachute',
               'cheeseburger', 'trifle', 'butternut_squash', 'artichoke', 'fig', 'jackfruit', 'head_cabbage',
               'mushroom', 'unicycle', 'canoe', 'vending_machine', 'monitor', 'castle', 'puck', 'vase', 'totem_pole',
               'tape_player', 'ruler', 'trailer_truck', 'envelope', 'cairn_terrier', 'pinwheel', 'washbasins',
               'king_penguin', 'american_coot', 'coucal', 'redshank', 'yorkshire_terrier'])

for i in words3:
    print(wn.synsets(i.lower()))            

