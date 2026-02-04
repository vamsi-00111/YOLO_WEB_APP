import logging
from pathlib import Path
import os
import datetime

def log():
        
        #creating logs
        logger=logging.getLogger(__name__)

        logger.setLevel(logging.DEBUG)
        
        #making directory
        dir=Path(__file__).parent/"logs"
        dir.mkdir(exist_ok=True,parents=True)
        
        #creating file path with timestamp 
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d")
        file_path=dir/f'{timestamp}.log'
        
        file_handler=logging.FileHandler(filename=file_path)
        
        file_formatter=logging.Formatter('[%(asctime)s] %(levelname)s:%(name)s:%(message)s')
        
        file_handler.setLevel(logging.DEBUG)
        
        file_handler.setFormatter(file_formatter)
        
        #adding file_handler to logger file
        
        logger.addHandler(file_handler)
        
        return logger
        
        
        
        
        
        



