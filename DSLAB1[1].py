def PrefixToPostfix(input_file):
    # Open the file for reading
    with open(input_file, 'r') as f:
        
        # Print the input file
        print(f"Processing file: {input_file}")
        print(f.read())
        f.seek(0)  # Return to the beginning of the file

        # Read the non-blank lines of the file
        non_blank_lines = [line.strip() for line in f if line.strip()]

    # Process the non-blank lines
    for i, line in enumerate(non_blank_lines):
        # Initialize error flag and error messages list for current line
        error_flag = False
        error_messages = []

        # Skip empty lines
        if not line:
            continue

        # Check for spaces in the line
        if ' ' in line:
            error_messages.append(f"Error [{i}]: Invalid expression - spaces not allowed")
            error_flag = True

        # Strip the newline character from the end of the line
        line = line.rstrip()

        # Stack for storing operands
        stack = []

        operators = set(['+', '-', '*', '/', '$', '^'])

        # Reversing the order
        line = line[::-1]

        # iterating through individual tokens
        for j, token in enumerate(line):

            # if token is operator
            if token in operators:

                # check if there are at least two operands in the stack
                if len(stack) < 2:
                    error_messages.append(f"Error [{i}]: Not enough operands for operator: {token}")
                    error_flag = True
                    break

                # pop 2 elements from stack
                a = stack.pop()
                b = stack.pop()

                # check if operator is defined
                if token == '^':
                    error_messages.append(f"Error [{i}]: Invalid expression - {token} not defined as operator in program guidelines")
                    error_flag = True
                    break

                # concatenate them as operand1 + operand2 + operator
                temp = a+b+token
                stack.append(temp)

            # else if operand
            else:
                stack.append(token)

        # check if there is exactly one element in the stack
        if len(stack) != 1:
            error_messages.append(f"Error [{i}]: Invalid expression")
            error_flag = True

        # if error encountered, print the first error message for that line
        if error_flag:
            print(error_messages[0])
        else:
            print(stack[-1])

# Call the function with the input file as argument
PrefixToPostfix('Required_Input.txt')
print('\n')
PrefixToPostfix('Additional_Input.txt')















