import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.linalg import block_diag
from collections.abc import Sequence

# Different types of table arrangements.
def rectangular_with_heads(N):
    adj = np.zeros((N, N))
    adj[0, 1] = 1
    adj[0, 2] = 1
    for i in range(1, N-2):
        adj[i, i+2] = 1
        if i % 2 != 0:
            adj[i, i+1] = 1
    adj[N-2, N-1] = 1
    adj_sym = (adj + adj.T).astype(int)
    return adj_sym

def recatangular(N):
    assert N % 2 == 0, "N must be even for rectangular table"
    adj = np.zeros((N, N))
    for i in range(0, N-2):
        adj[i, i+2] = 1
        if i % 2 == 0:
            adj[i, i+1] = 1
    adj[N-2, N-1] = 1
    adj_sym = (adj + adj.T).astype(int)
    return adj_sym

def strong_recatangular_with_heads(N):
    adj = np.zeros((N, N))
    adj[0, 1] = 1
    adj[0, 2] = 1
    for i in range(1, N-2):
        adj[i, i+2] = 1
        adj[i, i+1] = 1
        if i % 2 != 0:
            try: 
                adj[i, i+3] = 1
            except:
                pass
    adj[N-2, N-1] = 1
    adj_sym = (adj + adj.T).astype(int)
    return adj_sym

def strong_recatangular(N):
    assert N % 2 == 0, "N must be even for rectangular table"
    adj = np.zeros((N, N))
    for i in range(0, N-2):
        adj[i, i+2] = 1
        adj[i, i+1] = 1
        if i % 2 == 0:
            adj[i, i+3] = 1
    adj[N-2, N-1] = 1
    adj_sym = (adj + adj.T).astype(int)
    return adj_sym

def round(N):
    adj = np.zeros((N, N))
    adj[0, 1] = 1
    adj[0, N-1] = 1
    for i in range(1, N-2):
        adj[i, i+1] = 1
    adj[N-2, N-1] = 1
    adj_sym = (adj + adj.T).astype(int)
    return adj_sym

def strong_round(N):
    adj = np.zeros((N, N))
    adj[0, 1] = 1
    adj[0, 2] = 1
    adj[0, N-1] = 1
    adj[0, N-2] = 1
    for i in range(1, N-2):
        adj[i, i+1] = 1
        adj[i, i+2] = 1
    adj[N-2, N-1] = 1
    adj[1, N-1] = 1
    adj_sym = (adj + adj.T).astype(int)
    return adj_sym

def init_table_adj(N, type='round'):
    if type == 'round':
        adj = round(N)
    elif type == 'rectangular':
        adj = recatangular(N)
    elif type == 'rectangular_with_heads':
        adj = rectangular_with_heads(N)
    elif type == 'strong_round':
        adj = strong_round(N)
    elif type == 'strong_rectangular':
        adj = strong_recatangular(N)
    elif type == 'strong_rectangular_with_heads':
        adj = strong_recatangular_with_heads(N)
    return adj


# Create table arrangement graph as adjacency matrix.
def init_adj(type_list: Sequence[str], N_list: Sequence[int], save_dir: str=None,) -> np.ndarray:
    assert len(type_list) == len(N_list), "type_list and N_list must have same length"
    table_list = []
    for type, N in zip(type_list, N_list):
        table_list.append(init_table_adj(N, type))
    adj = block_diag(*table_list)

    if save_dir is not None:
        # Visualize graph
        G = nx.from_numpy_matrix(adj)
        nx.draw(G, with_labels=True)
        plt.savefig(os.path.join(save_dir, 'initial'), format='pdf')
    return adj