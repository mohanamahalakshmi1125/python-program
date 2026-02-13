def cellCompete(cells, days):
    for d in range(days):
        newCells = [0]*8
        for i in range(1, 7):
            if cells[i-1] == cells[i+1]:
                newCells[i] = 1
            else:
                newCells[i] = 0
        cells = newCells
    return cells

# Example
cells = [1,0,0,0,0,1,0,0]
days = 2

print(cellCompete(cells, days))
