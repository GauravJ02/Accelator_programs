def large_transactions(amount, threshold):
    if amount > threshold:
        yield amount

print(next(large_transactions(amount,threshold)))