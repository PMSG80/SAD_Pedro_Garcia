
def solution(S):
    if len(S) % 2 == 1:   return 0
	
	
    op1 = {"]": "[", "}": "{", ")": "("}
    op2 = ["[", "{", "("]
    stack = 
    
	for element in S:
        if element in op2:
            stack.append(element)
        else:
            if len(stack) == 0:
                return 0
            
				
    if len(stack) == 0:
        return 1
    else:
        return 0