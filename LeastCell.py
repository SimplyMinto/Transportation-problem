import numpy as np


def least_cost_method(supply, demand, cost_matrix):
    # Initialize the solution matrix with zeros
    rows, cols = len(supply), len(demand)
    solution = np.zeros((rows, cols))

    # Copy supply and demand to avoid modifying the original lists
    supply_copy = supply.copy()
    demand_copy = demand.copy()

    while np.any(supply_copy) and np.any(demand_copy):
        # Find the cell with the minimum cost
        min_cost_idx = np.unravel_index(np.argmin(cost_matrix, axis=None), cost_matrix.shape)
        i, j = min_cost_idx

        # Allocate as much as possible to the minimum cost cell
        allocation = min(supply_copy[i], demand_copy[j])
        solution[i, j] = allocation

        # Reduce the corresponding supply and demand
        supply_copy[i] -= allocation
        demand_copy[j] -= allocation

        # If supply is exhausted, set the row's costs to a very high number to avoid revisiting
        if supply_copy[i] == 0:
            cost_matrix[i, :] = np.inf

        # If demand is exhausted, set the column's costs to a very high number to avoid revisiting
        if demand_copy[j] == 0:
            cost_matrix[:, j] = np.inf

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

    # Compute the initial feasible solution using the Least Cost Method
    solution = least_cost_method(supply, demand, cost_matrix)

    # Display the solution
    print("\nInitial Solution using Least Cost Method:")
    print(solution)

    # Calculate the total transportation cost
    total_cost = calculate_total_cost(solution, cost_matrix)

    # Display the total cost
    print("\nTotal Transportation Cost:")
    print(total_cost)


if __name__ == "__main__":
    main()
