# Seating
Multi-period seating plan optimization. 

*The dinner party solution you have always dreamed of. Now your guests can stop complaining they were seated next to an obnoxious boor.*

## Description
This is a Python package for optimizing seating plans for multiple periods. It describes a seating plan as a graph with guests as nodes and edges representing the relationship between guests. Both the graph structure (the table layout) and the pairwise relationship between guests are user-defined. Simulated annealing is used to find the optimal seating plan for the given graph structure and pairwise relationships by minimizing the total relationship score of the seating plan.

Over multiple time periods with the same guests, pairwise relationships are penalized if the guests sat next to each other in previous periods.

## Features
- Handles any number of guests and tables.
- Supports multiple periods with the same guests (e.g. multiple dinner parties).
  * Pairings of guests who sat next to each other in previous time periods are penalized. 
  * Guests can be fixed to the same position in each period. 
- Supports 3 table topologies each in 2 versions (strongly and weakly connected):
  * rectangular, 
  * rectangular with a head and/or a foot, 
  * round.
- Seating plans and convergence plots are saved as PDFs.
![example](figures/seating_n2.pdf)

## Installation
```bash 
git clone [seating repo]
cd seating
pip install .
```

## Usage
*Example 1*: three sequential dinner parties each with two tables, one recangular table with two fixed heads and 8 guests, one round table with 5 guests. `relationships.csv` is the matrix of pairwise relationship scores between guests (all named). The output is saved in `figures/`.
```bash
python -m seating 8 5 -t rectangular_with_heads -t round -r data/relationships.csv -s figures/ -n 3 -f 0 -f 7 
```

*Example 2*: two sequential dinner parties each with a single round table of 15 guests. Host and their partner have their positions fixed.
```bash
python -m seating 15 -t round -r data/relationships.csv -s figures/ -n 2 -f 0 -f 7 
```

For help with command line arguments and options: 
```bash 
python -m seating --help
```

To create a template for the relationships matrix:
```bash
template [list of names]
```