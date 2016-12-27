# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 16:08:11 2016

@author: Thomas
"""

import soco

def keepVolumeLow(n_decibels):
    """
    I am bored with people putting the music loud in the office.
    This is my revenge. 
    """    
    
    try:
        speakers = list(soco.discover())
    except Exception:
        return print("No Sonos in there. What a relief.")
    
    Me_at_work = True
    
    while Me_at_work:
        try:
            for i in range(len(speakers)):
                speakers[i].volume = n_decibels
                
        except Exception:
            speakers = list(soco.discover())
