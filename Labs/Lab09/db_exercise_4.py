import time
import sys


def slow_subtractor(a, b):
    """Return a minus b."""
    time.sleep(1)
    return a - b


if __name__ == "__main__":
    some = slow_subtractor(int(sys.argv[1]), int(sys.argv[2]))
    crazy = slow_subtractor(int(sys.argv[3]), int(sys.argv[4]))
    scientific = slow_subtractor(int(sys.argv[5]), int(sys.argv[6]))
    experiment = slow_subtractor(int(sys.argv[7]), int(sys.argv[8]))
    total = some + crazy + scientific + experiment
    experimental_fraction = float(experiment / total)
    print(experimental_fraction)
