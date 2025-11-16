def hanoi(n, source, target, helper):
    if n == 1:
        print(f"Move disc 1 from {source} to {target}")
    else:
        hanoi(n - 1, source, helper, target)
        print(f"Move disc {n} from {source} to {target}")
        hanoi(n - 1, helper, target, source)

# Move from A to B using C as helper
hanoi(3, 'A', 'B', 'C')