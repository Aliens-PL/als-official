from sys import argv, platform
from os import name , path , mkdir , getcwd

possible_cmd = {

    "createproject":
    [
        2,
        1,
        "!project_name",
        "~path",
        # add "~os" if user want to specify which os to run on
    ],

    "update":
    [
        0,
        0,
    ],

    "remove":
    [
        1,
        0,
    ],

    "-help":
    [
        0,
        0,
    ]
    
}


class als(object):

    def __make_tree(self, dic , track_path=None):
        isRoot = False
        for key in dic:
            if track_path == None:
                isRoot = True
                track_path = key

            # file
            if key.startswith('$'):
                print("++ Writing : "+ track_path+self.os_slash+key[1:])
                tmp_file = open(track_path+self.os_slash+key[1:], 'w+')
                tmp_file.write(dic[key])
                tmp_file.close()

            else:        
                if isinstance(dic[key] , list):
                    track_path += self.os_slash+key if not isRoot else ""
                    print("+++ Creating : "+ track_path)
                    mkdir( track_path , self.chmod)

                    for item in dic[key]:
                        if isinstance(item, dict):
                            # Recursivity
                            self.__make_tree(item , track_path)
                        else:
                            print("++ Creating : "+ track_path+self.os_slash+item)
                            mkdir(track_path+self.os_slash+item, self.chmod)
                    
                    if not isRoot :
                        track_path.replace(self.os_slash+key, '')
                        

    def __create_environement(self, project_name , project_path=None):
        if project_path:
            if path.isdir(project_path) == False:
                self.output = "+ Path specified does not exists !"
                self.isDone = False
                return
            else:
                self.path = path.abspath(project_path)+self.os_slash+project_name

        # in case no project path specified we create a new root folder in current dir
        else:
            self.path = path.abspath(project_name)
        
        self.project_name = project_name

        # Main Tree:
        tree = {
            self.path:[
                "wals",
                "mals",
                {
                    project_name+"_conf":
                    [
                        {
                            "$global.als":"""

                            @static
                            Planet global
                            
                                #Which Operating system the project was created on .
                                _$_OS_              = {}


                                # Global {}'s Default Configs

                                
                                # The project path
                                _$_PROJECT_PATH     = {}
                                
                                # The project Name
                                _$_PROJECT_NAME     = {}

                                # Time when the project was created
                                _$_PROJECT_TIME     = {}
                                
                                # Who Created the project
                                _$_PROJECT_OWNER    = {}

                                # For now we set compatibility for all
                                _$_PROJECT_RUN_ON   = {}
                                
                                # By default it's als
                                _$_DEFAULT_TYPE     = {}

                              

                            """.format( 
                                self.os, self.project_name, self.path, self.project_name,
                                self.time, self.user, self.run_on, self.default_type
                            )
                        },
                    ]
                },
                {
                    "$main.als":'''
                        
                        # Hello dear Human !
                        # Since you're here now , You must know that this is space so your earthy rules does not fully applies here !

                        # To make things easier for you , here is some protips :

                        # + As you have already realised , we use # as a secret signal to say that this is a coment / tip
                        
                        # + Our EntryPoint is called space , without it there is no meaning for us !
                        
                        # + We use Variable to store usefull informations as Exmpl : 
                        #       |_ name     = "Dr. JerrAlien"
                        #       |_ my_id    = 1337
                        #       |_ my_bag   = ["APen", "APaper"]
  
                        # + We Also have many Functionalities that we do use .
                        #       |_ We Create them as following : $func_name p1 p2 { ... }
                        #       |_ We Call them using $func_name(v1, v2)
                      
                        # + We also have Galaxies which are a Bunch of Entities , that we load up when needed.
                        #       |
                        #       |_ since you're one from us now , you have the right to build your own Galaxy !

                        # + Our Entities Are called either Planet or IPlanet , depending on our needs
                        #       |
                        #       |_ We've heard some rumors saying that Humans call that class/abstract class
                        
                        # Well , That's more than enough to get you started with , The rest is up to you now to explore .. !
                        # Good luck , fresh Alien !


                        from @als load @als_hello


                        $space()
                        {
                            @als_hello.als_official()
                            $show("Hello Humanity ,\nWe , Aliens also know how to code !")
                        }                    
                    '''
                }
            ]
        }

        try:
            self.__make_tree(tree)
        except FileExistsError:
            self.output = "+ A folder Name with same name already does Exists !"
            self.isDone = False
            return

            
        
                

    def __do_Task(self, name , seq=None):
        print(" + Called : "+ name)
        if seq:
            print("\t|_ with : "+ str(seq)+"\n")
            # for a in seq:
            #     if not a.isalpha():
            #         self.isDone = False
            #         self.output = "\t+ [ "+a+" ] Must be only alphabets !"
            #         return

        if not name.isalpha():
            self.isDone = False
            self.output = "\t+ Project name [ "+name+" ] Must be only alphabets !" 
            return

        # !hardcoded , change it after please.
        if name == 'createproject':
            if possible_cmd[name][0] == seq.__len__():
                self.__create_environement(seq[0], seq[1])
            else :            
                self.__create_environement(seq[0])
        elif name == 'remove':

            abs_dir = getcwd()
                        
            if possible_cmd[name][0] == seq.__len__():
                abs_dir = path.abspath(seq[1])

            curdir = path.split(abs_dir)[-1]
            if path.exists(curdir+"_conf/global.als"):
                __import__("shutil").rmtree(abs_dir, ignore_errors=True)
            else:
                self.isDone = False
                self.output = "+ Invalid ALS directory !"


    # Later we make it work using keyword args (kwargs) better .
    def __init__(self, args):
        self.run_on = 'all'
        self.default_type = 'als'
        #year:month:day:hour:min:sec
        self.time = ':'.join([str(x) for x in __import__('time').localtime()[0:6]])
        # Owner of the project
        try:
            self.user = path.split(path.expanduser('~'))[-1]
        except Exception as ex:
            self.user = "~user"
        
        # Linux slash by default
        self.os_slash = '/' 
        self.isDone = False
        self.output = ""
        # Fedault Project Dir Access rights [r for all Only owner has w access]
        self.chmod  =0o755
        # winxx for windows / linux for linux 
        self.os     = platform
        if self.os is None or self.os == "":
            #nt for windows / posix for linux
            self.os = name

        # Windows a-slash
        if self.os.startswith('win') or self.os == 'nt':
            self.os_slash = '\\' 
        
        args = args[1:]
        args_len = args.__len__()

        if args_len <= 0:
            print("+ No Argument was Speciafied , check -help for more .")
            exit(0)
        
        else:
            self.output = " [ "+args[0] + " ] is not a valid Command , check -help for more infos ."

            for pos , arg in enumerate(args):
                if arg.lower() in possible_cmd.keys():
                    if pos != 0:
                        self.output = " [ "+arg + " ] Must always be placed right after als ."
                        break
                    else:
                        
                        if possible_cmd[arg][0] == 0:
                            self.isDone = True
                            self.__do_Task(arg)
                            break
                        else:
                            possible_sub_cmd_nbr = args_len - 1

                            if  possible_sub_cmd_nbr >= possible_cmd[arg][1]:
                                self.isDone = True
                                self.__do_Task(arg, args[1:])
                                break
                            else:
                                self.output = "+ The command [ "+arg+" ] Needs atleast "+str(possible_cmd[arg][1])+" Arguments ."
                                break

            if self.isDone == False:
                print(self.output)
                exit(-1)




if __name__ == '__main__':
    als(argv)