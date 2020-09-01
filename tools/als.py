#!/usr/bin/python3
from sys import argv, platform , path as sys_path
from os import name , path , mkdir , getcwd
from _core_ import CoreEngine

VERSION = 0.1
HP = """\nManage your aliens project .\n\n> master commands : \n\nals createproject <name-of-project> [<optional-path>]\n\t> Create new aliens project in the specified path if you want   \n\nals update\n\t> Upgrade to latest version\n\nals remove [<optional-repository>]\n\t> Remove the aliens project in current or optional repository\n\nals run [<name.als>]\n\t> Run your space function (space.als)  or  her optional name \n\nals uninstall\n\t> Remove the aliens language from your computer\n"""
possible_cmd = {

    "createproject":
    [
        2,
        1,
        "!project_name",
        "~path",
        # add "~os" if user want to specify which os to run on
    ],

    "run":
    [
        1,
        0,
        "!file_name.als",
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

    "help":
    [
        0,
        0,
    ],

    
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
                    print("++ Creating : "+ track_path)
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
                {
                    "mals":[
                        {
                            "externals":[
                                {"$loads.sals":""}
                            ],
                        }
                    ]
                },
                {
                    
                    project_name+"_conf":
                    [
                        {
"$global.als":f"""

@static
locked planet global
{{


    #Which Operating system the project was created on .
    _$_OS_              = "{self.os}"


    # Global {self.project_name}'s Default Configs


    # The project path
    _$_PROJECT_PATH     = "{self.path}"

    # The project Name
    _$_PROJECT_NAME     = "{self.project_name}"

    # Time when the project was created
    _$_PROJECT_TIME     = "{self.time}"

    # Who Created the project
    _$_PROJECT_OWNER    = "{self.user}"

    # For now we set compatibility for all
    _$_PROJECT_RUN_ON   = "{self.run_on}"

    # By default it's als
    _$_DEFAULT_TYPE     = "{self.default_type}"


}}

                            """
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
#       |_ We Ctreate them as following : $func_name p1 p2 { ... }
#       |_ We Call them using $func_name(v1, v2)

# + We also have Galaxies which are a Bunch of Entities , that we load up when needed.
#       |
#       |_ since you're one from us now , you have the right to build your own Galaxy !

# + Our Entities Are called either Planet or IPlanet , depending on our needs
#       |
#       |_ We've heard some rumors saying that Humans call that class/abstract class

# Well , That's more than enough to get you started with , The rest is up to you now to explore .. !
# Good luck , fresh Alien !


##### EDIT :
# We were out of time , but lexer is fully working and managing almost all the cases .

# Parser is somewhat like 10% done , so  most you see there executing is simply a manual python converting .
# One thing to know , our language is not affected by lower/upper casing either vars , funcs , loads ... everything .

#possible loads : 

# load MyPlanet     # this basically look for a local file in mals folder named MyPlanet.mals
# load @base        # This is out galaxy which has all the builtin stuff .
# from ../path_to_module load MyPlanet
# from http://..../web.mals load MyPlanet # this download the file only once and save it as random_string.mals which will be accessed after directly.

# OOP should always be in a .mals File  

# Defining Function  :
$SayHi _name _prenom 
{
    # if statement
    if(_name == "saad"){
        _name = "SAAD"
    }
    # elif statement
    :(_name == "adil")
    {
        _name = "ADIL" 
    }:(_name == "jamal")
    {
        _name = "JAMAL"
    }
    # else statement
    :{
        _name = "UNKNOWN"
    }

    # range loop
    @loop(1, 5) as x
    {
        _prenom += $Sayhi("MAHMOUD", "TEST")
    }

    # shoud print _name + _prenom12345
    return _name + _prenom
}

# At first we have actually used a sharedlib.so that we have decided to make in C ,
# then load it up to use it from python in order to use some hacky stuff :p
# But that was not the right path to follow especially with the time left .

# We will for sure use that a little later on .

$space
{
    # Please Note that we had no time to actually make it happen , but you can at least feel it ..
    # Winning or loosing the Jam will not affect us from keep pushing it up (for people who find it interesting).

    # normally this is loaded from @als_ a built-in galaxy

    $als_official()
    #$system("ls")
    
    #$out(8*2)
    $out("\\n\\nHello Humanity ,\\nWe , Aliens also know how to code !")

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
                abs_dir = path.abspath(seq[0])

            curdir = path.split(abs_dir)[-1]
            if path.exists(abs_dir+self.os_slash+curdir+"_conf/global.als"):
                __import__("shutil").rmtree(abs_dir, ignore_errors=True)
            else:
                self.isDone = False
                self.output = "+ Invalid ALS directory !"

        elif name == 'run':
            if seq.__len__() >= possible_cmd[name][0] :
                self.__run_transpiler(seq[0])
            else:
                self.__run_transpiler()
        elif name in ['version', '-v', 'v' , 'ver']:
            print(VERSION)
            exit(0)
        
        elif name in ['help', 'h', '-help', '-h']:
            print(HP)
            exit(0)
            
    def __run_transpiler(self , fpath = None):
        if fpath is None:
            fpath = path.join(getcwd(), 'main.als')
        
        fpath = path.abspath(fpath)
        if path.exists(fpath):
            CoreEngine(fpath, '')
            #print("+ Job Done !")
            exit(0)
        else :
            print(f"+ No Such als file exists on the current directory {fpath}")
            exit(0)

    # Later we make it work using keyword args (kwargs) better .
    def __init__(self, args):
        self.run_on = 'all'
        self.default_type = 'als'
        #year:month:day:hour:min:sec
        self.time = ':'.join([str(x) for x in __import__('time').localtime()[0:6]])
        # Owner of the project
        try:
            self.user = path.split(path.expanduser('~'))[-1]

        except Exception:
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
