from tool.download_file_in_parts import download_file_in_parts
from tool.merge_files import merge_files
from tool.status_callback import status_callback

def download_manger() -> None:
    url = input("please enter a <URL> : ")
    num_parts = int(input("please enter number of parts : "))
    filename =  input("please enter a filename like a <<test.pdf>>: ")
    download_file_in_parts(url, num_parts, filename, status_callback)
    merge_files(filename, num_parts)
    
download_manger()