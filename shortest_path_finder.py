import curses
from curses import wrapper
import time
import queue

maze = [
    ["🧱", "🧱", "🍌", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱"],
    ["🧱", " ", " ", " ", " ", " ", "🧱", " ", " ", " ", " ", " ", "🧱", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🧱"],
    ["🧱", " ", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱"],
    ["🧱", " ", " ", " ", "🧱", " ", " ", " ", " ", " ", "🧱", " ", " ", " ", " ", " ", " ", " ", "🧱", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🧱"],
    ["🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱"],
    ["🧱", " ", " ", " ", " ", " ", " ", " ", "🧱", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🧱"],
    ["🧱", " ", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱"],
    ["🧱", " ", "🧱", " ", " ", " ", "🧱", " ", " ", " ", "🧱", " ", " ", " ", "🧱", " ", " ", " ", "🧱", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🧱"],
    ["🧱", " ", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", "🧱", "🧱", " ", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱"],
    ["🧱", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🧱"],
    ["🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", " ", "🧱"],
    ["🧱", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "🧱"],
    ["🧱", "S", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱", "🧱"],
]
def print_maze(maze,stdscr,path=[]):
    BLUE=curses.color_pair(1)
    YELLOW=curses.color_pair(2)

    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,2*j,"👾",BLUE)

            else:    
                stdscr.addstr(i,2*j,value,BLUE)


def find_start(maze,start):
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if value==start:
                return i,j

def find_path(maze,stdscr):
    start="S"
    end="🍌"
    start_pos=find_start(maze,start)
    
    q=queue.Queue()
    q.put((start_pos,[start_pos]))

    visited=set()

    while not q.empty():
        current_pos,path=q.get()
        row,col=current_pos

        if maze[row][col]==end:
            stdscr.clear()
            curses.curs_set(0)
            print_maze(maze,stdscr,path)
            
            stdscr.refresh()
           
            break
        
        stdscr.clear()
        
        curses.curs_set(0)
        print_maze(maze,stdscr,path)
        time.sleep(0.8)
        stdscr.refresh()
    

        neighbours=find_neighbours(maze,row,col)
        for neighbour in neighbours:
            
            if neighbour in visited:
                continue

            r,c=neighbour

            if maze[r][c]=="🧱":
                continue

            new_path=path+[neighbour]
            q.put((neighbour,new_path))
            visited.add(neighbour)


def find_neighbours(maze,row,col):
    neighbours=[]
    if row>0: #up
        neighbours.append((row-1,col))
    if row<len(maze)-1: #down
        neighbours.append((row+1,col))
    if col>0: #left
        neighbours.append((row,col-1))
    if col<len(maze[0])-1:#right
        neighbours.append((row,col+1))
    
    return neighbours
        



def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    
    
    find_path(maze,stdscr)
    stdscr.getch()


wrapper(main)    
