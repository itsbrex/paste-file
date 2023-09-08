import argparse
import os
import subprocess

import pyperclip


def get_finder_path() -> str:
    """
    Get the path of the current Finder window or the desktop if no windows are open.
    """
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


def get_args() -> argparse.Namespace:
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-ph', '--paste-here', action='store_true', help='Skip dialog prompt and use terminal input.')
    parser.add_argument('-f', '--folder', nargs='?', default=None, help='Optional subfolder of CWD to save the file in.')
    return parser.parse_args()


def get_file_path(args: argparse.Namespace, current_path: str) -> str:
    """
    Get the file path based on the provided arguments and current path.
    """
    file_name = input("Enter the full file name with extension: ")
    if args.folder:
        file_path = os.path.join(current_path, args.folder, file_name)
        os.makedirs(os.path.join(current_path, args.folder), exist_ok=True)
    else:
        file_path = os.path.join(current_path, file_name)
    return file_path


def main() -> None:
    args = get_args()
    clipboard_content = pyperclip.paste()

    if args.paste_here:
        current_path = os.getcwd()
        file_path = get_file_path(args, current_path)
    else:
        current_finder_path = get_finder_path()
        file_name = input("Enter the full file name with extension: ")
        file_path = os.path.join(current_finder_path, file_name)

    with open(file_path, 'w') as md_file:
        md_file.write(clipboard_content)

    relative_path = os.path.relpath(file_path, start=os.getcwd())
    print(f"File saved at: {relative_path}")
    subprocess.call(['cursor', relative_path])


if __name__ == "__main__":
    main()

