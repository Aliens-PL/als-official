

#---TO DO---#

# Replace f_call_fixer => Call bin->fixer/updater to fix the last exception loged/cached

#-----------#


class __c:
    """+ Will Check and Load cfg file
    + Parse the content to bytes (short)
    + Get them ready along with the file content to be sent to the extern function
    """
    def __init__(self):
        self.maped = []
        try:
            self.cfg = open("__c.cfg").readlines()
            #f_call_fixer
            assert self.cfg != None , "[ERR] File __c.cfg is Missing or Broken !"
            
            for i,line in enumerate(self.cfg):
                # flag must start with either _ or .
                if line[0] in ['._']:
                    splited_line = line.split(' ')
                    #f_call_fixer
                    assert splited_line.__len__() == 2 , "[ERR] File __c.cfg is Broken !"
                    self.maped.append(splited_line[0])
                    for j, each in enumerate(splited_line[1]):
                        
                else:
                    #f_call_fixer
        except Exception as ex:
            print(str(ex))
        