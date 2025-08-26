t = int(input())
Ans = []
for _ in range(t):
    S = input()

    A = list(S)

    result = []
    for i in range(len(A)):
        if A[i] == "q":
            result.append("p")
        if A[i] == "p":
            result.append("q")
        if A[i] == "w":
            result.append("w")

    F_str = "".join(result)
    Ans.append(F_str)

for i in range(len(Ans)):
    print(Ans[i])
