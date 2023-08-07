import numpy as np

# Swap two nodes in the adjacency matrix
def swap_nodes(adj, i, j):
    assert i != j, "Shouldn't swap node with itself"
    adj = adj.copy()
    adj[[i, j]] = adj[[j, i]]
    adj[:, [i, j]] = adj[:, [j, i]]
    return adj

# Objective function
def objective(adj, R):
    return np.sum(np.where(adj, R, 0)) / 2