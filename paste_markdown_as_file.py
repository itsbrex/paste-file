import pyperclip
import os
import subprocess

def get_finder_path():
    script = '''
    tell application "Finder"
        if (count of Finder windows) is 0 then
            set thePath to POSIX path of (desktop as alias)
        else
            set front_folder to (folder of the front Finder window as alias)
            set thePath to POSIX path of front_folder
        end if
    end tell
    return thePath
    '''
    return subprocess.check_output(['osascript', '-e', script]).decode('utf-8').strip()

# from the terminal, run: python paste_markdown_as_file.py
# def main():
#     clipboard_content = pyperclip.paste()
#     current_finder_path = get_finder_path()
#     file_name = input("Enter a name for the markdown file (without .md extension): ")
#     file_path = os.path.join(current_finder_path, f"{file_name}.md")

#     with open(file_path, 'w') as md_file:
#         md_file.write(clipboard_content)

#     print(f"File saved as: {file_path}")

import json

def main():
    clipboard_content = pyperclip.paste()
    current_finder_path = get_finder_path()

    script = '''
    set dialog_result to display dialog "Enter a name for the markdown file (without .md extension):" default answer "" with title "File Name"
    return "{\\"text returned\\": \\"" & text returned of dialog_result & "\\"}"
    '''

    result = subprocess.check_output(['osascript', '-e', script]).decode('utf-8').strip()
    file_name = json.loads(result)['text returned']

    file_path = os.path.join(current_finder_path, f"{file_name}.md")

    with open(file_path, 'w') as md_file:
        md_file.write(clipboard_content)

    print(f"File saved as: {file_path}")
    

if __name__ == "__main__":
    main()
