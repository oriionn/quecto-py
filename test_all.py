import subprocess

commands = [
    "python ./tests/short.py",
    "python ./tests/short_with_password.py",
    "python ./tests/unshort.py",
    "python ./tests/unshort_with_password.py",
    "python ./tests/ivi_valid.py",
    "python ./tests/ivi_invalid.py"
]


def execute_commands(commands):
    for command in commands:
        print(f"Executing script: {command.split(' ')[1]}")
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            print(result)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
        print("=" * 40)


execute_commands(commands)
