def complete(adj,k,c):
    return len(adj) == len(c)

def extensions(adj,k,c):
    i = list(adj.keys())[len(c)]
    cv = [c[x] for x in adj[i] if x in c]
    return [(i,x) for x in range(k) if x not in cv]

def valid(adj,k,c):
    return True

def search(adj,k):
    c = {}
    if aux(adj,k,c):
        return c

def aux(adj,k,c):
    if complete(adj,k,c):
        return valid(adj,k,c)
    for i,x in extensions(adj,k,c):
        c[i] = x
        if aux(adj,k,c):
            return True
        c.pop(i)
    return False

"""
complete(adj, k, c):
    This function checks if the assignment c is complete for the given adjacency list adj and the total number
    of variables k. It compares the length of adj (which represents the number of variables) with the length of
    c (which represents the number of assigned variables). If the lengths are equal, it means all variables have
    been assigned, and the function returns True; otherwise, it returns False.

extensions(adj, k, c):
    This function generates the possible variable-value extensions for the next unassigned variable in the
    adjacency list adj and the current assignment c. It retrieves the first unassigned variable i from the
    keys of the adjacency list. It then collects the assigned values cv for the variables adjacent to i that
    already have assignments in c.Finally, it creates a list of tuples (i, x) where x is a value not present
    in cv and ranges from 0 to k-1.

valid(adj, k, c):
    This function checks if the current assignment c is valid given the adjacency list adj and the total number
    of variables k. In the provided implementation, the valid function always returns True, indicating that any
    assignment is considered valid.
   
search(adj, k):
    This is the main entry point for the backtracking search algorithm. It initializes an empty assignment
    dictionary c. If the auxiliary function aux(adj, k, c) returns True, it means a valid solution has been
    found, and c is returned. If no solution is found, None is implicitly returned.

aux(adj, k, c):
    This is the recursive function that performs the backtracking search. If the assignment c is complete
    (all variables assigned), it calls the valid function to check if it is a valid assignment. If it is
    valid, it returns True, indicating that a solution has been found.Otherwise, it extends the assignment
    by assigning the next variable i to a value x from the extensions provided by the extensions function.
    It recursively calls itself with the extended assignment c, and if a solution is found, it returns True.
    If no solution is found, it removes the variable i from the assignment c (backtracks) and continues with
    the next extension. If all extensions are exhausted without finding a solution, it returns False.
"""