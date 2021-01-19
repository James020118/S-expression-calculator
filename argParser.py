class Parser:
    def __init__(self, expr):
        self.expr = expr

    # Parsing arguments into a list
    def parse_input(self):
        newStr = ""
        for char in self.expr:
            # Separating opening and closing brackets from the word,
            # thus making brackets their own elements in the list
            if char == "(":
                newStr += char + " "
            elif char == ")":
                newStr += " " + char
            else:
                newStr += char
        return newStr.split()

