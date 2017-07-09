# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:17:11 2017

@author: Shahriar Kabir
"""

class Meat(object):
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice(object):
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False
            
class Beans(object):
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False

class Burrito(object):
    
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = Meat(meat)
        self.set_to_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)
    
    def get_rice(self):
        return self.rice.get_value()
    
    def get_meat(self):
        return self.meat.get_value()
    
    def get_beans(self):
        return self.beans.get_value()
    
    def get_to_go(self):
        return self.to_go
    
    def get_extra_meat(self):
        return self.extra_meat
    
    def get_guacamole(self):
        return self.guacamole
    
    def get_cheese(self):
        return self.cheese
    
    def get_pico(self):
        return self.pico
    
    def get_corn(self):
        return self.corn
    
    def set_rice(self, rice):
        self.rice.set_value(rice)
        
    def set_meat(self, meat):
        self.meat.set_value(meat)
    
    def set_beans(self, beans):
        self.beans.set_value(beans)
    
    def set_to_go(self, to_go):
        if to_go in [True, False]:
            self.to_go = to_go
    
    def set_extra_meat(self, extra_meat):
        if extra_meat in [True, False]:
            self.extra_meat = extra_meat
   
    def set_guacamole(self, guacamole):
        if guacamole in [True, False]:
            self.guacamole = guacamole
    
    def set_cheese(self, cheese):
        if cheese in [True, False]:
            self.cheese = cheese
    
    def set_pico(self, pico):
        if pico in [True, False]:
            self.pico = pico
    
    def set_corn(self, corn):
        if corn in [True, False]:
            self.corn = corn
            
    def get_cost(self):
        base = 5
        if self.meat.get_value() in ["chicken", "pork", "tofu"]:
            base += 1
        elif self.meat.get_value() == 'steak':
            base += 1.5
        if self.get_extra_meat() and bool(self.meat.get_value()):
            base += 1
        if self.get_guacamole():
            base += 0.75
        return base
    
    def __sub__(self, other):
        return self.get_cost() - other.get_cost()

def total_cost(bur_list):
    su = 0
    for burrito in bur_list:
        su += burrito.get_cost()
    return su