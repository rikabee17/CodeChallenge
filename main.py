import numpy as np

def get_coord(index,array):
    for i in range(8):
        for j in range(9):
            if j <= 7:
                position=array[i][j]
                if position==index:
                    return i,j # i=asse x | j=asse y
            else:
                j=0
                continue  

class cell:
 
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

def isInside(x, y, N):
    if (x >= 1 and x < N and
            y >= 1 and y < N):
        return True
    return False

def move_current_office(int_starting_position, int_end_position):

    lst_current_office = [
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    ["A", "M", " ", "A", "M", " ", "A", "M"],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    ["A", "M", " ", "A", "M", " ", "A", "M"],
    [" ", "M", "C", " ", "M", "C", " ", "M"]
]
    lst_index = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31],
    [32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47],
    [48, 49, 50, 51, 52, 53, 54, 55],
    [56, 57, 58, 59, 60, 61, 62, 63]
]
    array_index=np.array(lst_index)
    array_current_office=np.array(lst_current_office)
    N = 8 

    starting_axis=get_coord(int_starting_position,array_index)
    end_axis=get_coord(int_end_position,array_index)

    # all possible movements for the knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
 
    queue = []
 
    # push starting position of knight
    # with 0 distance
    queue.append(cell(starting_axis[0], starting_axis[1], 0))
 
    # make all cell unvisited
    visited = [[False for i in range(N+1)]
               for j in range(N+1)]
 
    # visit starting state
    visited[starting_axis[0]][starting_axis[1]] = True
 
    # loop until we have one element in queue
    while(len(queue) > 0):
 
        t = queue[0]
        queue.pop(0)

        if(t.x == end_axis[0] and t.y == end_axis[1]):
            return t.dist
        
        for i in range(8):
            
            x = t.x + dx[i]
            y = t.y + dy[i]

            if(isInside(x, y,N) and not visited[x][y] and check_current_position(array_current_office[x][y]) == True):
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))
                
    else:
        return np.inf
    

def check_position(starting_office,end_office):
    if starting_office and end_office == ' ':
        return True
    else:
        return False
    
def check_current_position(current_office):
    if current_office == ' ':
        return True
    else:
        return False

def main():
    lst_current_office = [
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    ["A", "M", " ", "A", "M", " ", "A", "M"],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    ["A", "M", " ", "A", "M", " ", "A", "M"],
    [" ", "M", "C", " ", "M", "C", " ", "M"]
]
    lst_index = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31],
    [32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47],
    [48, 49, 50, 51, 52, 53, 54, 55],
    [56, 57, 58, 59, 60, 61, 62, 63]
]
    array_index=np.array(lst_index)
    array_current_office=np.array(lst_current_office)

    int_starting_position = 24 #input
    int_end_position = 62 #input

    starting_axis_X = get_coord(int_starting_position,array_index)[0]
    starting_axis_y= get_coord(int_starting_position,array_index)[1]

    end_axis_X = get_coord(int_end_position,array_index)[0]
    end_axis_y= get_coord(int_end_position,array_index)[1]

    starting_office=array_current_office[starting_axis_X][starting_axis_y] #str
    end_office=array_current_office[end_axis_X][end_axis_y] #str
    
    # check_position(starting_office,end_office)
    if check_position(starting_office,end_office)==False:
        print(np.nan)
    else:
        print(move_current_office(int_starting_position,int_end_position))

if __name__ == '__main__':
    main()
