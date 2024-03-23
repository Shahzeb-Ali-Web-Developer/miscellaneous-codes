class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            popped = self.head.data
            self.head = self.head.next
            self.size -= 1
            return popped

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.head.data

    def get_size(self):
        return self.size

    def get_items(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            items = []
            current = self.head
            while current:
                items.append(current.data)
                current = current.next
            return items

def is_valid_step(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "*"

def solve_maze(maze):
    stack = Stack()
    visited = set()
    start_x, start_y = None, None

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'P':
                start_x, start_y = i, j
                break

    if start_x is None or start_y is None:
        return "No starting point found", []

    stack.push((start_x, start_y, []))

    while not stack.is_empty():
        x, y, path = stack.pop()

        if maze[x][y] == 'T':
            return "Maze solved", path + [(x, y)]

        visited.add((x, y))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_step(nx, ny, maze) and (nx, ny) not in visited:
                stack.push((nx, ny, path + [(x, y)]))

    return "Maze unsolved", []

maze1 = [
    [" ", "*", " ", "*", " ", " "],[" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],["*", " ", " ", " ", " ", " "]]

maze2 = [
    [" ", "*", " ", "*", " ", " "],[" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],["*", " ", " ", " ", " ", "*"]
]

result1, path1 = solve_maze(maze1)
print(result1)
if result1 == "Maze solved":
    print("Path:", path1)

result2, path2 = solve_maze(maze2)
print(result2)
if result2 == "Maze solved":
    print("Path:", path2)
