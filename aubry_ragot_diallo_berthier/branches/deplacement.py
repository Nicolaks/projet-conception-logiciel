def pos_hero(grid):#fonction qui retrouve la position du hero
    h,l = len(grid), len(grid[0])
    for i in range(h):
        for j in range(l):
            if i == "1":
                return [i,j] #Position du hero

def deplacement_gauche(grid, pos_hero):
    h,l = len(grid), len(grid[0])
    i = pos_hero[0]
    j = pos_hero[1]
    if i != 0:
        grid[i][j] = ' - '