def arithmetic_arranger(problems, s=False):
    first = ""
    op = ""
    lines = ""
    second = ""
    som = ""
    string = ""

    #we can only manage 4 problems
    if(len(problems) > 5):
        return "Error: Too many problems."

    for problem in problems:
        #I set the error here to make it more easy
        if len(problem.split(' ')) >= 5:
            return "Error: Numbers cannot be more than four digits."

        one = problem.split(" ")[0]
        op = problem.split(" ")[1]
        two = problem.split(" ")[2]

        # checking length, max 4
        if len(one) > 4 or len(two) > 4:
            return "Error: Numbers must only have no more than four digits."

        # checking any characters, I prefer isnumeric() than isdigit() because isnumeric() check if all characters are in 0-9, even -1 or 9.3  will throw a False
        if not one.isnumeric() or not two.isnumeric():
            return "Error: Numbers must only contain digits."

        # checking any op different from + or - and adding or subtracting whether op is + or -, if is found we throw the error
        if (op == "+" or op == "-"):
            if op == "+":
                res = str(int(one) + int(two))
            if op == "-":
                res = str(int(one) - int(two))
        else:
            return "Error: Operator must be '+' or '-'."

        #that's the tricky part, we using the length of all variables in the for-loop to create the right whitespaces
        l = max(len(one), len(two)) + 2
        top = str(one.rjust(l))
        bottom = op + str(two.rjust(l - 1))
        smx = str(res).rjust(l)


        line = ""
        for d in range(l):
            line += "-"

        #these lines are for creating the right space and not adding more space to the last addition or subtraction
        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            som += smx + '    '
        else:
            first += top
            second += bottom
            lines += line
            som += smx

    #last step, tricky and ma
    if s:
        string = first + "\n" + second + "\n" + lines
    else:
        string = first + "\n" + second + "\n" + lines + "\n" + som
    return string


x = ["32 - 8", "1 - 3801", "99399 + 9999", "523 - 49"]
print(arithmetic_arranger(x))
