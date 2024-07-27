def should_buy_coupon(N, X, Y, prices):
    total_without_coupon = sum(prices)
    total_with_coupon = X + sum(max(0, price - Y) for price in prices)
    
    if total_with_coupon < total_without_coupon:
        return "COUPON"
    else:
        return "NO COUPON"

# Read input
T = int(input())
results = []

for _ in range(T):
    N, X, Y = map(int, input().split())
    prices = list(map(int, input().split()))
    result = should_buy_coupon(N, X, Y, prices)
    print(result)

# Print results
#for result in results:
#    print(result)


## Output exactly vaise he hona jaise testcase me hai!!
