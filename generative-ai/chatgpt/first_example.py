import openai

def process_plugin_command(command):
    # Split the command into components
    parts = command.split()
    if len(parts) != 3:
        return "Invalid command. Please provide two numbers and an operator separated by spaces."

    try:
        num1 = float(parts[0])
        num2 = float(parts[2])
    except ValueError:
        return "Invalid numbers provided."

    operator = parts[1]
    result = None

    # Perform the arithmetic operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero."

    return f"The result is: {result}"

def process_plugin(prompt):
    # Process the plugin command based on the prompt
    if prompt.startswith('calculate'):
        return process_plugin_command(prompt[len('calculate'):].strip())
    else:
        return "Unknown command. Please start your command with 'calculate'."

def run_plugin():
    while True:
        # Get user input
        prompt = input("Enter your command: ")

        # Exit if user enters 'quit'
        if prompt.strip().lower() == 'quit':
            break

        # Process the plugin command
        response = process_plugin(prompt)
        print(response)

if __name__ == '__main__':
    run_plugin()



