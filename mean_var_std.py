import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)
    describe = {}
    describe["mean"] = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().item()]
    describe["variance"] = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(),matrix.var().item()]
    describe["standard deviation"] = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().item()]
    describe["max"] = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().item()]
    describe["min"] = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().item()]
    describe["sum"] = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().item()]

    return describe