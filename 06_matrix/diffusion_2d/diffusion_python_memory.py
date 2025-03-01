#!/usr/bin/env python3

import time

try:
    profile
except NameError:
    profile = lambda x: x

grid_shape = (640, 640)


@profile
def evolve(grid, dt, out, D=1.0):
    xmax, ymax = grid_shape
    for i in range(xmax):
        for j in range(ymax):
            grid_xx = (
                grid[(i + 1) % xmax][j] + grid[(i - 1) % xmax][j] - 2.0 * grid[i][j]
            )
            grid_yy = (
                grid[i][(j + 1) % ymax] + grid[i][(j - 1) % ymax] - 2.0 * grid[i][j]
            )
            out[i][j] = grid[i][j] + D * (grid_xx + grid_yy) * dt


def run_experiment(num_iterations):
    # setting up initial conditions
    scratch = [[0.0 for x in range(grid_shape[1])] for x in range(grid_shape[0])]
    grid = [[0.0 for x in range(grid_shape[1])] for x in range(grid_shape[0])]

    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    for i in range(block_low, block_high):
        for j in range(block_low, block_high):
            grid[i][j] = 0.005

    start = time.time()
    for i in range(num_iterations):
        evolve(grid, 0.1, scratch)
        # scratch is the output and is the object updated in evolve
        # it is assigned into the grid variable so grid becomes the input in the subsequent iteration
        # scratch then gets assigned grid (actually they are swapped at the same time)
        # which was the old/previous input and the values are no longer needed,
        # and will be used for the output during the next iteration
        # note that the values are not zeroed out, like they are in the original version
        # but that doesn't matter because each element is overwritten in evolve;
        # the point is to recycle the memory so we don't care about old values
        grid, scratch = scratch, grid
    return time.time() - start


if __name__ == "__main__":
    run_experiment(500)
