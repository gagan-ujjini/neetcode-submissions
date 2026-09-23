class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set() # tracks every cell ever added to the queue (multi-source BFS)

        # Since BFS explores level-by-level, starting from every chest simultaneously
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        dist=0 # distance of the current BFS layer/frontier from the nearest chest

        #expand outward one full layer at a time.
        while q:
            # Processing exactly len(q) cells = processing one complete "ring"/level of BFS.
            # Every cell popped in this inner loop is guaranteed to be `dist` steps away.
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist # stamp this cell with its distance from nearest chest

                for dr, dc in directions:
                    row, col = r+dr, c+dc

                    # Skip if: out of bounds, already discovered, or water (impassable).
                    if(row<0 or row >= ROWS or col<0 or col>= COLS or (row, col) in visit or grid[row][col] == -1):
                        continue

                    # Mark visited at PUSH time
                    visit.add((row, col))
                    q.append((row, col))
            
            dist += 1 # move to the next layer — every cell in the queue now is dist+1 away
        
#Time: O(rows × cols), Space: O(rows × cols) — each cell is enqueued/visited exactly once now.