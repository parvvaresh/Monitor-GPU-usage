# GPU Usage Monitor

This repository contains a Python script that monitors GPU usage and logs the data into a CSV file at regular intervals. The script leverages `nvidia-smi` to query GPU statistics and runs in the background using the `screen` utility.

## Project Structure

```
.
├── _gpu_usage
│   ├── install_screen.py
│   ├── run_commands.py
│   ├── run_in_screen.py
│   ├── write_sh_file.py
├── report_server
    ├── report_server.py
├── gpu_usage.py
└── README.md
```

### Files and Their Functions

- **_gpu_usage/install_screen.py**: Installs the `screen` utility.
- **_gpu_usage/run_commands.py**: Executes necessary commands to set up and run the monitoring script.
- **_gpu_usage/run_in_screen.py**: Runs the monitoring script in a detached `screen` session.
- **_gpu_usage/write_sh_file.py**: Creates a shell script that logs GPU usage data.
- **gpu_usage.py**: Main script that coordinates the process.

## Prerequisites

- Python 3.x
- NVIDIA GPU with `nvidia-smi` installed
- `screen` utility (the script will install it if not present)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/parvvaresh/Monitor-GPU-usage
   cd Monitor-GPU-usage
   ```

2. **Run the Script**:
   ```bash
   python3 gpu_usage.py
   ```
   The script will prompt you to enter the interval (in seconds) at which you want to log the GPU usage data.

## Usage

1. **Enter the Logging Interval**:
   When prompted, specify how frequently you want to save the GPU usage data (in seconds).

2. **Background Logging**:
   The script will:
   - Make the logging shell script executable.
   - Install `screen` if it is not already installed.
   - Run the logging shell script in a detached `screen` session named `usage_gpu`.

3. **Access the Log File**:
   The GPU usage data will be logged in a file named `result.csv` in the same directory as the script.


## report server
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/parvvaresh/Monitor-GPU-usage
   cd Monitor-GPU-usage
   ```

2. **Use class**:
   ```python
   from report_server.report_server import report_server
   rs = report_server(df) # data frame who save it in your server
   rs.get_report_plot()
   rs.get_text_report()
   ```

   ```bash
   python3 gpu_usage.py
   ```


## Contributing

Contributions are welcome. Please fork the repository and submit a pull request for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.