"""
-*- coding: utf-8 -*-
========================
Python Lazy Junk Files Organizer
========================
========================
"""
import os
from pathlib import Path


DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "MARKUP": [".md"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
               ".heif", ".psd"], 
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
               ".qt", ".mpg", ".mpeg", ".3gp",".mkv"], 
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
                  "pptx",".md",".pages",".numbers"], 
    "ARCHIVES": [".a", ".ar", ".arh",".tar",".tar.bz2",".tar.gz",".cpio", ".tar", ".gz", ".rz", ".7z", 
                 ".rar", ".xar", ".zip",".xz",".pkg",".deb",".rpm"], 
    "DISKIMAGE":[".iso",".img",".vcd",".dmg"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
    "PLAINTEXT": [".txt", ".in", ".out",".csv",".log"],
    "POWERSHELL": [".ps1",".psm1",".psd1"],
    "PDF": [".pdf"], 
    "PYTHON": [".py",".pyi",".pyc"], 
    "XML": [".xml",".fxml"], 
    "EXECUTABLE": [".exe",".run"], 
    "SHELL": [".sh"],
    "DATABASE":[".db",".sql"],
    "C#" :[".cs"],
    "C++": [".cpp"],
    "C": [".c"],
    "GO": [".go"],
    "YAML": [".yaml"],
    "JSON": [".json"],
    "ASP Classic": [".asp"],
    "ASP_NET": [".aspx", ".axd", ".asx", ".asmx", ".ashx"],
    "CSS": [".css"],
    "Coldfusion": [".cfm"],
    "Erlang": [".yaws"],
    "Flash": [".swf"],
    "Java": [".jar",".java",".jsp", ".jspx", ".wss", ".do", ".action"],
    "Kotlin": [".kt",".kts",".ktm"],
    "JavaScript": [".js"],
    "TypeScript": [".ts"],
    "Rust": [".rs",".rlib"],
    "Toml": [".toml"],
    "Travis": [".travis"],
    "Perl": [".pl"],
    "PHP": [".php", ".php4", ".php3", ".phtml"],
    "Ruby": [".rb", ".rhtml"],
    "SSI": [".shtml"],
    "XML": [".xml", ".rss", ".svg"],
    "APPS": [".app",".ipa",".apk"],
    "LINKS":[".webloc",".lnk"]

}


FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))

    try:
        os.mkdir("OTHER-FILES")
    except:
        pass

    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/OTHER-FILES/' + str(Path(dir)))
        except:
            pass


if __name__ == "__main__":
    organize_junk()