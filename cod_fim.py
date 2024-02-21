import pandas as pd 
import numpy as np
from datetime import datetime 
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches
from docx import Document

movies_metadata = pd.read_csv("movies_metadata.csv")
movies = movies_metadata[["id", "original_language", "original_title", "overview", "release_date", "status"]][:10000]