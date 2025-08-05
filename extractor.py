# TO parse pdf to text

import pdfplumber
import os
from tkinter import Tk
from tkinter import filedialog

def extract_pdf(file_path):
    text = ''
    with pdfplumber.open(file_path) as f:
        for page in f.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text+ '\n'
            else:
                print('Page_text has Nothing')
    return text

def select_folder_gui():
    root = Tk()
    root.withdraw()  # Hide main window
    folder_path = filedialog.askdirectory(title="Select Resume Folder")
    return folder_path


def parse_resumes(folder_path):
    parsed = {}
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            text = extract_pdf(path)
            parsed[file] = text
            print(f"\nFrom {file}:\n{text[:300]}...\n")
    return parsed


if __name__ == '__main__':
    folder = select_folder_gui()
    if folder:
        parse_resumes(folder)
    else:
        print("⚠️ No folder selected.")