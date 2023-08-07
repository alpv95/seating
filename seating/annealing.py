import numpy as np

from .utils import *

# Simulated Annealing, given initial adjacency matrix, Relationship matrix.
def simulated_annealing(adj, R, T, alpha, max_iter, fixed=None):
    N = adj.shape[0]
    scores = [objective(adj, R)]
    swappable_nodes = np.arange(N)
    if fixed is not None:
        swappable_nodes = np.delete(swappable_nodes, fixed)
    for t in range(max_iter):
        node1, node2 = np.random.choice(swappable_nodes, 2, 
                                        replace=False)
        new_adj = swap_nodes(adj, node1, node2)
        score = objective(new_adj, R)
        # Simulated Annealing adjust temperature
        T /= (t + 1) ** alpha
        if score > scores[-1] or np.random.rand() < np.exp((score - scores[-1]) / T):
            adj = new_adj
            scores.append(score)
        else:
            scores.append(scores[-1])
    return adj, scores
