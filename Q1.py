import queue
def Maze_create():
    maze = []
    #maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#", "S", "#", " ", " ", " ", " ", "#", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", " ", "#", "#"])
    maze.append(["#", " ", "#", " ", "#", "G", " ", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", "#", " ", "#", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", " ", "#", "#"])
    maze.append(["#", "#", "#", " ", " ", " ", " ", "#", "#"])
    #maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#"])
    return maze

def maze_print(maze, path = ""):
    for x, pos in enumerate(maze[0]):
        if pos == "G":
            start = x
    i = start
    j = 0
    pos = set()
    for move in path:
        if move =="A":
            i -= 1
        elif move == "B":
            i+=1
        elif move == "C":
            j -= 1
        elif move == "D":
            j += 1
        pos.add((j,i))
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if(j, i) in pos:
                print("+", end="")
            else:
                print(col + "", end= "")
        print()

def validation(maze, moves):
    start = None
    if start is None:
        return False
    for x, pos in enumerate(maze[0]):
        if pos =="G":
            start = x
    
    i = start
    j = 0
    for move in moves:
        if move == "A":
            i -= 1
        elif move == "B":
            i += 1
        elif move == "C":
            j -= 1
        elif move == "D":
            j += 1

        elif (maze[j][i] == '#'):
            return False
    return True

def end_maze(maze, moves):
    start = None
    if start is None:
        return False
    for x, pos in enumerate(maze[0]):
        if pos == "G":
            start = x
    
    i = start
    j = 0
    for move in moves:
        if move == "A":
            i -= 1
        elif move == "B":
            i+= 1
        elif move == "C":
            j -= 1
        elif move == "D":
            j += 1
    if maze[j][i] == "S":
        print("Found: " + moves)
        maze_print(maze, moves)
        return True
    return False

maze_run = queue.Queue()
maze_run.put(" ")
add = ""
maze = Maze_create()

while not end_maze(maze, add):
    add = maze_run.get()
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if validation(maze, put):
            maze_run.put(put)

