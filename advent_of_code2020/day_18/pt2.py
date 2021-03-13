with open("d18input.txt", "r") as f:
    exps = [x.strip() for x in f.readlines()]

def obtain_result(exp):
    exp = "".join([x for x in exp if x not in ["(", ")"]])
    while "*" in exp or "+" in exp:
        ops = sorted([(i, op) for i, op in enumerate(exp.split())\
                if op in ["*", "+"]], key=lambda x: x[-1], reverse=True)

        sexp = exp.split()
        i = ops[0][0]
        if "+" in [x[-1] for x in ops]:
            res = int(sexp[i-1]) + int(sexp[i+1])
        else:
            res = int(sexp[i-1]) * int(sexp[i+1])

        exp = (" ".join(sexp[:i-1]) + " " + str(res) + " " + " ".join(sexp[i+2:])).strip()
    return int(exp) 

results = []
for exp in exps:
    #print(exp)
    while "(" in exp or ")" in exp:
        
        first_par = exp[::-1].index("(")
        rfp = len(exp) - 1 - first_par
        closed_rfp = exp[rfp:].index(")") + rfp + 1
        
        pexp = exp[rfp+1:closed_rfp-1]
        
        val = obtain_result(pexp)
        exp = exp[:rfp] + str(val) + exp[closed_rfp:]

    results.append(obtain_result(exp))

print(sum(results))
