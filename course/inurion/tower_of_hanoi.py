def toh(n, from_bar, to_bar, aux_bar):
    if n == 1:
        print(f"Move disk 1 {from_bar} to {to_bar}")
        return
    
    toh(n-1, from_bar, aux_bar, to_bar)
    print(f"Move disk {n} {from_bar} to {to_bar}")
    toh(n-1, aux_bar, to_bar, from_bar)


if __name__ == '__main__':
    toh(4, "A", "B", "C")
