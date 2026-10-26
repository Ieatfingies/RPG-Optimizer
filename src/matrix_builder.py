import pandas as pd
import numpy as np

def load_game_data(filepath="data/item_database.csv"):
    return pd.read_csv(filepath, index_col="ItemName")

def build_linear_system(item_names, constraints, df):
    selected_items = df.loc[item_names]
    stat_columns = list(constraints.keys())
    item_stats = selected_items[stat_columns]
    A = item_stats.T.to_numpy(dtype=float)
    b = np.array(list(constraints.values()), dtype=float)
    return A, b

def is_system_solvable(A):
    rows, cols = A.shape
    if rows != cols:
        print(f"Matrix is {rows}x{cols}. Exact solvers require a square matrix.")
        return False
    determinant = np.linalg.det(A)
    print(f"Matrix Determinant: {determinant:.2f}")
    if np.isclose(determinant, 0):
        print("Determinant is 0. The items are linearly dependent.")
        return False
    return True

if _name_ == "_main_":
    db = load_game_data()
    desired_items = ['Iron Sword', 'Knight Shield', 'Health Potion']
    desired_stats = {
        'GoldCost': 1000, 
        'Weight': 50,     
        'Attack': 125     
    }
    A, b = build_linear_system(desired_items, desired_stats, db)
    print("Matrix A:\n", A)
    print("\nVector b:\n", b)
    print("\nSolvability Check:")
    is_solvable = is_system_solvable(A)