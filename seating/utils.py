import os
import numpy as np
import pandas as pd
import click

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

# Build template (lower triangular) relationship matrix from list of names.
@click.command()
@click.argument('names', nargs=-1)
@click.option('--savedir', '-s', default='data/', 
              help='Save directory for relationship matrix.')
def build_R(names, savedir):
    N = len(names)
    R = np.ones((N,N))
    R = np.tril(R, k=-1) # lower triangular
    df = pd.DataFrame(R.astype(int))

    # relabel indices of dataframe to be list of names
    df.index = names
    df.columns = names
    df.to_csv(os.path.join(savedir, 'relationships.csv'))