import zipfile

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive(r"D:\Coding Related\Udemy\Python Course\bonuses\compressed.zip", r"D:\Coding Related\Udemy\Python Course\bonuses\new")
