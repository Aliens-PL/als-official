

class __c:

    def __init__(self):
        try:
            self.cfg = open("__c.cfg").read()
            assert self.cfg != None , "[ERR] File __c.cfg is Missing or Messed up !"
            self.mapped = [for ]
        except Exception as ex:
            print(str(ex))
        