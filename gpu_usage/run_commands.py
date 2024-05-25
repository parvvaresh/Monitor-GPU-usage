from write_sh_file import write_sh_file
from run_in_screen import run_in_screen
import subprocess


def run_commands(sec : int) -> None:
    """
        write this update
    """
    script_path = write_sh_file(sec)
    
    subprocess.run(["chmod", "+x", script_path], check=True)    
    subprocess.run(["sudo", "apt-get", "update"], check=True)
    subprocess.run(["sudo", "apt-get", "install", "-y", "screen"], check=True)
    
    
    run_in_screen(script_path)