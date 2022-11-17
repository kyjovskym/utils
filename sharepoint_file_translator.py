from pathlib import Path
import os
import logging

forbiden_chars = ['"', '*', ':', '<', '>', '?', '/', '\\', '|']

def rename_path_for_sharepoint(root_dir: str):
    """
        Converts a path to a format that is compatible with Sharepoint.
    """
    for subdir, dirs, files in os.walk(root_dir,topdown=False):

        for dir in dirs:
            old_dir = dir
            dir = dir.strip()
            for char in forbiden_chars:
                dir = dir.replace(char, '_')
            os.rename(os.path.join(subdir, old_dir), os.path.join(subdir, dir))


        for file in files:

            if [e for e in forbiden_chars if e in file]:
                logging.info(f"File {file} contains forbiden characters. Renaming.")
                # Keep suffixes
                basename = Path(file).stem
                suffix = Path(file).suffix
                old_file = file
                file = basename.strip()
                for char in forbiden_chars:
                    file = file.replace(char, '_')
                os.rename(os.path.join(subdir, old_file), os.path.join(subdir, file.with_suffix(suffix)))



if __name__ == "__main__":
    root_dir = os.path.join(os.getcwd(), "test_files")
    print(rename_path_for_sharepoint(root_dir))
