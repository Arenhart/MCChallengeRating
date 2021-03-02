# -*- coding: utf-8 -*-
"""
01/03/2021
@author: Rafael Arenhart
"""

import numpy as np

SAVES = ['fort', 'ref', 'will']
SKILLS = ['appraise', 'balance', 'bluff', 'climb', 'concentration', 'craft', 'decipher script', 'diplomacy', 'disable device', 'disguise', 'escape artist', 'forgery', 'gather information', 'handle animal', 'heal', 'hide', 'intimidadate', 'jump', 'knowledge', 'liseten', 'move silently', 'open lock', 'perform', 'profession', 'ride', 'search', 'sense motive', 'sleight of hand', 'spellcraft', 'spot', 'survival', 'swim', 'tumble', 'use magic device', 'use rope']
ATTRIBUTES = ('STR','DEX','CON','INT','WIS','CHA')
OTHER_PROPERTIES = ('name', 'bab', 'ca', 'hp', 'speed')

def roll(roll):
    if '+' in roll:
        roll, mod = roll.split('+')
        mod = int(mod)
    elif '-' in roll:
        roll, mod = roll.split('-')
        mod = -int(mod)
    else:
        mod = 0
    dice_num, dice_sides = roll.split('d')
    dice_num = int(dice_num)
    dice_sides = int(dice_sides)
    return np.random.randint(1, dice_sides+1, dice_num).sum() + mod
    
def attribute_mod(value):
    return (value - 10) // 2