import requests

def download_part(url : str,
                  start_byte : int,
                  end_byte : int,
                  filename : str,
                  num_parts : int) -> None:
    
    headers = {"Range" : f"bytes={start_byte}-{end_byte}"}
    respones = requests.get(url, headers=headers, stream=True)
    
    with open(filename + f".part{num_parts}", "wb") as f:
        for chunk  in respones.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                
        
    