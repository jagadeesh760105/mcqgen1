import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
import streamlit as st  
from langchain_community.callbacks.manager import get_openai_callback
from src.mcqgenerator.logger import logging

#loading json file
with open('C:\Users\JAGADEESHNAIKPALTHYA\mcqgen1\responce.json','r') as file:
    RESPONSE_JSON= json.load(file)
    
