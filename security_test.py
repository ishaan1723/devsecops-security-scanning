import subprocess


def run_command():
    subprocess.run(
        ["python", "--version"],
        check=True
    )


run_command()