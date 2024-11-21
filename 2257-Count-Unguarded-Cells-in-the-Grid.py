class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
    
        directions = {"LEFT": (0, -1), "RIGHT": (0, 1), "UP": (-1, 0), "DOWN": (1, 0)}
        guarded = set()
        walls = set([tuple(wall) for wall in walls])
        guards = set([tuple(guard) for guard in guards])
        

        def dfs(direction, i, j, guard_count):
            
            if (
                i < 0 or j < 0 or i > m - 1 or j > n - 1
                or (i, j) in walls
                or ((i, j) in guards and guard_count)
            ):
                return

            if (i, j) not in guards:
                guarded.add((i, j))
            else:
                guard_count += 1

            for direction_, dir_vals in directions.items():
                if direction == direction_:
                    dfs(direction, i + dir_vals[0], j + dir_vals[1], guard_count)

        for i, j in guards:
            for direction in directions:
                dfs(direction, i, j, 0)

        return (m * n) - len(guards) - len(walls) - len(guarded)
