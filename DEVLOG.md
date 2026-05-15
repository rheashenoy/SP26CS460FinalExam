# Development Log – The Torchbearer

**Student Name:** Rhea Shenoy
**Student ID:** 130452657

---

## Entry 1 – [5/14/26]: Initial Plan

I think to start I'll start by implementing dijkstra's on the different relic nodes and for each relic node to calculate all the shortest pats from the start node and from all the relics. Then using the shortest path distances stored, we try every single order for the relics and compute costs but we prune as we search to make sure we aren't wasting too much time. Once we do that we then pick the one with the cheapest cost. I think the part that is going to be the most difficult to implement is the search with pruning part, as trying to figure out when to prune and how to prune and make sure the optimal solution isn't discarded is something I forsee my self struggling with. I think testing will need to be done with multiple different graphs to make sure the algorithm i have written works.

---

## Entry 2 – [5/14/26]: [Bug 1 - heappush syntax error]

My code was giving me a massive error in the run_dijkstra's function. It gave me a 'list' object is not callable error. I realised it was my heappush function that was reason for the error. i wrote it such that the compiler thought that minheap was a function itself. I reealised it was a syntax error and added a comma and it started to work.

---

## Entry 3 – [5/14/26]: [the output cost was wrong]

Finally my code was running bu the output it gave me was wrong. It gave me the cost as 14 when it should have been 4. I realised it was becuase I permanently changing the cost_to_far variable and so the output cost kept getting changed so instead I added the travel cost to the cost so far in the recursive call itself

---

## Entry 4 – [5/14/26]: Post-Implementation Reflection

I think I would definately improve on the explore function. Instead of having it go through every possible solution, maybe i may have been able to come up with a solution that finds the order rather than a trial and error. This would therefore bring down the time complexity of our algorithm.

---

## Final Entry – [5/14/26]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 1 hour 15 minutes|
| Part 2: Precomputation Design | 1 hour |
| Part 3: Algorithm Correctness | 40 minutes |
| Part 4: Search Design | 30 minutes |
| Part 5: State and Search Space | 40 minutes |
| Part 6: Pruning | 1 hour |
| Part 7: Implementation | 7 hours |
| README and DEVLOG writing | 45 minutes|
| **Total** | 12 hours and 50 minutes |
