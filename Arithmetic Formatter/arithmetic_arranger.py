def arithmetic_arranger(problems , show_answer = True):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ["", "", "", ""]
    #loop for each problem and splited its argument 
    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if show_answer :
            result = str(eval(problem)) 
        else :
            result =" "    

        width = max(len(operand1), len(operand2)) + 2
        arranged_problems[0] += operand1.rjust(width)
        arranged_problems[1] += operator + operand2.rjust(width - 1)
        arranged_problems[2] += "-" * width
        arranged_problems[3] += result.rjust(width) if show_answer else ""
        #add spaces between problems
        if problem != problems[-1]:
            arranged_problems[0] += "    "
            arranged_problems[1] += "    "
            arranged_problems[2] += "    "
            arranged_problems[3] += "    "

    arranged_problems = "\n".join(arranged_problems)  

    return arranged_problems
