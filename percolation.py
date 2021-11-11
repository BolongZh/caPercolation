import numpy as np
import itertools

def check_complete(matrix):
    # check if a graph represented by adjacency matrix is complete
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 0:
                return False
    return True


def forward(initial_state, n, h):
    nodes = itertools.combinations([i for i in range(n)], h)
    thresh = h * (h - 1) // 2

    toConnect = []
    for j in nodes:
        connections = 0
        disconnection = 0
        nodeX = None
        nodeY = None
        for comb in itertools.combinations(j, 2):
            x = comb[0]
            y = comb[1]
            if initial_state[x][y] == 1:
                connections += 1
            else:
                nodeX = x
                nodeY = y
                disconnection += 1
            # early stopping if 2 edges are disconnected
            if disconnection > 1:
                break
        if connections == thresh - 1:
            toConnect.append((nodeX, nodeY))

    # making connections
    for i in toConnect:
        nodeX = i[0]
        nodeY = i[1]
        initial_state[nodeX][nodeY] = 1

    # whether the process stabilized
    return len(toConnect) == 0

def trial(num_sim, n, h, p, estimated_prob):
    success = 0
    for _ in range(num_sim):
        adjacency_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(i + 1, n):
                if np.random.random_sample() < p:
                    adjacency_matrix[i][j] = 1
        stabilized = False
        while not stabilized:
            stabilized = forward(adjacency_matrix, n, h)
        if check_complete(adjacency_matrix):
            success += 1
    estimated_prob.append(success / num_sim)
    return p, success/num_sim



