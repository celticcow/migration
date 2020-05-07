#!/usr/bin/python3

"""
Class for representing application data for a group
"""

class appgroup(object):
    """
    """
    ### constructor
    def __init__(self, data_center="lab", eai_num="0", level="lab", comment="this_line_left_blank"):
        self.data_center = data_center
        self.eai_num = eai_num
        self.level = level
        self.comment = comment
        self.name = self.level + "_eai" + self.eai_num + "-" + self.level

    ## Accessor

    def get_name(self):
        return(self.name)

    def get_data_center(self):
        return(self.data_center)

    def get_eai_num(self):
        return(self.eai_num)
    
    def get_level(self):
        return(self.level)
    
    def get_comment(self):
        return(self.comment)

    ## Modifiers

    def set_data_center(self, data_center):
        self.data_center = data_center
    
    def set_eai_num(self, eai_num):
        self.eai_num = eai_num
    
    def set_level(self, level):
        self.level = level
    
    def set_comment(self, comment):
        self.comment = comment


#end of class