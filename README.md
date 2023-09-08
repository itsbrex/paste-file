# paste-file

`paste-file` is a Python script that allows you to save the content of your clipboard directly to a file. This can be useful for storing information copied from different sources or for quickly backing up data currently stored in your clipboard.

This script is designed with MacOS users in mind and uses AppleScript to interact with Finder for path retrieval and dialog display.

## Installation

The script depends on several Python libraries. You can install them using pip:

```shell
python -m pip install -r requirements.txt
```

## Usage

You can run the script from the terminal as follows:

```shell
python paste-file.py [-ph/--paste-here] [-f/--folder <folder_name>]
```


### Arguments

- `-ph` or `--paste-here`: This flag will make the script save the clipboard content to a file in the terminal's current directory without popping up a dialog box. The script will instead ask you to enter the file name directly into the terminal.

- `-f` or `--folder <folder_name>`: This optional argument allows you to specify a subfolder in the current working directory (CWD) where the file will be saved. If the specified folder doesn't exist, it will be created.

If no arguments are given, the script will pop up a dialog box asking for the file name and will save the clipboard content in the currently active Finder window's directory. If no Finder windows are open, it will save the file on the desktop.

The script will then print the relative path of the saved file and open it in your default editor.

- `-ph` or `--paste-here`: This flag will make the script save the clipboard content to a file in the terminal's current directory without popping up a dialog box. The script will instead ask you to enter the file name directly into the terminal.

- `-f` or `--folder <folder_name>`: This optional argument allows you to specify a subfolder in the current working directory (CWD) where the file will be saved. If the specified folder doesn't exist, it will be created.

If no arguments are given, the script will pop up a dialog box asking for the file name and will save the clipboard content in the currently active Finder window's directory. If no Finder windows are open, it will save the file on the desktop.

## Contributors

Contributions are welcomed. This project follows the all-contributors spec. ([emoji key](https://github.com/all-contributors/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/github/all-contributors/itsbrex/paste-file?color=ee8449&style=flat-square)](#contributors)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## License

MIT © [itsbrex](https://github.com/itsbrex)

If you found this project interesting, please consider [sponsoring me](https://github.com/sponsors/itsbrex) or <a href="https://twitter.com/itsbrex">following me on twitter <img src="https://storage.googleapis.com/saasify-assets/twitter-logo.svg" alt="twitter" height="24px" align="center"></a>
