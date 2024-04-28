


def process_revealed_cells(game, ai, move, revealed, HEIGHT, WIDTH, revealed_cells=set()):
    revealed_cells.add(move)
    
    # While the revealed cells is not empty:
    while len(revealed_cells) > 0:
        # move receives the first element of revealed_cells
        move = revealed_cells.pop()
    
        # Loop over all cells within one row and column
        for i in range(move[0] - 1, move[0] + 2):
            for j in range(move[1] - 1, move[1] + 2):

                # Ignore the cell itself
                if (i, j) == move:
                    continue

                # Reveal and add to ai knowledge
                if 0 <= i < HEIGHT and 0 <= j < WIDTH and (i, j) not in revealed and (i, j) not in revealed_cells:
                    nearby = game.nearby_mines((i,j))
                    revealed.add((i,j))
                    ai.add_knowledge((i,j), nearby)
                    
                    if nearby == 0 and (i,j):
                        revealed_cells.add((i,j))
        
    return game, ai, revealed