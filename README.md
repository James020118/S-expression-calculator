# S-expression-calculator

Write a command line program that acts as a simple calculator: it takes a
single argument as an expression and prints out the integer result of
evaluating it.

Assuming the program is implemented in Python, invocations should look like:

    $ ./calc.py 123
    123

    $ ./calc.py "(add 12 12)"
    24

Expression syntax
-----------------

Since the expression is passed in as a command line argument, it is a string.
The syntax resembles [S-expressions][sexp] but the rules are simplified. An
expression can be in one of two forms:

### Integers

An integer is just a sequence of base 10 digits. For example:

    123

### Function calls

A function call takes the following form:

    (FUNCTION EXPR EXPR)

A function call is always delimited by parenthesis `(` and `)`.

The `FUNCTION` is one of `add` or `multiply`.

The `EXPR` can be any arbitrary expression, i.e. it can be further function
calls or integer expressions.

Exactly one space is used to separate each term.

For example:

    (add 123 456)

    (multiply (add 1 2) 3)

Assumptions
-----------

A list of assumptions you're allowed to make:

- Since numbers are specified by digits only, you don't have to deal with
  inputting negative numbers.

- Depending on your choice of language, you may have to pick a data type to
  represent your integers and calculations. Pick something that gives you at
  least 32 bits. None of the calculations will deal with numbers larger than
  that and you won't be penalized for not dealing with overflow.

- You can be pretty lax about error handling. Throwing an exception when in an
  invalid state is fine.

  The tested examples will always be well formed. That means that:

  - Parenthesis will always be balanced.
  - Only the `add` and `multiply` functions will be called.
  - There will always be a single space between the function arguments.

How my code works
-----------------

### evaluator.py

I start by evaluateing the inner-most layer of expression by finding the first closing bracket
and the closest opening bracket to it. Then, I work my way out layer by layer while replacing
evaluated expressions with their results. When there is no more closing brackets, the code stops
and returns the final answer.

### argParser.py

Parsing the command line argument into a list so that I can more conveniently iterating through
the whole expression.