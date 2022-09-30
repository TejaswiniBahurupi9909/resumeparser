from pyresparser import ResumeParser
import os
from docx import Document
import json
import spacy
import pyresparser
import nltk
#nltk.download('stopwords')
path = "D:/Internship/Recorem/Project"
os.chdir(path)
filename = 'D:/Internship/Recorem/data.json'
#filed='D:/Internship/Recorem/Project/swetha sc-RESUME.pdf'
try:
    doc = Document()
    def read_text_file(file_path):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            doc.add_paragraph(file.read())
            doc.save("text.docx")
            data = ResumeParser('text.docx').get_extracted_data()
            print(data)
            with open(filename, 'a') as file_object:
                print("Appending data")
                json.dump(data, file_object, indent=3)
            print("Data Appended")


    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".pdf"):
            file_path = f"{path}\{file}"

            # call read text file function
            read_text_file(file_path)
except:
    # data = ResumeParser(file).get_extracted_data()
    print("Error")