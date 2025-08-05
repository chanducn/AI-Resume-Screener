import os
from tkinter import Tk,filedialog

def get_job_desc(): # As a input
    print("📝 Paste the job description below (Press ENTER twice to finish):\n")
    lines = []
    while True:
        line = input()
        if line.strip() == '':
            break
        lines.append(line)
    return '\n'.join(lines)

def load_job_desc():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Job Description (.txt) file",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path and os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    else:
        print("❌ No file selected or file not found.")
        return ""
    

def get_job_description():
    print("\n📌 Choose how you want to provide the job description:\n")
    print("1. Paste manually")
    print("2. Load from a .txt file\n")


    choice = input("Enter your choice (1 or 2) ").strip()

    if choice == '1':
        return get_job_desc()
    elif choice == '2':
        return load_job_desc()
    else:
        print("⚠️ Invalid choice. Defaulting to manual input.")
        return get_job_desc()
    
if __name__ == '__main__':
    job_text = get_job_description()
    print("\n✅ Job Description Loaded:\n")
    print(job_text[:1000])  # Preview first 1000 characters

    with open("job_description.txt", "w", encoding="utf-8") as f:
        f.write(job_text)
