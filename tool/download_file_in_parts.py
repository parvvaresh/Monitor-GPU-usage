import requests
import threading

from .download_part import download_part



def download_file_in_parts(url : str,
                           num_parts : int,
                           filename : str):
    response = requests.head(url)
    total_size = int(response.headers.get('content-length', 0))
    part_size = total_size // num_parts
    theards = []
    
    for i in range(num_parts):
        start_byte = i * part_size
        end_byte = None
        if i < num_parts - 1:
            end_byte = start_byte + part_size - 1
        else:
            end_byte = total_size - 1
    
    
        theard = threading.Thread(
            target=download_part,
            args=(url, start_byte, end_byte, filename, i)
        )
        theards.append(theard)
        theard.start()
        
        
    
    for _thread in theards:
        _thread.join()
    
                