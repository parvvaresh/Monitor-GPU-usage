## Download Manager

This is a simple Python script that allows you to download a file from a URL in multiple parts concurrently, merge them, and save the complete file locally. This can be useful when downloading large files, as it allows for faster downloads by utilizing multiple connections.

### How to Use

1. **Clone the Repository**: Clone or download the repository containing the code.

2. **Navigate to the `tool` directory**: This directory contains the scripts necessary for downloading and managing files.

3. **Run the `download_manager.py` script**: This script acts as the main entry point for the download manager. Execute the following command:

    ```bash
    python download_manager.py
    ```

4. **Follow the Instructions**: You will be prompted to enter the URL of the file you want to download, the number of parts to download the file in, and the desired filename for the downloaded file.

5. **Monitor Progress**: During the download process, progress updates will be displayed, showing the status of each part being downloaded.

6. **Completion**: Once all parts have been downloaded and merged, you will find the complete file saved locally with the specified filename.

### Explanation of Code

#### `download_file_in_parts.py`
- This script contains a function `download_file_in_parts` that orchestrates the download process.
- It calculates the size of each part based on the total size of the file and the number of parts specified.
- Utilizes threading to download each part concurrently.
- Calls the `download_part` function for each part.

#### `download_part.py`
- This script contains the `download_part` function responsible for downloading a specific part of the file.
- Uses HTTP range requests to download a specific portion of the file.
- Progress updates are sent to a callback function if provided.

#### `merge_files.py`
- This script contains a function `merge_files` that merges all downloaded parts into a single file.
- It sequentially reads each part file and writes its content into the final file.
- Removes the individual part files after merging.

#### `status_callback.py`
- This script defines a simple callback function `status_callback` to display progress updates during the download process.

#### `download_manager.py`
- This script serves as the entry point for the download manager.
- Imports necessary functions from other scripts (`download_file_in_parts`, `merge_files`, `status_callback`) and orchestrates the download process based on user input.

### Command Line Usage

To run the download manager from the command line, follow these steps:

1. Open a terminal.
2. Navigate to the directory containing the `download_manager.py` script.
3. Run the following command:

    ```bash
    python download_manager.py
    ```

4. Follow the on-screen instructions to enter the URL, number of parts, and filename for the download.

5. Monitor progress updates in the terminal until the download is complete.

6. Once finished, locate the downloaded file in the same directory with the specified filename.

### Dependencies

This project requires the `requests` library, which can be installed via pip:

```bash
pip install requests
```

### Note

- Ensure you have sufficient disk space available to accommodate the downloaded file.
- Running multiple instances of the download manager simultaneously may cause conflicts or unexpected behavior.
- This download manager is primarily intended for educational purposes and may not be suitable for large-scale or production use.
