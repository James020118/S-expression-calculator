class Evaluator:
    def __init__(self, expr_list):
        self.expr_list = expr_list

    def evaluate(self):
        # If there still are closing bracket left in the list, calculation not done 
        while ")" in self.expr_list:
            # Using index() to find the first appearance of the closing bracket
            right_index = self.expr_list.index(")")
            left_index = right_index

            # Using a while loop to find the first opening bracket to its left.
            # This guarantees that there is a single valid expression between 
            # left_index and right_index
            while left_index >= 0 and self.expr_list[left_index] != "(":
                left_index -= 1

            # Evaluating the single expression using the helper function
            result = self.evaluate_single_expr(self.expr_list[left_index : right_index + 1])
            
            # Replace the expression with its result, so that we can use the result
            # to further evaluate
            del self.expr_list[left_index : right_index + 1]
            self.expr_list.insert(left_index, result)

        # If there is no closing bracket left, the list guarantees to only contain a 
        # single integer, which is the result
        return self.expr_list[0]

    def evaluate_single_expr(self, sub_expr):
        expressions = sub_expr
        
        # Removes the brackets on both ends of the list
        del expressions[0]
        del expressions[-1]
        
        # Evaluating based on the operation.
        # Since there are only two numbers, I can reference them by using [1] and [2]
        # If there would be more arguments, a for-loop can be implemented
        answer = 0
        operation = expressions[0]
        if operation == "add":
            answer = int(expressions[1]) + int(expressions[2])
        elif operation == "multiply":
            answer = int(expressions[1]) * int(expressions[2])
        else:
            print("Illegal operation.")

        return answer
