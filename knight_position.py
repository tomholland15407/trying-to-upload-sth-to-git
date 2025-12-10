MOD = 10**9 + 7

def mat_mult(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) % MOD for j in range(n)] for i in range(n)]

def mat_pow(mat, p):
    n = len(mat)
    if p == 0:  # base case: identity matrix
        return [[int(i == j) for j in range(n)] for i in range(n)]
    if p == 1:
        return mat
    half = mat_pow(mat, p // 2)
    half_sq = mat_mult(half, half)
    return mat_mult(half_sq, mat) if p % 2 else half_sq

def is_valid(mask, M):
    for r in range(M):
        if mask & (1 << r):
            for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                           (1, -2), (1, 2), (2, -1), (2, 1)]:
                nr = r + dr
                if 0 <= nr < M and dc == 0 and mask & (1 << nr):
                    return False
    return True

def can_transition(a, b, M):
    for r in range(M):
        if a & (1 << r):
            for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                           (1, -2), (1, 2), (2, -1), (2, 1)]:
                nr = r + dr
                if 0 <= nr < M and dc == 1 and b & (1 << nr):
                    return False
    return True

def count_knight_placements(M, N):
    configs = [mask for mask in range(1 << M) if is_valid(mask, M)]
    size = len(configs)
    trans = [[int(can_transition(a, b, M)) for b in configs] for a in configs]
    trans_pow = mat_pow(trans, N - 1)
    return sum(sum(row) for row in trans_pow) % MOD

# Example test cases
for M, N in [(1, 2), (2, 2), (2, 3), (4, 10)]:
    print(count_knight_placements(M, N))