import time

class Agent:

    """
        initialize some member variables
    """
    def __init__(self):
        self.player_row = 0
        self.player_col = 0
        self.level_matrix = None
        self.elapsed_solve_time = 0

        """
            please use these variables for statistics
        """
        self.expanded_node_count = 0
        self.generated_node_count = 0
        self.maximum_node_in_memory_count = 0

        #  not implemented, not necessary
        self.real_distance_matrix = []
        self.manhattan_distance_matrix = []
    


    """
        returns REAL manhattan distance between two points in the level.
    it is the amount of steps required from going point 1 to point 2, 
    so it also consider walls.
    row_1 and col_1 is the position of first point
    row_2 and col_2 is the position of second point 

        this function is not necessary, you may leave it empty
    """
    def real_distance(self, row_1, col_1, row_2, col_2):
        raise NotImplementedError
    


    """
        level_matrix is list of lists (like 2d array)
    that contains whether a particular cell is
    -A (apple)
    -F (floor)
    -P (player)
    -W (wall)

    level_matrix[0][0] is top left corner
    level_matrix[height-1][0] is bottom left corner
    level_matrix[height-1][width-1] is bottom right corner

        player_row and player_column are current position
    of the player, eg:
    level_matrix[player_row][player_column] supposed to be P
      
        returns a character list, list of moves
    that needs to be played in order to solve
    given level
    valid letters are R, U, L, D corresponds to:
    Right, Up, Left, Down
    an example return value:
    L = ["U", "U", "U", "L", "R", "R"]...
    """
    def solve(self, level_matrix, player_row, player_column):
        self.player_row = player_row
        self.player_col = player_column
        self.level_matrix = level_matrix

        #  you may precompute distances between pairs of points here

