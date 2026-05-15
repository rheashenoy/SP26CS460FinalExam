"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Rhea Shenoy
Student ID: 130452657

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    return " 1) Just shortest path is not enough becuase we also want it to visit " \
        "every chamber in set M atleast once. The decision that shortest path cannot make is in which order to visit the chambers"\
        "2) Deciding which path to take so as to visit all the chambers"\
        "If we do a single computation it is possible that another path uses lesser fuel. So searching over order allows you " \
        "to check all the different paths and therefore choosing the cheapest one."


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    relics.append(spawn)
    relics.append(exit_node)

    return relics


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    distances_from_source = {}

    for node in graph:
        distances_from_source[node] = float('inf')

    distances_from_source[source] = 0
    min_heap = [(0, source)]
    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances_from_source[current_node]:
            continue

        else:
            for neighbour, cost in graph[current_node]:
                new_distance = current_distance + cost
                if new_distance < distances_from_source[neighbour]:
                    distances_from_source[neighbour] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbour))

    return distances_from_source


def precompute_distances(graph, spawn, relics, exit_node):
    sources = select_sources(spawn, relics, exit_node)
    dijkstras_distances = {}

    for node in sources:
        dijkstras_distances[node] = run_dijkstra(graph, node)
    return dijkstras_distances

# =============================================================================
# PART 3
# =============================================================================


def dijkstra_invariant_check():
    return "3a)**For nodes already finalized (in S):** Since nodes are already in S the nodes shortest distance is already finalized from the source" \
        "- **For nodes not yet finalized (not in S):**Since the node is not in S the shortest distance is not finalised but distance saved is the shortest" \
        "path found so far but we could still find a shorter path."\
        "3)b **Initialization : why the invariant holds before iteration 1:** Before the first iteration all the nodes have a distance of infinity as no"\
        "distances have been found and te distance for the source from the source is zero. So no distances have been found incorrectly." \
        "**Maintenance : why finalizing the min-dist node is always correct:** When going through the loop finalizing the min-distance node" \
        "is correct since all edges are non-negative there will not be a shorter path to than the shortest distance." \
        "**Termination : what the invariant guarantees when the algorithm ends:** All the nodes have the shortest distance from the source."\
        "3)c) the correct shortest path distances are necessary so that torchbearer can choose the path with the minimum cost and therefore " \
        "will not waste fuel or take the wrong exit."

# =============================================================================
# PART 4
# =============================================================================


def explain_search():
    return "**The failure mode:** Greedy picks the shortest distance in that moment which is the local optimal choice. But later " \
        "it could lead to a higher total cost " \
        "- **Counter-example setup:** " \
        "S -> A - 1 " \
        "S -> B - 2 " \
        "A -> B - 100 " \
        "B -> A - 3 " \
        "A -> T - 2 " \
        "B -> T - 5 " \
        "- **What greedy picks:** Greedy picks S -> A -> B -> T, whose total cost is 106 " \
        "- **What optimal picks:** Optimal picks S -> B -> A -> T whose total cost is 7 " \
        "- **Why greedy loses:** Becuase greedy ignores the possiblity that future costs could make the total cost larger."\
        "The algorithm must explore all the different orders of nodes the torchbearer can take from the start node to the end node."


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    relics_remaining = set(relics)
    collected_relics = []
    cost_so_far = 0

    best_so_far = [float('inf'), []]

    _explore(dist_table, spawn, relics_remaining,
             collected_relics, cost_so_far, exit_node, best_so_far)

    return best_so_far[0], best_so_far[1]


def _explore(dist_table, current_loc, relics_remaining, collected_relics, cost_so_far, exit_node, best):
    # This part of the code prunes, it lets us skip any computed path that is more expensive than the best one we have found.
    # This way we are evaluating all the possible paths but getting rid of paths where the current cost + remaining cost is more than
    # best so far

    # pruning
    if cost_so_far >= best[0]:
        return

    # base case
    if not relics_remaining:

        remaining_cost = dist_table[current_loc][exit_node]

        if remaining_cost == float('inf'):
            return

        total_cost = cost_so_far + remaining_cost
        if total_cost <= best[0]:
            best[0] = total_cost
            best[1] = collected_relics.copy()
            return

    # recursive case

    for relic in relics_remaining:
        cost_to_travel = dist_table[current_loc][relic]

        if cost_to_travel == float('inf'):
            continue

        relics_remaining.remove(relic)
        collected_relics.append(relic)
        cost_so_far += cost_to_travel

        _explore(dist_table, relic, relics_remaining,
                 collected_relics, cost_so_far, exit_node, best)

        collected_relics.pop()
        relics_remaining.add(relic)

# =============================================================================
# PIPELINE
# =============================================================================


def solve(graph, spawn, relics, exit_node):
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    min_cost, relics_in_order = find_optimal_route(
        dist_table, spawn, relics, exit_node)

    return min_cost, relics_in_order


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
