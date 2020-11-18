# Operation Research Solvers

Contains separate solvers for different Operation Research problems. The list of problems that have their solvers are:

* Tranportation Problem

* Assignment Problem

## Tranportation Problem

The transportation problem is a special type of linear programming problem where the objective is to minimise the cost of distributing a product from a number of sources or origins to a number of destinations. Because of its special structure the usual simplex method is not suitable for solving transportation problems.

**Input**: Trans_Input.txt
First line contains the no. of supplier and no. of depots.
Second and third line contains the limits of the suppliers and depots.
From fourth line the cost matrix is given with each line for each supplier respectively.

Example

```txt
3 4
250 350 400
200 300 350 150
3 1 7 4
2 6 5 9
8 3 3 2
```
