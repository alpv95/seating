import numpy as np
import pandas as pd
import click

from .annealing import simulated_annealing
from .plotting import plot_results
from .arrangement import init_adj


@click.command()
@click.argument('n_list', type=click.INT, nargs=-1)
@click.option('--tables', '-t', multiple=True, help='List of table types.')
@click.option('--relfile', '-r', default=None, help='Relationship matrix file.')
@click.option('--max_iter', type=click.INT, default=1000,
              help='Maximum iterations of simulated annealing per time period.')
@click.option('--n_periods', '-n', type=click.INT, default=1, help='Number of time periods.')
@click.option('--fixed', '-f', default=None, type=click.INT,
              multiple=True, help='List of guests who cannot be moved.')
@click.option('--savedir', '-s', default=None, help='Save directory for results.')
def main(relfile, n_list, tables, max_iter, n_periods, fixed, savedir):
    # Load pairwise relationships between guests.
    if relfile is not None:
        R_tril = pd.read_csv(relfile, index_col=0)
        R = R_tril.to_numpy() * 1.0
        R = R + R.T # make symmetric
        N = R.shape[0]
        names = dict(zip(np.arange(N), R_tril.index.to_list()))
        assert N == sum(n_list), "Number of guests in relationship file does not match number of guests in N_list."
    else:
        # All pairwise relationships are equal.
        N = sum(n_list)
        R = np.ones((N, N))
        np.fill_diagonal(R, 0)
        names = dict(zip(np.arange(N),np.arange(N)))

    adj = init_adj(tables, n_list,)
    for t in range(n_periods):
        adj, scores = simulated_annealing(adj, R=R, T=5, alpha=0.5, 
                                                max_iter=max_iter, fixed=fixed)
        plot_results(scores, adj, R, t+1, names, label_edges=False, 
                    k=0.1, savedir=savedir)

        # Update R, fractionally reducing relationship score where guests have been seated together
        R *= np.where(adj, 0.5, 1)

if __name__ == '__main__':
    main()