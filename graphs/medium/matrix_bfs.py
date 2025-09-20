

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])

        res = 0 
        q = deque([(0,0)])   
        visit = set((0,0))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q: 

            for i in range(len(q)):

                x,y = q.popleft()   
                if x == ROWS - 1 and y == COLS - 1: 
                    return res

                for dx,dy in directions:

                    if ( x+dx >= ROWS 
                        or y + dy >= COLS 
                        or min(x+dx,y+dy) < 0 
                        or (x+dx,y+dy) in visit
                        or grid[x+dx][y+dy] == 1 
                    ): 
                        continue 
                    else:
                        q.append((x+dx,y+dy))
                        visit.add((x+dx,y+dy))
            
            res += 1 
        return -1 


