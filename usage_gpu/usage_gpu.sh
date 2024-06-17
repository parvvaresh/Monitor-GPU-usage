
#!/bin/bash



echo please enter a path file for saved csv file :
read LOGFILE



if [ ! -f "$LOGFILE" ]; then    echo "timestamp,name,utilization.gpu [%],utilization.memory [%]" >> "$LOGFILE"
fi


echo please enter secend for saved  (s) :
read time

while true; do
    nvidia-smi --query-gpu=timestamp,name,utilization.gpu,utilization.memory --format=csv,noheader,nounits >> "$LOGFILE"
    sleep time
done
