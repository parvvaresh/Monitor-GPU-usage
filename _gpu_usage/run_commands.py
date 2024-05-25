from .run_in_screen import run_in_screen
from .install_screen import install_screen
import subprocess


def run_commands(script_path : str) -> None:
    """
        this code have 4 steps 
        1 -> run commands 
           1.1 -> To run the script, you need to give execute permission to the file. Do this using the chmod command : chmod +x
           1.2 -> To run the script in the background (so that it continues to run after closing the terminal), you can use the screen tool
        2 -> Running the script in a screen session
    """
    
    subprocess.run(["chmod", "+x", script_path], check=True)    
    install_screen()
    
    
    run_in_screen(script_path)