

#---TO DO--------------------------------------------------------------------------------#

#- Replace f_call_fixer => Call bin->fixer/updater to fix the last exception loged/cached

#----------------------------------------------------------------------------------------#


class Cfg(object):
    """+ Will Check and Load cfg file
    + Parse the content to bytes (short)
    + Get them ready along with the file content to be sent to the extern function
    """
    def __init__(self):
        flag_sep = 0x01
        print("+ Starting __C ")
        self.maped = []
        try:
            self.cfg = open("__c.cfg").readlines()
            assert self.cfg != None , "[ERR] File __c.cfg is Missing or Broken !" #f_call_fixer

            for i,line in enumerate(self.cfg):
                # flag must start with either _ or .
                if line[0] in ['.', '_']:
                    splited_line = line.split(' ')
                    
                    assert splited_line.__len__() == 2 , "[ERR] File __c.cfg is Broken !" #f_call_fixer
                    self.maped.append(splited_line[0]+chr(flag_sep))
                    _tmp_len = splited_line[1].replace('\n','').__len__()

                    assert _tmp_len > 0 , "[ERR] File __c.cfg is Broken !" #f_call_fixer
                    assert _tmp_len % 2 == 0 ,str(_tmp_len)+"[ERR] File __c.cfg is Broken !" #f_call_fixer

                    pos = 0
                    while pos < _tmp_len:
                        self.maped[i] += chr(int(splited_line[1][pos]+splited_line[1][pos+1], 16))
                        pos += 2  


                else:
                    #f_call_fixer
                    raise Exception("Failed Checking cfg's signatures !")

        except Exception as ex:
            print(str(ex))
            exit(0)
    
    def get_cfg(self):
        return self.maped
