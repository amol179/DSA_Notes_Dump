"""
ID: amolgur1
LANG: PYTHON3
TASK:  shopping
"""

def read_input():
    with open("shopping.in", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    s = int(lines[0])
    offers = []
    idx = 1
    for _ in range(s):
        parts = list(map(int, lines[idx].split()))
        n = parts[0]
        offer = {}
        for i in range(n):
            code = parts[1 + 2 * i]
            qty = parts[2 + 2 * i]
            offer[code] = qty
        price = parts[-1]
        offers.append((offer, price))
        idx += 1

    b = int(lines[idx])
    idx += 1
    needs = []
    code_to_index = {}
    prices = []
    for i in range(b):
        code, qty, price = map(int, lines[idx + i].split())
        code_to_index[code] = i
        needs.append(qty)
        prices.append(price)

    idx += b
    return offers, needs, prices, code_to_index

def apply_offer(offer, needs, code_to_index):
    new_needs = needs[:]
    for code in offer:
        if code not in code_to_index:
            return None
        idx = code_to_index[code]
        if offer[code] > new_needs[idx]:
            return None
        new_needs[idx] -= offer[code]
    return new_needs

def dfs(needs, offers, prices, code_to_index, memo):
    key = tuple(needs)
    if key in memo:
        return memo[key]

    # Regular price without any offer
    min_cost = 0
    for i in range(len(needs)):
        min_cost += needs[i] * prices[i]

    # Try each offer
    for offer, offer_price in offers:
        new_needs = apply_offer(offer, needs, code_to_index)
        if new_needs is not None:
            cost = offer_price + dfs(new_needs, offers, prices, code_to_index, memo)
            if cost < min_cost:
                min_cost = cost

    memo[key] = min_cost
    return min_cost

def main():
    offers, needs, prices, code_to_index = read_input()
    memo = {}
    result = dfs(needs, offers, prices, code_to_index, memo)
    with open("shopping.out", "w") as f:
        f.write(str(result) + "\n")

main()