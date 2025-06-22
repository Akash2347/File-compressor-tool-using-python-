import zipfile
import os

def compress_file(input_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isfile(input_path):
            zipf.write(input_path, os.path.basename(input_path))
            print(f"Compressed file: {input_path} -> {output_zip}")
        elif os.path.isdir(input_path):
            for root, dirs, files in os.walk(input_path):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, input_path)
                    zipf.write(full_path, arcname)
            print(f"Compressed folder: {input_path} -> {output_zip}")
        else:
            print("Invalid input path.")

def decompress_file(zip_path, extract_to):
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(extract_to)
            print(f"Extracted {zip_path} to {extract_to}")
    else:
        print("Invalid ZIP file.")

def main():
    print("File Compression Tool")
    print("1. Compress File/Folder")
    print("2. Decompress ZIP")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        path = input("Enter path to file or folder to compress: ")
        output = input("Enter name for output zip file (e.g., output.zip): ")
        compress_file(path, output)
    elif choice == '2':
        zip_path = input("Enter path to zip file: ")
        extract_path = input("Enter folder path to extract files to: ")
        decompress_file(zip_path, extract_path)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
