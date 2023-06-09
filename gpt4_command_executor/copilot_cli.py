#!/usr/bin/env python3
import subprocess
import sys
from gpt4_command_executor import config
from gpt4_command_executor import executor
from gpt4_command_executor.gpt3 import revise_command, generate_command, generate_explanation


def copilot_cli(prompt):
    command = config.get_terminal_command(prompt)
    return executor.execute_command(command)


def main():
    if len(sys.argv) < 2:
        print("Usage: q '?? command request'")
        sys.exit(1)

    query = sys.argv[1]
    command = generate_command(query)
    print(f"Generated command: {command}")

    while True:
        user_input = input("Do you want to execute this command? (y/n/r/e) for revision or explanation: ")

        if user_input.lower() == 'y':
            subprocess.run(command, shell=True)
            break
        elif user_input.lower() == 'n':
            break
        elif user_input.lower() == 'r':
            command = revise_command(command)
            print(f"Revised command: {command}")
        elif user_input.lower() == 'e':
            explanation = generate_explanation(command)
            print(f"Explanation: {explanation}")
        else:
            print("Invalid input, please enter 'y', 'n', 'r', or 'e'.")


if __name__ == "__main__":
    main()
