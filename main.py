import sys
from argParser import *
from evaluator import *

def main():
    # Checks whether there are sufficient arguments
    if len(sys.argv) <= 1:
        print("Not enough input.")
        return

    # Parsing input into a list
    parser = Parser(sys.argv[1])
    expression = parser.parse_input()
    
    # Evaluating the list
    eval = Evaluator(expression)
    result = eval.evaluate()
    print(result)

if __name__ == "__main__":
    main()