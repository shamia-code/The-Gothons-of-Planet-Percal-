class Room(object):
    
    def __init__(self, name,description):
        self.name = name
        self.description = description
        self .paths = {}
    def __get__(self,name,description):
        print(self.description)
             
    def go(self,direction):
 
        path=self.paths.get(direction,self.paths.get('*'))
        
        print(path.description)
        """for k,v in self.paths.items():
            if k in self.paths.keys() and path==k:
                print(v.description)
                return v
            """ 
        return path.next_room

    def add_paths(self,paths):
   
        return self.paths.update(paths)

central_corridor=Room('central Corridor',
"""The Gothons of Planet Percal #25 have invaded your ship and 
destroyed your entire crew. You are the surviving 
member and your last mission is to get the neutron destruct 
bomb from the Weapons Armory , put it in the bridge , and 
blow the ship up after getting into an escape pod.
        
you`re running down the central corridor to the Weapons 
Armory when a Gothon jumps out, red scaly skin , dark grimy
teeth, and evil clown costume flowing around his hate 
filled body. He`s blocking the door to the Armory and
about to pull a weapon to blast you. 
""")

laser_weapon_armory=Room('Laser Weapon Armory',
"""Lucky for you they made you learn Gothon insults in 
the academy. You tell the one Gothon joke you know :
Lhsdf gfwey ncbbdf gf,uyerw ucbefds dudhh  ewafi gur ubrr,
kur sketw beqhe kus isnafd. The Gothon stops, tries 
not to laugh, then busts out laughing  and can`t move.
While he`s laughing you run up and shoot him square in
the head putting him down , then jump through the 
Weapon Armory door.

You do a dive roll into the Weapon Armory , crouch and scan
the room for more Gothons that might be hiding. Tt`s dead
quiet, too quiet. you stand up and run to the far side of 
the room and find the neutron bomb in it`s container.
There`s a keypad lock on the box and you need the code to 
get the bomb out. If you get the code wrong 10 times then
the lock closes forever and you can`t get the bomb. The
code is 1 digits. 
""")

the_bridge=Room('The Bridge',
"""The container clicks open and the seal breaks, letting
gas out. You grab the neutron bomb and run as fast as 
you can to the bridge where you must place it in the 
right spot.

You burst onto the bridge with the neutron destruct bomb
under your arm and surprise 5 Gothons who are trying 
to take control of the ship. each of them has an even uglier 
clown costume than the last. They haven`,t pulled their 
weapons out yet, as they see the active bomb under your 
arm and don`t want to set it off.
""")

escape_pod=Room("Escape Pod",
"""You point your blaster at the bomb under your arm and
the Gothons put their hands up and start to sweat.
You inch backward to the door , open it , and then 
carefully place the bomb on the floor, pointing your 
blaster at it. You then jump back through the door, 
punch the close button and blast the lock so the 
Gothons can`t get out. Now that the bomb is placed 
you run to the escape pod to get off this tin can.

You rush through the ship desperately trying to make it to 
the escape pod before the  whole ship explodes. It seems 
like hardly any Gothons are on the ship, so your run is 
clear of interference. You get to the chamber with the 
escape pods, and now need to pick one to take. Some of 
them could be damaged but you don`t have time to look.
There`s 5 pods , which one do you take?           
""")

the_end_winner=Room("The End",
"""You jump into pod 2 and hit the eject button .
The pod easily slides out into space heading to the 
planet below. As it flies to the planet, you look 
back and see your ship implode then explode like a 
bright star, taking out the Gothon ship at the same 
time. You won !
""")

the_end_loser=Room("The End",
""""You jump into pod 2 and hit the eject button.
The pod escapes out into the void of space, then 
implodes as the hull ruptures, crushing your body into 
jam jelly.
""")

generic_death=Room("death","You died")



class Path:
    def __init__(self,description,next_room):
        self.description=description
        self.next_room=next_room

    
the_informery=Room('Weapons',"""This is the informery room""")

northpath=Path("""
Quick on the draw you yank out your blaster and fire 
it at the Gothon.  His clown costume is flowing and 
moving around his body, which throws off your aim.
Your laser hits his costume but misses him entirely.
This completely ruins his brand new costume his mother 
bought him, which makes him fly into an insane  rage .He
strikes at once,and you pierce right through his heart
and he dies. 
""", laser_weapon_armory)

southpath=Path("""
Like a world class boxer you dodge, weave , slip and 
slide right as the Gothon`s blaster cranks a laser 
past your head. In the middle of your artful dodge 
your foot slips and you bang your head on the metal
wall and pass out. You wake up shortly after only to
die as the Gothon stomps on your head and eats you.
""",central_corridor)


westpath=Path("""
The lock buzzes one last time and then you hear a 
sickening melting sound as the mechanism is fused 
together. You decide to sit there, and finally the 
Gothons blow up the ship  from their ship and you die.""",
escape_pod  )

eastpath=Path("""
In a panic you throw the bomb at the group of Gothons 
and make a leap for the door. Right as you drop it a 
Gothon shoots you right in the back killing you. As 
you see another Gothon frantically try to 
disarm the bomb.""",the_bridge
)

#paths for the central corridor
path_to_armory=Path("""description of what happens when player is in central corridor and 
chooses the weapon armory""", laser_weapon_armory)

path_to_bridge=Path(""""description of what happens when player in central coridor and chooses bridge""", the_bridge)

#paths for the laser weapon armory

back_to_corridor=Path("""description of what happens when player in armory and
chooses to go back to central corridor""",central_corridor)

the_informery.add_paths({
    'direction1':northpath,
    'direction2':path_to_bridge

})




escape_pod.add_paths({
    '2':the_end_winner,
    '*':the_end_loser,
    'east':eastpath
})
#making generic_death ,the catch-all action 

the_bridge.add_paths({
    'throw the bomb':generic_death,
    'slowly place the bomb':escape_pod,
    '*':generic_death,
    'north':northpath,
    'south':southpath

})

laser_weapon_armory.add_paths({
    '0132':the_bridge,
    '*':generic_death,
    'door3':path_to_bridge,
    'door4':back_to_corridor
})

central_corridor.add_paths({
    'shoot!':generic_death,
    'dodge!':generic_death,
    'tell a joke':laser_weapon_armory,
    '*':generic_death,
    'door1':path_to_bridge,
    'door2':path_to_armory

})


class  Engine(Room,Path):
     
    def __init__(self,name,description,next_room):
        super(Engine,self).__init__(name,description)
        super(Engine,self).__init__(description,next_room)
        self.name=name
        self.next_room=next_room
        self.description=description
        self.started=False 
    def load_room(self,start_room):
        """There is a potential security problem here.
        Who gets to set name? Can that expose a variable?
        """
        return start_room
    #def go(self,direction):
    
    def play(self):
        start=central_corridor or the_informery 
        self.started=True
        
         
        if start  in ['central_corridor','the_informery']:
            return start 
        self.load_room(start) 
     
            
        print(start.description) 
         
        path_choice=input("path>")
        path=start.go(path_choice)
        
        while path.next_room!=generic_death or path['2']:
            print(path.next_room.description)
            path_choice
            path.next_room.go(path_choice)
            if path.next_room==generic_death:
                print(path.next_room.description)
                print("YOU DIED !")
            if path.next_room==path['2']:
                print(path.next_room.description)
                print("CONGRATULATIONS, YOU WON !")

game=Engine("shamie","""description""","nextroom")
start=input('start_map>')
game.play()


