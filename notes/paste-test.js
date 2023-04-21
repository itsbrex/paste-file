import pyperclip
import os
import subprocess
import json
import argparse

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

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ph', '--paste-here', action='store_true', help='Skip dialog prompt and use terminal input.')
    parser.add_argument('subfolder', nargs='?', default=None, help='Optional subfolder for saving the file.')
    return parser.parse_args()

def main():
    args = get_args()
    clipboard_content = pyperclip.paste()

    if args.ph:
        current_path = os.getcwd()
        file_name = input("Enter the full file name with extension: ")
        if args.subfolder:
            file_path = os.path.join(current_path, args.subfolder, file_name)
            os.makedirs(os.path.join(current_path, args.subfolder), exist_ok=True)
        else:
            file_path = os.path.join(current_path, file_name)
    else:
        current_finder_path = get_finder_path()
        script = '''
        set dialog_result to display dialog "Enter the full file name with extension:" default answer "" with title "File Name"
        return "{\\"text returned\\": \\"" & text returned of dialog_result & "\\"}"
        '''
        result = subprocess.check_output(['osascript', '-e', script]).decode('utf-8').strip()
        file_name = json.loads(result)['text returned']
        file_path = os.path.join(current_finder_path, file_name)

    with open(file_path, 'w') as md_file:
        md_file.write(clipboard_content)

    print(f"File saved as: {file_path}")

if __name__ == "__main__":
    main()
