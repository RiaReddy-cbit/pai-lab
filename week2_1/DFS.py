def astar_dfs_three_jugs(cap, goal):
    start = (0, 0, 0)
    stack = [(0, 0, start, [])]  # f = g + h, h=0
    visited = set()
    
    while stack:
        f, g, state, path = stack.pop()  # LIFO
        a, b, c = state
        if goal in state:
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        
        next_states = []
        # Fill any jug
        next_states.append((cap[0], b, c))
        next_states.append((a, cap[1], c))
        next_states.append((a, b, cap[2]))
        # Empty any jug
        next_states.append((0, b, c))
        next_states.append((a, 0, c))
        next_states.append((a, b, 0))
        # Pour between jugs
        jugs = [a, b, c]
        for i in range(3):
            for j in range(3):
                if i != j:
                    temp = jugs.copy()
                    pour = min(temp[i], cap[j]-temp[j])
                    temp[i] -= pour
                    temp[j] += pour
                    next_states.append(tuple(temp))
        
        for s in next_states:
            # f = g + h, h = 0
            stack.append((g+1, g+1, s, path + [state]))
    
    return None

def show_solution(sol):
    if sol:
        print(f"\nDFS (A*-like) Solution (moves = {len(sol)-1}):")
        for s in sol:
            print(s)
    else:
        print("\nDFS (A*-like) Solution: No solution found")

# -------- User Input --------
cap_a = int(input("Enter capacity of Jug A: "))
cap_b = int(input("Enter capacity of Jug B: "))
cap_c = int(input("Enter capacity of Jug C: "))
goal = int(input("Enter goal amount: "))

solution = astar_dfs_three_jugs((cap_a, cap_b, cap_c), goal)
show_solution(solution)
