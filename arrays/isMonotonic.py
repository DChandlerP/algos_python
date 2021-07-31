# https://www.geeksforgeeks.org/python-program-to-check-if-given-array-is-monotonic/
def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))