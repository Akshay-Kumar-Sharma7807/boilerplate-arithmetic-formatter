def arithmetic_arranger(problems, solution=False):
  if (len(problems) > 5):
    print("Error: Too many problems.")
    return "Error: Too many problems."

  operand1s = ""
  operand2s = ""
  separator = ""
  result = ""
  for problem in problems:

    [a, op, b] = problem.split()

    # Handle errors
    try:
      int(a)
      int(b)
    except:
      return "Error: Numbers must only contain digits."
    
    if op not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."

    if len(a) > 4 or len(b) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    space = max(len(a), len(b)) + 2
    a = (space - len(a)) * " " + a
    b =  op + (space - len(b) -1 ) * " " +  b


    sol = eval(problem)

    sol = (space - len(str(sol))) * " " + str(sol)
    if result == "":
      result += sol
    else:
      result += "    " + sol

    if operand1s == "":
      operand1s += a
    else:
      operand1s += "    " + a

    if operand2s == "":
      operand2s += b
    else:
      operand2s += "    " + b

    if separator == "":
      separator += space * "-"
    else:
      separator += "    " + space * "-"

  if solution:
    return f"{operand1s}\n{operand2s}\n{separator}\n{result}"
  else:
    return f"{operand1s}\n{operand2s}\n{separator}"