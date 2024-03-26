def fi(n):
    if n <= 2:
        return 1
    return fi(n-1) + fi(n-2)

print(fi(0))