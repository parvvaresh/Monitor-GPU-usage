#!/bin/bash


# prompt for csv file path

echo "please enter path for the saved CSV file : "
read LOGFILE



# check if the file exists : if not create it with header

if [! -f "$LOGFILE"]; then
    echo "timestamp,name,utilization.gpu [%],utilization.memory [%],cpu.utilization [%]" >> "$LOGFILE"
    fi



# Prompt for sampling interval in seconds
echo "Please enter interval (seconds) for saving:"
read time



while true; do
    # Get GPU data
    gpu_data=$(nvidia-smi --query-gpu=timestamp,name,utilization.gpu,utilization.memory --format=csv,noheader,nounits)
    
    # Get CPU utilization (average of all cores)
    cpu_util=$(mpstat 1 1 | awk '/Average/ {print 100 - $NF}')
    
    # Combine GPU and CPU data and write to log file
    while IFS= read -r line; do
        echo "$line,$cpu_util" >> "$LOGFILE"
    done <<< "$gpu_data"
    
    # Wait for the specified interval
    sleep "$time"
done
