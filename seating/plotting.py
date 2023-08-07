import os
from matplotlib import pyplot as plt
import numpy as np
import networkx as nx


# Plot the scores
def plot_results(scores, adj, R, timestep, names, 
                 label_edges=True, k=0.1, savedir=None):
    fig, (ax1,ax2) = plt.subplots(ncols=2, figsize=(12, 6))
    
    # Visualize graph
    G = nx.from_numpy_matrix(np.where(adj, R, 0))
    pos = nx.spring_layout(G, k=k)
    nx.draw(G, labels=names, ax=ax1, pos=pos, node_size=900)
    if label_edges:
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax1)

    ax2.plot(scores)
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Score')
    if savedir is not None:
        plt.savefig(os.path.join(savedir, f'seating_n{timestep}.pdf'), format='pdf')