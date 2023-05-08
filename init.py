import os
import glob
import shutil

# dictionary mapping each extension with its corresponding folder
# For example, 'jpg', 'png', 'ico', 'gif', 'svg' files will be moved to 'images' folder
# feel free to change based on your needs
extensions = {
    "jpg": "images",
    "png": "images",
    "ico": "images",
    "gif": "images",
    "svg": "images",
    "sql": "sql",
    "exe": "programs",
    "msi": "programs",
    "pdf": "pdf",
    "xlsx": "excel",
    "csv": "excel",
    "rar": "archive",
    "zip": "archive",
    "gz": "archive",
    "tar": "archive",
    "docx": "word",
    "torrent": "torrent",
    "txt": "text",
    "ipynb": "python",
    "py": "python",
    "pptx": "powerpoint",
    "ppt": "powerpoint",
    "mp3": "audio",
    "wav": "audio",
    "mp4": "video",
    "m3u8": "video",
    "webm": "video",
    "ts": "video",
    "json": "json",
    "css": "web",
    "js": "web",
    "html": "web",
    "apk": "apk",
    "sqlite3": "sqlite3",
      'swf': 'Adobe Flash file',
    'sys': 'System file',
    'bnf': 'Backus-Naur Form file',
    'mts': 'AVCHD video file',
    'nix': 'Nix package file',
    'bsd': 'BSD Unix configuration file',
    'html': 'Hypertext Markup Language file',
    'closure-compiler': 'Closure Compiler file',
    'css': 'Cascading Style Sheet file',
    'php': 'PHP script file',
    'log': 'Log file',
    'msi': 'Windows Installer package',
    'crdownload': 'Chrome Partially Downloaded file',
    'sqlite3': 'SQLite database file',
    'ipynb': 'Jupyter Notebook file',
    'flow': 'Flow type declaration file',
    'cat': 'Catalog file',
    'ini': 'Initialization file',
    'inf': 'Setup Information file',
    'exe': 'Executable file',
    'cmd': 'Command script file',
    'cts': 'Conversation Translation Service file',
    'lock': 'Lock file',
    'mdown': 'Markdown file',
    'coffee': 'CoffeeScript file',
    'bak': 'Backup file',
    'map': 'Source Map file',
    'zip': 'Compressed file archive',
    'dat': 'Data file',
    'bin': 'Binary file',
    'conf': 'Configuration file',
    'jison': 'Jison grammar file',
    'dll': 'Dynamic Link Library file',
    'markdown': 'Markdown file',
    'esprima': 'Esprima JavaScript parser file',
    'pdf': 'Portable Document Format file',
    'md': 'Markdown file',
    'sh': 'Shell script file',
    '1': 'Manual page file',
    'tsbuildinfo': 'TypeScript build information file',
    'yml': 'YAML file',
    'rar': 'RAR compressed archive',
    'lnk': 'Windows Shortcut file',
    'def': 'Module definition file',
    'wps': 'Microsoft Works document file',
    'mem': 'Memory dump file',
    'ts': 'TypeScript file',
    'txt': 'Text file',
    'pegjs': 'PEG.js grammar file',
    'mjs': 'ECMAScript module file',
    'docx': 'Microsoft Word document file',
    'applescript': 'AppleScript file',
    'js': 'JavaScript file',
    'license': 'License file',
    'opts': 'Options file',
    'csv': 'Comma-Separated Values file',
    'jpeg': 'JPEG image file',
    'doc': 'Microsoft Word document file',
    'json': 'JavaScript Object Notation file',
    'ico': 'Icon file',
    'jst': 'JavaScript Template file',
    'cjs': 'CommonJS module file',
    'online': 'Online file',
    'wasm': 'WebAssembly binary file',
    'jpg': 'JPEG image file',
    'ejs': 'Embedded JavaScript file',
    'sql': 'Structured Query Language file'
}

path = r"C:\Users\Alus"
    # setting verbose to 1 (or True) will show all file moves
    # setting verbose to 0 (or False) will show basic necessary info
verbose = True
for extension, folder_name in extensions.items():
        # get all the files matching the extension
        files = glob.glob(os.path.join(path, f"*.{extension}"))
        print(f"[*] Found {len(files)} files with {extension} extension")
        if not os.path.isdir(os.path.join(path, folder_name)) and files:
            # create the folder if it does not exist before
            print(f"[+] Making {folder_name} folder")
            os.mkdir(os.path.join(path, folder_name))
        for file in files:
            # for each file in that extension, move it to the correponding folder
            basename = os.path.basename(file)
            dst = os.path.join(path, folder_name, basename)
            if verbose:
                print(f"[*] Moving {file} to {dst}")
            shutil.move(file, dst)
