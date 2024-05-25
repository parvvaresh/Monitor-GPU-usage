import subprocess

def install_screen():

    
    subprocess.run(["sudo", "apt-get", "install", "-y", "screen"], check=True)