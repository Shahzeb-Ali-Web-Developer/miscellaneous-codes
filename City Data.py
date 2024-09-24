class CityData:
    def __init__(self, name, outConCount, outCons):
        self.name = name  # Name of the city
        self.outConCount = outConCount  # Number of outgoing connections
        self.outCons = outCons  # List of outgoing connection indices
        self.seen = False  # Whether the city has been visited
        self.predecessor = -1  # Index of the predecessor city (for path tracing)



def read_city_data(filename):
    with open(filename, 'r') as file:
        city_count = int(file.readline().strip())  # Read the number of cities
        cities = []  # List to store CityData objects

        for _ in range(city_count):
            line = file.readline().strip().split(', ')  # Read city line
            index, city_name = line[0].split(' ', 1)  # Separate index and name
            index = int(index)
            outConData = list(map(int, line[1].split()))  # Split outgoing connections data
            outConCount = outConData[0]  # Number of outgoing connections
            outCons = outConData[1:]  # Indices of connected cities
            cities.append(CityData(city_name, outConCount, outCons))

    return cities


def find_route(cities, current_index, destination_index, path):
    current_city = cities[current_index]
    current_city.seen = True  # Mark the current city as seen
    path.append(current_index)  # Add the current city to the path

    # If the current city is the destination, print the path
    if current_index == destination_index:
        print("Path is:", " -> ".join(cities[i].name for i in path))
        return True

    # Recursively search each unseen connected city
    for neighbor_index in current_city.outCons:
        neighbor_city = cities[neighbor_index]
        if not neighbor_city.seen:
            neighbor_city.predecessor = current_index  # Set the predecessor
            if find_route(cities, neighbor_index, destination_index, path):
                return True

    # Backtrack: Remove the current city from the path
    path.pop()
    return False


def main():
    filename = input("Please enter filename storing a network: ").strip()
    cities = read_city_data(filename)

    while True:
        start_name = input("Enter the name of starting city: ").strip()
        destination_name = input("Enter the name of destination: ").strip()

        # Find indices of the starting and destination cities
        start_index = next((i for i, city in enumerate(cities) if city.name == start_name), -1)
        destination_index = next((i for i, city in enumerate(cities) if city.name == destination_name), -1)

        # Check if the starting and destination cities are valid
        if start_index == -1:
            print(f"{start_name} is not a valid city, please re-enter options.")
            continue
        if destination_index == -1:
            print(f"{destination_name} is not a valid city, please re-enter options.")
            continue

        # Reset seen status and predecessors for a fresh search
        for city in cities:
            city.seen = False
            city.predecessor = -1

        # Find the route using recursion
        path = []
        if not find_route(cities, start_index, destination_index, path):
            print(f"There is no path from {start_name} to {destination_name}, please re-enter options.")
        else:
            break  # Exit the loop once a valid path is found

# Run the main function
if __name__ == "__main__":
    main()
