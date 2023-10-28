import unittest
import sys
sys.path.insert(1,"C:/Users/y/Desktop/GOTHONS")
from gothonweb.planisphere import *

class RoomTest(unittest.TestCase):
    """Testing class Room"""

    def SetUp(self):
        Room
        MoreRooms
    def test_room(self):
        gold = Room("GoldRoom",
        """This room has gold in it you can grab. There`s a
        door to the north.""")
        self.assertEqual( gold.name,"GoldRoom")
        self.assertEqual( gold.paths,{})

    def test_room_paths(self):
        center=Room("Center", "Test room is the center.")
        north =Room("North", "Test room is the north.")
        south=Room("South","Test room is the south.")

        center.add_paths({'north':north, 'south':south})
        self.assertEqual(center.go('north'), north)
        self.assertEqual (center.go('south'),south)

    def test_map(self):
        start=Room("Start", "You can go west down a hole.")
        west=Room("Trees", "There are trees here, you can go east.")
        down=Room("Dungeon", "It`s dark down here, you can go up.") 
     
        start.add_paths({'west':west, 'down': down})
        west.add_paths({'east': start})
        down.add_paths({'up': start})

        self.assertEqual (start.go('west'),west)
        self.assertEqual (start.go('west').go('east'),start) 
        self.assertEqual (start.go('down').go('up'), start)

    def test_gothon_game_map(self):
        start_room=load_room(START)
        self.assertEqual( start_room.go('shoot!'),generic_death)
        self.assertEqual( start_room.go('dodge!'),generic_death)
    
        room=start_room.go('tell_a_joke')
        self.assertEqual( room,laser_weapon_armory)

if __name__=="__main__":
    unittest.main()