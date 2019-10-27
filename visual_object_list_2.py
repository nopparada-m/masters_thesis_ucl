#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:22:06 2019
Reference: http://www.nltk.org/howto/wordnet.html
@author: Nopparada
"""

import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

##Generates the synsets for items in the first list

##words1 = The first list of the close triplet; words2 = The second list of the close triplets; 
##words3 = The last list of the close triplets; words4 = The first list of the far triplets;
##words5 = The second list of the far triplets; words6 = The last list of the far triplets.


words1 = list(['black_grouse', 'cock', 'great_white', 'eft', 'jay', 'tench', 'african_grey', 'black_swan',
           'wallaby', 'jellyfish', 'flatworm', 'chambered_nautilus', 'crayfish', 'bustard', 'italian_greyhound',
           'siberian_husky', 'pomeranian', 'pembroke', 'lynx', 'cougar', 'fly', 'grasshopper', 'angora',
           'fox_squirrel', 'echidna', 'lesser_panda', 'barracouta', 'cauldron', 'flute', 'violin', 'fountain_pen',
           'marimba', 'cornet', 'cloak', 'dome', 'barbell', 'pickup_truck', 'minibus','notebook', 'palace',
           'airliner', 'bagel', 'guacamole', 'cucumber', 'acorn_squash', 'orange', 'pineapple', 'granny_smith',
           'cauliflower', 'tandem_bicycle', 'aircraft_carrier', 'dishwasher', 'laptop', 'mountain_tent', 'ping-pong_ball',
           'water_jug', 'tripod', 'cassette_player', 'letter_opener', 'tray', 'kerry_blue_terrier', 'reel',
           'shopping_cart', 'dowitcher', 'ruddy_turnstone', 'ptarmigan', 'european_gallinule', 'japanese_spaniel'])
 
for i in words1:
    print(wn.synsets(i.lower())) 


words2 = list(['partridge', 'ostrich', 'hammerhead', 'common_newt', 'indigo_bunting', 'goldfish', 'macaw', 'drake', 'wombat',
           'sea_anemone', 'nematode', 'conch', 'spiny_lobster', 'oyster_catcher', 'whippet', 'malamute', 'chow_chow',
           'cardigan', 'persian_cat', 'cheetah', 'ant', 'cricket', 'wood_rabbit', 'guinea_pig', 'skunk', 'giant_panda',
           'sturgeon', 'pail', 'bassoon', 'cello', 'matchstick', 'accordion', 'french_horn', 'poncho', 'beacon', 'dumbbell',
           'minivan', 'fire_engine', 'mortarboard', 'church', 'airship', 'pretzel', 'mashed_potato', 'zucchini', 'artichoke',
           'lemon', 'jackfruit', 'pomegranate', 'broccoli', 'unicycle', 'fireboat', 'cash_machine', 'desktop_computer', 'yurt',
           'croquet_ball', 'vase', 'tricycle', 'tape_player', 'ruler', 'petri_dish', 'cairn_terrier', 'spindle', 'washbasin',
           'king_penguin', 'american_coot', 'prairie_chicken', 'redshank', 'papillon'])

for i in words2:
    print(wn.synsets(i.lower())) 


words3 = list(['peacock', 'axolotl', 'tiger_shark', 'spotted_salamander', 'mud_turtle', 'electric_ray', 'toucan', 'sea_lion',
           'spiny_lobster', 'brain_coral', 'isopod', 'hermit_crab', 'american_lobster', 'pelican', 'borzoi', 'samoyed',
           'oystercatcher', 'chihuahua', 'leopard', 'beagle', 'redbone', 'mantis', 'hare', 'border_terrier', 'jellyfish',
           'indri', 'silky_terrier', 'breastplate', 'guitar', 'harp', 'jigsaw_puzzle', 'maraca', 'saxophone', 'gown', 'milk_can',
           'horizontal_bar', 'moped', 'racer', 'shoji', 'stretcher', 'parachute', 'cheeseburger', 'trifle', 'hotpot', 'pomegranate',
           'fig', 'custard_apple', 'head_cabbage', 'mushroom', 'rugby_ball', 'canoe', 'vending_machine', 'monitor', 'castle', 'puck',
           'printer', 'totem_pole', 'manhole_cover', 'muzzle', 'fire_screen', 'anemone_fish', 'pinwheel', 'coffee_mug', 'bee', 'llama',
           'coucal', 'zebra', 'yorkshire_terrier'])

for i in words3:
    print(wn.synsets(i.lower())) 


words4 = list(['black_grouse', 'cock', 'great_white', 'eft', 'jay', 'tench', 'african_grey', 'black_swan',
           'wallaby', 'jellyfish', 'flatworm', 'chambered_nautilus', 'crayfish', 'bustard', 'italian_greyhound',
           'siberian_husky', 'pomeranian', 'pembroke', 'lynx', 'cougar', 'fly', 'grasshopper', 'angora',
           'fox_squirrel', 'echidna', 'lesser_panda', 'barracouta', 'cauldron', 'flute', 'violin', 'fountain_pen',
           'marimba', 'cornet', 'cloak', 'dome', 'barbell', 'pickup_truck', 'minibus','notebook', 'palace',
           'airliner', 'bagel', 'guacamole', 'cucumber', 'acron_squash', 'orange', 'pineapple', 'granny_smith',
           'cauliflower', 'tandem_bicycle', 'aircraft_carrier', 'dishwasher', 'laptop', 'mountain_tent', 'ping-pong_ball',
           'water_jug', 'tripod', 'cassette_player', 'letter_opener', 'tray', 'kerry_blue_terrier', 'reel',
           'shopping_cart', 'dowitcher', 'ruddy_turnstone', 'ptarmigan', 'european_gallinule', 'japanese_spaniel'])

for i in words4:
    print(wn.synsets(i.lower())) 


words5 = list(['partridge', 'ostrich', 'hammerhead', 'common_newt', 'indigo_bunting', 'goldfish', 'macaw', 'drake', 'wombat',
           'sea_anemone', 'nematode', 'conch', 'spiny_lobster', 'oyster_catcher', 'whippet', 'malamute', 'chow_chow',
           'cardigan', 'persian_cat', 'cheetah', 'ant', 'cricket', 'wood_rabbit', 'guinea_pig', 'skunk', 'giant_panda',
           'sturgeon', 'pail', 'bassoon', 'cello', 'matchstick', 'accordion', 'french_horn', 'poncho', 'beacon', 'dumbbell',
           'minivan', 'fire_engine', 'mortarboard', 'church', 'airship', 'pretzel', 'mashed_potato', 'zucchini', 'artichoke',
           'lemon', 'jackfruit', 'pomegranate', 'broccoli', 'unicycle', 'fireboat', 'cash_machine', 'desktop_computer', 'yurt',
           'croquet_ball', 'vase', 'tricycle', 'tape_player', 'ruler', 'petri_dish', 'cairn_terrier', 'spindle', 'washbasin',
           'king_penguin', 'american_coot', 'prairie_chicken', 'redshank', 'papillon'])

for i in words5:
    print(wn.synsets(i.lower())) 


words6 = list(['plate', 'consomme', 'yawl', 'water_bottle', 'waffle_iron', 'wall_clock', 'teddy_bear', 'table_lamp', 'spotlight', 'space_shuttle', 
           'sombrero', 'soap_dispenser', 'snorkel', 'slide_rule', 'shovel', 'safety_pin', 'rotisserie', 'pill_bottle', 'oxygen_mask', 'obelisk',
           'microwave', 'megalith', 'jinrikisha', 'hourglass', 'dining_table', 'crate', 'chiffonier', 'king_crab', 'flatworm', 'koala', 'bee_eater',
           'robin', 'dungeness_crab', 'black_stork', 'albatross', 'ibizan_hound', 'sealyham_terrier', 'kelpie', 'komondor', 'shetland_sheepdog',
           'border_collie', 'french_bulldog', 'keeshond', 'timber_wolf', 'coyote', 'bassinet', 'bookshop', 'binoculars', 'bow_tie', 'bell_pepper',
           'quail', 'goldfinch', 'pufferfish', 'briard', 'clumber_spaniel', 'leonberg', 'great_pyrenees', 'armadillo', 'persian_cat', 'siamese_cat',
           'apiary', 'sea_cucumber', 'sea_urchin', 'barn', 'maypole', 'cleaver', 'crock_pot', 'goblet'])


for i in words6:
    print(wn.synsets(i.lower())) 