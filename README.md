# Seating
Multi-period seating plan optimization.

## Installation
```bash 
git clone ...
cd seating
pip install .
```

## Usage
Example 1: three sequential dinner parties each with two tables, one recangular table with two fixed heads and 8 guests, one round table with 5 guests. `relationships.csv` is the matrix of pairwise relationship scores between guests (all named). The output is saved in `figures/`.
```bash
python -m seating 8 5 -t rectangular_with_heads -t round -r data/relationships.csv -s figures/ -n 3 -f 0 -f 7 
```

Example 2: two sequential dinner parties each with a single round table of 15 guests. Host and their partner have their positions fixed.
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