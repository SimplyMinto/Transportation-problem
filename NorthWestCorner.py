import numpy as np


def northwest_corner_method(supply, demand):
    # Initialize the solution matrix with zeros
    rows, cols = len(supply), len(demand)
    solution = np.zeros((rows, cols))

    i, j = 0, 0  # Start at the northwest corner
    while i < rows and j < cols:
        if supply[i] < demand[j]:
            solution[i, j] = supply[i]
            demand[j] -= supply[i]
            i += 1
        else:
            solution[i, j] = demand[j]
            supply[i] -= demand[j]
            j += 1

    return solution


def calculate_total_cost(solution, cost_matrix):
    # Calculate the total cost by multiplying the solution matrix by the cost matrix
    total_cost = np.sum(solution * cost_matrix)
    return total_cost


def get_input():
    # Get the number of sources and destinations
    m = int(input("Enter the number of sources: "))
    n = int(input("Enter the number of destinations: "))

    # Get the supply values
    print("\nEnter the supply values for each source:")
    supply = [int(input(f"Supply for source {i + 1}: ")) for i in range(m)]

    # Get the demand values
    print("\nEnter the demand values for each destination:")
    demand = [int(input(f"Demand for destination {i + 1}: ")) for i in range(n)]

    # Get the cost matrix
    print("\nEnter the cost matrix:")
    cost_matrix = []
    for i in range(m):
        row = list(map(int, input(f"Enter costs for source {i + 1} (space-separated): ").split()))
        cost_matrix.append(row)

    cost_matrix = np.array(cost_matrix)

    return supply, demand, cost_matrix


def main():
    # Get user input for supply, demand, and cost matrix
    supply, demand, cost_matrix = get_input()

    # Compute the initial feasible solution using the Northwest Corner Rule
    solution = northwest_corner_method(supply, demand)

    # Display the solution
    print("\nInitial Solution using Northwest Corner Rule:")
    print(solution)

    # Calculate the total transportation cost
    total_cost = calculate_total_cost(solution, cost_matrix)

    # Display the total cost
    print("\nTotal Transportation Cost:")
    print(total_cost)


if __name__ == "__main__":
    main()
