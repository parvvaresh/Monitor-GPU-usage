Here is the **README** file for your script:

---

# GPU and CPU Utilization Logger

This Bash script logs GPU and CPU utilization data into a CSV file at user-specified intervals. It uses NVIDIA's `nvidia-smi` command to gather GPU data and `mpstat` for CPU utilization. This script is useful for monitoring system performance over time.

---

## Features
- Logs timestamp, GPU name, GPU utilization, memory utilization, and CPU utilization.
- Allows users to specify the file path for saving the logs.
- Lets users set the interval for collecting and saving the data.
- Outputs data in CSV format, compatible with tools like Excel and Python.

---

## Prerequisites
1. **NVIDIA GPU**:
   - Ensure you have an NVIDIA GPU with the `nvidia-smi` tool installed (typically included with NVIDIA drivers).

2. **mpstat**:
   - Install the `sysstat` package for CPU monitoring.
   - On Ubuntu/Debian:
     ```bash
     sudo apt-get install sysstat
     ```
   - On CentOS/RHEL:
     ```bash
     sudo yum install sysstat
     ```

---

## Usage

### Step 1: Make the script executable
```bash
chmod +x logger.sh
```

### Step 2: Run the script
```bash
./logger.sh
```

### Step 3: Provide the required inputs
- **CSV File Path**: Specify the file where the logs will be saved. If the file does not exist, it will be created with appropriate headers.
- **Sampling Interval**: Enter the interval in seconds between data collection cycles.

---

## Example
If you provide:
- File path: `/home/user/logs/utilization.csv`
- Sampling interval: `5` seconds

The script will append rows to `/home/user/logs/utilization.csv` every 5 seconds, with entries like:
```csv
timestamp,name,utilization.gpu [%],utilization.memory [%],cpu.utilization [%]
2024-12-21 10:15:30,NVIDIA GeForce RTX 3080,85,70,20
2024-12-21 10:15:35,NVIDIA GeForce RTX 3080,80,65,25
```

---

## Notes
- **Stop the Script**: To stop the script, press `Ctrl+C`.
- **Performance Impact**: The script runs lightweight monitoring commands (`nvidia-smi` and `mpstat`). However, frequent sampling intervals (e.g., 1 second) may cause a slight system overhead.
- **File Size**: Over time, the log file can grow large. Consider periodically archiving or clearing it if needed.

---

## Troubleshooting

1. **Command not found: `nvidia-smi`**:
   - Ensure that you have an NVIDIA GPU and the drivers are properly installed.

2. **Command not found: `mpstat`**:
   - Install the `sysstat` package using the instructions above.

3. **Permission Denied**:
   - Ensure the script has execute permissions:
     ```bash
     chmod +x logger.sh
     ```

4. **Incorrect Interval Input**:
   - The `sleep` command requires a numeric interval. Ensure that you enter a valid number.

---

## License
This script is provided "as is" without any warranties. Feel free to modify and use it as needed.

---

Let me know if you need additional details or adjustments!
