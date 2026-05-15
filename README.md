# The Torchbearer

**Student Name:** Rhea Shenoy
**Student ID:** 130452657
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  Just shortest path is not enough becuase we also want it to visit every chamber in set M atleast once. The decision that shortest path cannot make is in which order to visit the chambers

- **What decision remains after all inter-location costs are known:**
  Deciding which path to take so as to visit all the chambers

- **Why this requires a search over orders (one sentence):**
  If we do a single computation it is possible that another path uses lesser fuel. So searching over order allows you to check all the different paths and therefore choosing the cheapest one.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| start node | becuase we start the path from her so we need to run Dijkstras and the DFS from this node. |
| relic node | We need to run dijkstra's and DFS from each of the relics so that we can get theleast cost from each of the relics to all the other relics |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | Dictionary |
| What the keys represent | source nodes|
| What the values represent | Values represent dictionaries that store key-value pairs with the different destivnation nodes and the shortest distance to them from the source node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Since dictionaries represent a hashmap the time complexity to search in a hash table is always constant|

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs: k+1
- **Cost per run: O(mlog(n))
- **Total complexity:O((k+1)(mlog(n)))
- **Justification (one line): There are k relics and one start node and we run dijkstra's from all of them and so there are 
k+1 nodes we run dijkstra's from.

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  Since nodes are already in S the nodes shortest distance is already finalized from the source

- **For nodes not yet finalized (not in S):**
  Since the node is not in S the shortest distance is not finalised but distance saved is the shortest path found so far but we could still find a shorter path.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  Before the first iteration all the nodes have a distance of infinity as no distances have been found and te distance for the source from the source is zero. So no distances have been found incorrectly.

- **Maintenance : why finalizing the min-dist node is always correct:**
  When going through the loop finalizing the min-distance node is correct since all edges are non-negative there will not be a shorter path to than the shortest distance.

- **Termination : what the invariant guarantees when the algorithm ends:**
  All the nodes have the shortest distance from the source.

### Part 3c: Why This Matters for the Route Planner

 the correct shortest path distances are necessary so that torchbearer can choose the path with the minimum cost and therefore will not waste fuel or take the wrong exit.

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** Greedy picks the shortest distance in that moment whihc is the local opti mal choice. But later it could leade to a higher total cost
- **Counter-example setup:** 
S -> A - 1
S -> B - 2
A -> B - 100
B -> A - 3
A -> T - 2
B -> T - 5
- **What greedy picks:** Greedy picks S -> A -> B -> T, whose total cost is 106
- **What optimal picks:** Optimal picks S -> B -> A -> T whose total cost is 7
- **Why greedy loses:** Becuase greedy ignores the possiblity that future costs could make the total cost larger.

### What the Algorithm Must Explore

- The algorithm must explore all the different orders of nodes the torchbearer can take from the start node to the end node.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
