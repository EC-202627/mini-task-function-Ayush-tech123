M = str(input())
N = int(input())
F = int(input())

def calculate_fine(name, days, fine):
    fine = float(days * fine)
    if fine > 150:
        fine = 150
    print(f"Book: {name}")
    print(f"Days overdue: {days}")
    print(f"Fine: Rs. {fine}")
    return fine

f = calculate_fine(M, N, F)

#Status Done