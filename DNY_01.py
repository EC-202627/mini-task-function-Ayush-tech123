M = str(input())
N = int(input())

def calculate_fine(name, days):
    fine = float(days * 5)
    if fine >= 150:
        fine == 150
    print(f"Book: {name}")
    print(f"Days overdue: {days}")
    print(f"Fine: Rs. {fine}")

calculate_fine(M, N)
