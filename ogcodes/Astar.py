import heapq

def print_puzzle(puzzle):
    """Display the puzzle in a 3x3 grid format"""
    print("\nCurrent puzzle state:")
    for i in range(0, 9, 3):
        print("+---+---+---+")
        print("| {} | {} | {} |".format(*(
            " " if num == 0 else str(num) for num in puzzle[i:i+3]
        )))
    print("+---+---+---+")

def calculate_heuristic(puzzle, goal_positions):
    """Calculate Manhattan distance heuristic"""
    return sum(
        abs(i//3 - goal_positions[num]//3) + abs(i%3 - goal_positions[num]%3)
        for i, num in enumerate(puzzle) if num != 0
    )

def is_solvable(puzzle):
    """Check if the puzzle is solvable using inversion count"""
    inv_count = 0
    nums = [x for x in puzzle if x != 0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                inv_count += 1
    return inv_count % 2 == 0

def solve_puzzle(start, goal):
    """Solve the puzzle using A* algorithm"""
    goal_positions = {num: i for i, num in enumerate(goal)}
    heap = [(calculate_heuristic(start, goal_positions), 0, start, [])]
    visited = set()
    
    while heap:
        _, moves, current, path = heapq.heappop(heap)
        
        if current == goal:
            return path + [current]
        
        if tuple(current) in visited:
            continue
        visited.add(tuple(current))
        
        empty_pos = current.index(0)
        for move in [-3, 3, -1, 1]:  # Up, Down, Left, Right
            if (move == -3 and empty_pos < 3) or (move == 3 and empty_pos > 5) or \
            (move == -1 and empty_pos % 3 == 0) or (move == 1 and empty_pos % 3 == 2):
                continue
            
            new_puzzle = current[:]
            new_puzzle[empty_pos], new_puzzle[empty_pos + move] = \
                new_puzzle[empty_pos + move], new_puzzle[empty_pos]
            
            heapq.heappush(heap, (
                moves + 1 + calculate_heuristic(new_puzzle, goal_positions),
                moves + 1,
                new_puzzle,
                path + [current]
            ))
    
    return None

def get_puzzle_input(prompt):
    """Get puzzle input from user with validation"""
    while True:
        try:
            print(f"\n{prompt} (enter 9 numbers separated by spaces, use 0 for empty tile):")
            values = list(map(int, input().split()))
            if len(values) != 9 or sorted(values) != list(range(9)):
                raise ValueError
            return values
        except ValueError:
            print("Invalid input! Please enter exactly 9 unique numbers from 0-8.")

def main():
    print("8-Puzzle Solver using A* Algorithm")
    
    start_state = get_puzzle_input("Enter the initial puzzle state")
    goal_state = get_puzzle_input("Enter the goal puzzle state")
    
    if not is_solvable(start_state):
        print("\nNo solution exists for the given puzzle configuration (unsolvable).")
        return
    
    print("\nSolving the puzzle...")
    solution = solve_puzzle(start_state, goal_state)
    
    if solution:
        print("\n✅ Solution found! Here are the steps:")
        for step, state in enumerate(solution):
            print(f"\nStep {step}:")
            print_puzzle(state)
        print(f"\nTotal moves required: {len(solution) - 1}")
    else:
        print("\nNo solution exists for the given puzzle configuration.")

if __name__ == "__main__":
    main()
    
    
#input dalo ye wala

#1 2 3 4 0 5 6 7 8
#1 2 3 4 5 6 7 8 0