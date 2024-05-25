from _gpu_usage.run_commands import run_commands
from _gpu_usage.write_sh_file import write_sh_file


def gpu_usage():
    sec = int(input())
    path_script = write_sh_file(sec)    
    
    run_commands(path_script)


gpu_usage()