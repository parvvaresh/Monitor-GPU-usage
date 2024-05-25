import os
def write_sh_file(sec : int) -> str:
    
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    
    data = f"""
#!/bin/bash


LOGFILE="{current_directory}/result.csv"


if [ ! -f "$LOGFILE" ]; then\
    echo "timestamp,name,utilization.gpu [%],utilization.memory [%]" >> "$LOGFILE"
fi


while true; do
    nvidia-smi --query-gpu=timestamp,name,utilization.gpu,utilization.memory --format=csv,noheader,nounits >> "$LOGFILE"
    sleep {int(sec)}
done
    """

    script_path = os.path.join(current_directory, "usage_gpu.sh")
    
    with open(script_path, "w") as script_file:
        script_file.write(data)
    
    return script_path
