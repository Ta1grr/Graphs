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