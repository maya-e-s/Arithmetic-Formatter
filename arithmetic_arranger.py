import re, numpy as np

# inputs: list of strings containing arithmetic problems; when 'answer' is set to True the answers are also returned
# output: string containing the problems arranged vertically and side-by-side
def arithmetic_arranger(problems, answer=False):
    # check for errors 
    if len(problems) > 5: 
        return 'Error: Too many problems.'
    prob = np.array([ p.split() for p in problems ])
    if '*' in prob[:,1] or '/' in prob[:,1]: 
        return "Error: Operator must be '+' or '-'."
    for p in np.concatenate((prob[:,0], prob[:,2])):
        if re.search('[^0-9]', p): 
            return 'Error: Numbers must only contain digits.'
        if len(p) > 4: 
            return 'Error: Numbers cannot be more than four digits.'
    # create arranged_problems 
    maxL = [ len(max(p, key=len)) for p in prob] # get max length from each problem 
    prob = prob.T
    if answer:
        ans = [eval(p) for p in problems]
        arranged_problems = createLines(maxL, prob[0], prob[1], prob[2], ans)
    else: 
        arranged_problems = createLines(maxL, prob[0], prob[1], prob[2])
    return arranged_problems

# Helper function for arithmetic_arranger
# input maxL: list of lengths of largest operand per problem
# inputs op1, op, op2, ans: list of first operands, operators, second operands, and answers
# output: string holding the problems arranged vertically and side-by-side
def createLines(maxL, op1, op, op2, ans=[]):
    line1 = line2 = line3 = ''
    line4 = '\n'
    k=0
    for l in maxL:
        line1 += op1[k].rjust(l+2, ' ') + ' '*4
        line2 += op[k] + op2[k].rjust(l+1, ' ') + ' '*4
        line3 += '-'*(l+2) + ' '*4
        if len(ans) > 1: 
            line4 += str(ans[k]).rjust(l+2, ' ') + ' '*4 # answers
        k = k+1
    # strip extra white space at end and concatentate lines
    lines = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip() + line4.rstrip()
    return lines