from write_sh_file import write_sh_file
from run_in_screen import run_in_screen
import subprocess


def run_commands(sec : int) -> None:
    """
        this code have 4 steps 
        1 -> create .sh file and write into path file csv for save result
        2 -> run commands 
           2.1 -> To run the script, you need to give execute permission to the file. Do this using the chmod command : chmod +x
           2.2 -> To run the script in the background (so that it continues to run after closing the terminal), you can use the screen tool
        3 -> Running the script in a screen session
    """
    script_path = write_sh_file(sec)
    
    subprocess.run(["chmod", "+x", script_path], check=True)    
    subprocess.run(["sudo", "apt-get", "update"], check=True)
    subprocess.run(["sudo", "apt-get", "install", "-y", "screen"], check=True)
    
    
    run_in_screen(script_path)