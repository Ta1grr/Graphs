Step 1: Understanding the problem
 - User always start at coordinate (0, 0)
 - Traverse through every single room and record every movement
 
Step 2: Make a plan
 - Use BFS(Breadth First Search) to check every direction are not null (nearest node)
 - Depth First Search to traverse
    - Possibly use recursion if there are multiple route.
    - If recursion end then router back from fork. (Possibly slice from fork and reverse the answer)
 - Keep a way to keep track if room has been visited
 - Compare if visited length is same as length of rooms.

 Three commands to use
    - player.currentRoom.id
    - player.currentRoom.getExits()
    - player.travel(direction)

 Note: DFS to Build path, BFS to find nearest unexplored room.

 traversalPath = []

graph = {}

print("Player current room id:", player.currentRoom.id)
print("Player exits:", player.currentRoom.getExits())

inverse_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# Assign the id of the room player is currently in
current_room_id = player.currentRoom.id
# Assign players exits to room_exits
room_exits = player.currentRoom.getExits()

print("room exits:", room_exits) #room exits: ['n']

exits_dictionary = {}
for exit in room_exits:
    exits_dictionary[exit] = '?'

print("Exits_dictionary:", exits_dictionary) #Exits_dictionary: {'n': '?'}

# Adding in the current id as the key and assigning exits_dictionary as the value.
graph[current_room_id] = exits_dictionary

print("graph:", graph) #{0: {'n': '?'}}

# ----------  Step1  ------------
print(" -- Room 1 --")
direction_to_travel = 'n'

#assigning current room to previous room
previous_room_id = current_room_id

print("previous room id:", previous_room_id) #previous room id: 0

#Move player to direction_to_travel, which in this case is N
player.travel(direction_to_travel)

#Reassigned current_room_id to player.currentRoom.id
current_room_id = player.currentRoom.id

print("Current room id:", current_room_id) #Current room id: 1

#Reassigned room_exits to be room id 1 exits
room_exits = player.currentRoom.getExits()

#Remap exits_dictionary to show current room exits
exits_dictionary = {}
for exit in room_exits:
    exits_dictionary[exit] = '?'

print("room 1 exits:", exits_dictionary) #room 1 exits: {'n': '?', 's': '?'}

# Adding in the current room (room 1) as key and assign exits_dictionary as the value
graph[current_room_id] = exits_dictionary

print("graph:", graph) #graph:{0: {'n': '?'}, 1: {'n': '?', 's': '?'}}

# Assign inverse_direction to be the inverse of direction_to_travel, which will take 'n' for the key to get the value of 's' from inverse_directions
inverse_direction = inverse_directions[direction_to_travel]

print("inverse direction:", inverse_direction) #inverse direction: s

# Assigning previous_room_id (0) and the direction_to_travel (n) inside of it to current_room_id (1)
graph[previous_room_id] [direction_to_travel] = current_room_id

print("graph of room1:", graph) #graph of room1: {0: {'n': 1}, 1: {'n': '?', 's': '?'}}

# Assigning [current_room_id] (1) with the inverse_direction (s) to previous_room_id (0)
graph[current_room_id] [inverse_direction] = previous_room_id

print("graph of room1:", graph) #graph of room1: {0: {'n': 1}, 1: {'n': '?', 's': 0}}

print("Player current room id:", player.currentRoom.id)
print("Player exits:", player.currentRoom.getExits())


# -- Step 2 ---
print(" -- Room 2 --")
direction_to_travel = 'n'

#assigning current room to previous room
previous_room_id = current_room_id

print("previous room id:", previous_room_id) #previous room id: 0

#Move player to direction_to_travel, which in this case is N
player.travel(direction_to_travel)

#Reassigned current_room_id to player.currentRoom.id
current_room_id = player.currentRoom.id

print("Current room id:", current_room_id) #Current room id: 1

#Reassigned room_exits to be room id 1 exits
room_exits = player.currentRoom.getExits()

#Remap exits_dictionary to show current room exits
exits_dictionary = {}
for exit in room_exits:
    exits_dictionary[exit] = '?'

print("room 1 exits:", exits_dictionary) #room 1 exits: {'n': '?', 's': '?'}

# Adding in the current room (room 1) as key and assign exits_dictionary as the value
graph[current_room_id] = exits_dictionary

print("graph:", graph) #graph:{0: {'n': '?'}, 1: {'n': '?', 's': '?'}}

# Assign inverse_direction to be the inverse of direction_to_travel, which will take 'n' for the key to get the value of 's' from inverse_directions
inverse_direction = inverse_directions[direction_to_travel]

print("inverse direction:", inverse_direction) #inverse direction: s

# Assigning previous_room_id (0) and the direction_to_travel (n) inside of it to current_room_id (1)
graph[previous_room_id] [direction_to_travel] = current_room_id

print("graph of room1:", graph) #graph of room1: {0: {'n': 1}, 1: {'n': '?', 's': '?'}}

# Assigning [current_room_id] (1) with the inverse_direction (s) to previous_room_id (0)
graph[current_room_id] [inverse_direction] = previous_room_id

print("graph of room1:", graph) #graph of room1: {0: {'n': 1}, 1: {'n': '?', 's': 0}}

print("Player current room id:", player.currentRoom.id)
print("Player exits:", player.currentRoom.getExits())

print(graph[current_room_id]['s']) #To check through the current room direction list to see if there are question marks

#                                        #
#                002                     #
#                 |                      #
#                 |                      #
#                001                     #
#                 |                      #
#                 |                      #
#                000                     #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #
#                                        #

Player current room id: 0
Player exits: ['n']
room exits: ['n']
Exits_dictionary: {'n': '?'}
graph: {0: {'n': '?'}}
 -- Room 1 --
previous room id: 0
Current room id: 1
room 1 exits: {'n': '?', 's': '?'}
graph: {0: {'n': '?'}, 1: {'n': '?', 's': '?'}}
inverse direction: s
graph of room1: {0: {'n': 1}, 1: {'n': '?', 's': '?'}}
graph of room1: {0: {'n': 1}, 1: {'n': '?', 's': 0}}
Player current room id: 1
Player exits: ['n', 's']
 -- Room 2 --
previous room id: 1
Current room id: 2
room 1 exits: {'s': '?'}
graph: {0: {'n': 1}, 1: {'n': '?', 's': 0}, 2: {'s': '?'}}
inverse direction: s
graph of room1: {0: {'n': 1}, 1: {'n': 2, 's': 0}, 2: {'s': '?'}}
graph of room1: {0: {'n': 1}, 1: {'n': 2, 's': 0}, 2: {'s': 1}}
Player current room id: 2
Player exits: ['s']
1
TESTS FAILED: INCOMPLETE TRAVERSAL
2 unvisited rooms