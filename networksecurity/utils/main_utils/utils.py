import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os
import sys
import numpy as np
import dill
import pickle



def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "r") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
"""
The function read_yaml_file(file_path: str) -> dict is used to read a YAML configuration file 
and convert it into a Python dictionary so your pipeline can use it programmatically. 
Internally, it opens the YAML file, and yaml.safe_load() parses the file’s structured text 
(like your columns and numerical_columns) into a dictionary stored in memory. This dictionary lets your 
data validation code easily access things like expected column names and types to verify your dataset. 
In short, it acts as a bridge between the YAML schema file (configuration) and your Python ML pipeline logic, 
making the pipeline flexible and configurable.
"""
def write_yaml_file(file_path:str,content:object,replace:bool = False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(file_path,content)
    except Exception as e:
        raise NetworkSecurityException(e,sys)