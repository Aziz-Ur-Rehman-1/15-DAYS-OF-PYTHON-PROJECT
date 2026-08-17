import os
from docx2pdf import convert

def convert_single_file(docx_path):
    if not os.path.exists(docx_path):
        print(f"\nError: File '{docx_path}' not found!\n")
        return

    if not docx_path.lower().endswith('.docx'):
        print("\nError: Please provide a valid .docx file!\n")
        return

    try:
        pdf_path = docx_path.rsplit('.', 1)[0] + '.pdf'
        print(f"\nConverting '{docx_path}' to PDF...")
        convert(docx_path, pdf_path)
        print(f"Conversion complete! Saved as: '{pdf_path}'\n")
    except Exception as e:
        print(f"\nConversion Error: {e}\n")

def convert_batch_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"\nError: Folder '{folder_path}' not found!\n")
        return

    try:
        print(f"\nConverting all .docx files in '{folder_path}'...")
        convert(folder_path)
        print("Batch conversion completed successfully!\n")
    except Exception as e:
        print(f"\nBatch Conversion Error: {e}\n")

def main():
    while True:
        print("WORD TO PDF CONVERTER")
        print("1. Convert Single Word File (.docx ➔ .pdf)")
        print("2. Batch Convert Entire Folder")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            docx_file = input("Enter Word file path (e.g. document.docx): ").strip()
            if docx_file:
                convert_single_file(docx_file)
            else:
                print("\nPath cannot be empty!\n")
        elif choice == "2":
            folder_file = input("Enter folder path containing .docx files: ").strip()
            if folder_file:
                convert_batch_folder(folder_file)
            else:
                print("\nFolder path cannot be empty!\n")
        elif choice == "3":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Try again!\n")

if __name__ == "__main__":
    main() 