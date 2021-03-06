# caPercolation
H-bootstrap percolation process simulation

progress:

1. ~11/4/2021: Developed simulation for complete H and general H with visualizations aided by networkx. The code runs slowly and visualization seems impossible for large and dense graph, but it works nicely with small graphs.
2. ~11/11/2021: Started to focus on the special case for complete H and specifically H=K4. Introduced Numba to speed up the simulation. Numba provides really good speed-up, but the current algorithm is still infeasible for very large n. Estimating p is almost hopeless as it requires large number of simulations to get a good estimation. Also made some animation for fixed n, h, p. The problem with animation is that the process usually converges very quickly (which means it only offers a very small number of frames to build animation upon). Instead of animation, now focusing on the visualization of a single stage of a single process, with colors indicating at which stage in the process an edge gets connected/infected. Algorithm-wise, improved the case for K4 by finding triangles in the graph first and then check K4, which gives better best case bound than the algorithm for general complete graph.
3. ~11/18/2021: Huge thanks to @Bilbert from EECS discord for his valuable advice on my script related to the use of Numpy. Currently running simulations around the critical probability for n = 500, H = K4. Observed clear patterns of "passages" in my matrix representation of the process just below the critical probability. This pattern of narrow passages seems to be absent for processes with p above the critical probability. The pictures will be uploaded later.

Dependency: networkx, matplotlib, numpy
