import subprocess

def run_in_screen(script_path : str) -> None:
    subprocess.run(["screen", "-S", "usage_gpu", "-d", "-m", script_path], check=True)
    print("Started the script in a new screen session named 'usage_gpu'.")