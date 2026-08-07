import os
from py_compile import main
import shutil

# Extension map for sorting files based on their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", "xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Media": [".mp3", ".wav", ".mp4", ".avi", ".mkv"],
    "Code_and_Scripts": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
} 

def organize_files(target_path):
    if not os.path.exists(target_path):
        print(f"The specified path '{target_path}' does not exist.")
        return
    print(f"\nOrganizing files in: {target_path}\n")

    files = [f for f in os.listdir(target_path) if os.path.isfile(os.path.join(target_path, f))]

    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        moved = False

        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_path = os.path.join(target_path, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                shutil.move(os.path.join(target_path, file), os.path.join(category_path, file))
                print(f"Moved '{file}' to '{category}'")
                moved = True
                break

        # If not moved and has an extension, move to Others
        if not moved and file_extension != "":
            other_dir = os.path.join(target_path, "Others")
            if not os.path.exists(other_dir):
                os.makedirs(other_dir)
            shutil.move(os.path.join(target_path, file), os.path.join(other_dir, file))
            print(f"Moved '{file}' to 'Others'")
            
        print(f"Moved '{file}' to 'Others'")

    print("\nFile organization complete.")

def main():
    print("=" * 40)  
    print("Welcome to the File Organizer!")
    print("=" * 40)

    folder_path = input("Enter the path of the folder you want to organize: ").strip()
    organize_files(folder_path)

if __name__ == "__main__":
    main()
        

