def print_matrix(matrix):
    print("---------")
    for row in matrix:
        print("| ", end="")
        for s in row:
            print(s, end=" ")
        print("|")
    print("---------")

def check(matrix):
    x_num = 0
    o_num = 0
    for row in range(3):
        for cell in matrix[row]:
            if cell == 'X':
                x_num += 1
            elif cell == 'O':
                o_num += 1
      
    x_line = 0
    o_line = 0
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != '_':
            if matrix[i][0] == 'X':
                x_line += 1
            else:
                o_line += 1
        
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != '_':
            if matrix[0][i] == 'X':
                x_line += 1
            else:
                o_line += 1
    
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != '_':
        if matrix[1][1] == 'X':
            x_line += 1
        else:
            o_line += 1
    
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != '_':
        if matrix[1][1] == 'X':
            x_line += 1
        else:
            o_line += 1    
    
    print(x_line, o_line)
                
    if abs(x_num - o_num) > 1 or (x_line + o_line) > 1:
        return "Impossible"
    elif x_line == 1:
        return True, "X wins"
    elif o_line == 1:
        return True, "O wins"
    elif x_num + o_num == 9:
        return True, "Draw"
    else:
        return False, "Game not finished"
    
    
def make_move(coord_string, X_turn):
    coordinates = coord_string.split()
    if len(coordinates) != 2:
        print("You should enter numbers!")
        return False
    try:
        row, col = 3 - int(coordinates[1]), int(coordinates[0]) - 1, 
        print(coordinates, row, col)
    except ValueError:
        print("You should enter numbers!")
        return False     
        
    if row > 2 or row < 0 or col > 2 or col < 0:
        print("Coordinates should be from 1 to 3!")
        return False
    
    global matrix
    if matrix[row][col] != '_':
        print("This cell is occupied! Choose another one!")
        return False
    else:
        matrix[row][col] = 'X' if X_turn else 'O'
        return True
    
    
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append('_')
print_matrix(matrix)

finished = False
message = ''
X_turn = True
while not finished:
    moved = False
    while not moved:
        coord_string = input("Enter the coordinates: ")
        moved = make_move(coord_string, X_turn)
    X_turn = not X_turn
    print_matrix(matrix)
    
    finished, message = check(matrix)

print(message)
