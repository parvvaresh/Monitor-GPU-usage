#!/bin/bash


LOGFILE="/home/reza/Desktop/logfile.csv"


if [ ! -f "$LOGFILE" ]; then
    echo "timestamp,name,utilization.gpu [%],utilization.memory [%]" >> "$LOGFILE"
fi


while true; do
    nvidia-smi --query-gpu=timestamp,name,utilization.gpu,utilization.memory --format=csv,noheader,nounits >> "$LOGFILE"
    sleep 60
done
