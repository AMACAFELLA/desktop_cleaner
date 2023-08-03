# Desktop Cleaner

This Python script helps to automatically clean up your desktop by moving files into folders named after their extensions in your Documents directory.

## How it works

The script uses the `watchdog` library to monitor your desktop for any changes. When a new file is added, it is automatically moved into a folder named after its file extension. If a file with the same name already exists in the destination folder, a timestamp is appended to the filename to prevent overwriting.

## How to use

### Prerequisites

- Python 3
- `watchdog` library. Install it using pip:
```python
pip install watchdog
```


### Running the script

1. Download the script and place it in any directory.
2. Run the script from a terminal:
python desktop_cleaner.py

3. Now, any file you add to your desktop will be automatically moved to an appropriate folder in your Documents directory.

### Customizing the script

The script is set to monitor the Desktop and move files to the Documents directory. If you want to change these directories, modify the `desktop_path` and `target_folder` variables in the script:

```python
desktop_path = os.path.expanduser("~/Desktop")  # Change this to your source directory
target_folder = os.path.expanduser("~/Documents")  # Change this to your target directory
```

### Compatibility

This script should work on any operating system (Windows, MacOS, Linux) that supports Python. The desktop and documents paths are set to common defaults, but can be customized as needed.

### License

This project is licensed under the MIT License.