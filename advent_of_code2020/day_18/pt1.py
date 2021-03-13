with open("d18input.txt", "r") as f:
    exps = [x.strip() for x in f.readlines()]

results = []
for exp in exps:
    #print(exp)
    while "(" in exp or ")" in exp:
        
        first_par = exp[::-1].index("(")
        rfp = len(exp) - 1 - first_par
        closed_rfp = exp[rfp:].index(")") + rfp + 1
        
        pexp = exp[rfp+1:closed_rfp-1]

        ops_pos = [(i, x) for i, x in enumerate(pexp.split(" ")) if x in ["+", "*"]]
        pexp_s = pexp.split(" ")
    
        for ii, (i, op) in enumerate(ops_pos):
            if ii >= 1:
                s_part = prev_val
            else:
                s_part = int(pexp_s[i-1])
                
            if op == "*":
                val = int(s_part) * int(pexp_s[i+1])
            else:
                val = int(s_part) + int(pexp_s[i+1])
            prev_val = val
        
        exp = exp[:rfp] + str(val) + exp[closed_rfp:]

    #print(exp)
    ops_pos = [(i, x) for i, x in enumerate(exp.split(" ")) if x in ["+", "*"]]
    s_exp = exp.split(" ")

    for ii, (i, op) in enumerate(ops_pos):
        if ii >= 1:
            s_part = prev_val
        else:
            s_part = int(s_exp[i-1])

        if op == "*":
            val = int(s_part) * int(s_exp[i+1])
        else:
            val = int(s_part) + int(s_exp[i+1])
        prev_val = val
    results.append(val)
#print(results)
print(sum(results))
