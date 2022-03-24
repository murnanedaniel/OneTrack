import os

def list_files(dir):
    """
    List files from directory dir 
    """
    files = os.listdir(dir)
    files = [os.path.join(dir, f) for f in files]
    files = sorted(files)
    return files