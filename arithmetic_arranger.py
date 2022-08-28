import numpy as np, re

# input problems: list of strings that are arithmetic problems
# input answer: when set to True, the answers are displayed
# output arranged_problems: the problems arranged vertically and side-by-side
def arithmetic_arranger(problems, answer=False):
    # check for length error
    if len(problems) > 5: return 'Error: Too many problems.'
    # split by spaces
    prob = np.array([ p.split() for p in problems ])
    # check for operator and non-numeric error
    if '*' in prob[:,1] or '/' in prob[:,1]: return "Error: Operator must be '+' or '-'."
    for p in np.concatenate((prob[:,0], prob[:,2])):
        if re.search('[^0-9]', p): return 'Error: Numbers must only contain digits.'
        if len(p) > 4: return 'Error: Numbers cannot be more than four digits.'
    # get max length from each problem 
    maxL = [ len(max(p, key=len)) for p in prob]
    # create arranged_problems 
    prob = prob.T
    if answer:
        ans = [eval(p) for p in problems]
        arranged_problems = createLines(maxL, prob[0], prob[1], prob[2], ans)
    else: 
        arranged_problems = createLines(maxL, prob[0], prob[1], prob[2])
    return arranged_problems

# input maxL: list of lengths of largest operand in each problem
# input op1: list of first operands
# input op: list of operators
# input op2: list of second operands
# input ans: list of answers
# output lines: string holding the problems arranged vertically and side-by-side
def createLines(maxL, op1, op, op2, ans=[]):
    line1, line2, line3 = '', '', ''
    line4 = '\n'
    k=0
    for l in maxL:
        # line 1
        for i in range(0, l-len(op1[k])+2):
            line1 = line1 + ' '
        line1 = line1 + op1[k] + '    '
        # line 2
        line2 = line2 + op[k]
        for i in range(0, l-len(op2[k])+1):
            line2 = line2 + ' '
        line2 = line2 + op2[k] + '    '
        # line 3
        for i in range(0,l+2):
            line3 = line3 + '-'
        line3 = line3+'    '
        # answers
        if len(ans) > 1: 
            for i in range(0, l-len(str(ans[k]))+2):
                line4 = line4 + ' '
            line4 = line4 + str(ans[k]) + '    '
        k = k+1
    # strip extra white space at end and concatentate lines
    lines = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip() + line4.rstrip()
    return lines