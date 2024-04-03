import os

def merge_files(filename : str,
                num_parts : int) -> None:
    with open(filename, "wb") as f:
        for i in range(num_parts):
            part_file = filename + f".part{i}"
            with open(part_file, "rb") as part:
                f.write(part.read())
            os.remove(part_file)