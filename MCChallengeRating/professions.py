# -*- coding: utf-8 -*-
"""
01/03/2021
@author: Rafael Arenhart
"""

from MCChallengeRating.utils import SAVES

class Level():

    def __init__(self, profession, level, modifiers, conditions, actions):
        self.profession = profession
        self.level = level
        self.modifiers = modifiers
        self.conditions = conditions
        self.actions = actions


class Profession():

    def __init__(self, character):
        self.levels = []
        self.character = character
        
        
class Fighter(Profession):
    profession_skills = ['climb', 'craft', 'handle animal', 'intmidate', 'jump', 'ride', 'swim']
    proficeincies = ['simple', 'martial', 'light', 'medium', 'heavy', 'shield']
    skills_per_level = 2
    hp_per_level = (10, 5, 6)
    bab = 'high'
    saves = ['fort']
    
    def __init__(self):
        super().__init__()
        
    def level_up(self):
        modifiers = {}
        conditions = []
        actions = []
        next_total_level = self.character.get_level()
        next_profession_level = len(self.levels) + 1
        
        # increase hp
        if next_total_level == 1:
            modifiers['hp'] = self.__class__.hp_per_level[0]
        elif (next_total_level % 2) == 0:
            modifiers['hp'] = self.__class__.hp_per_level[1]
        else:
            modifiers['hp'] = self.__class__.hp_per_level[2]
        
        # increase saves
        if next_profession_level == 1:
            for save in self.__class__.saves:
                modifiers[save] = 2
        if (next_profession_level % 2) == 0:
            for save in self.__class__.saves:
                modifiers[save] = 1
        if (next_profession_level % 3) == 0:
            for save in SAVES:
                if save not in self.__class__.saves:
                    modifiers[save] = 1
                    
        # increase attributes
        if (next_total_level % 4) == 0:
            skill = self.character.choose_skill()
            modifiers[save] = 1
            
        # increase skills
        multiplier = 4 if (next_total_level == 1) else 1
        skills_per_level = character.get_property['skills per level'] + self.__class__.skills_per_level
        new_skills = self.character.choose_skills(multiplier * skills_per_level, self.__class__.profession_skills)
        modifiers.update(new_skills)
        
        # increase feats
        if ((next_total_level % 3) == 0) or (next_total_level == 1):
            modifiers['feats'] = 1   
        
        # increase bab
        if self.__clas__.bab == 'high':
            modifiers['bab'] = 1
        if self.__clas__.bab == 'medium':
            if (2*next_profession_level) %3 != 2:
                modifiers['bab'] = 1
        if self.__clas__.bab == 'low':
            if next_profession_level % 2 != 0:
                modifiers['bab'] = 1
        
        new_level = (self, next_total_level, modifiers, conditions, actions)
        
        
    
        