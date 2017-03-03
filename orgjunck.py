"""
-*- coding: utf-8 -*-
========================
Python Lazy Junk Files Organizer
========================
Developed by: Chirag Rathod (Srce Cde)
Email: chiragr83@gmail.com
========================
"""

import os

dir = ['IMAGE Files', 'DOC Files', 'PY Files', 'VIDEO Files',
       'COMPRESS Files', 'HTML Files', 'TXT Files', 'PDF Files',
       'XML Files', 'AUDIO Files']

IMG_FORMAT = ['.JPEG', '.JPG', '.TIFF', '.GIF', '.BMP', '.PNG', '.BPG', 'SVG',
              '.HEIF', '.PSD']

VID_FORMAT = ['.AVI', '.FLV', '.WMV', '.MOV', '.MP4', '.WEBM', '.VOB', '.MNG',
              '.QT', '.MPG', '.MPEG', '.3GP']

DOC_FORMAT = ['.OXPS', '.EPUB', '.PAGES', '.DOCX', '.DOC', '.FDF', '.ODS',
              '.ODT', '.PWI', '.XSN', '.XPS', '.DOTX', '.DOCM', '.DOX',
              '.RVG', '.RTF', '.RTFD', '.WPD', '.XLS', '.XLSX', '.PPT', 'PPTX']

ZIP_FORMAT = ['.A', '.AR', '.CPIO', '.ISO', '.TAR', '.GZ', '.RZ', '.7Z',
              '.DMG', '.RAR', '.XAR', '.ZIP']

AUDIO_FORMAT = ['.AAC', '.AA', '.AAC', '.DVF', '.M4A', '.M4B', '.M4P', '.MP3',
                '.MSV', 'OGG', 'OGA', '.RAW', '.VOX', '.WAV', '.WMA']

TXT_FORMAT = ['.TXT', '.IN', '.OUT']


class OrganizeJunk:

    def OJunk(self):
        for mdir in dir:
            if os.path.isdir(mdir):
                pass
            else:
                os.mkdir(mdir)

        curr_dir = os.getcwd()

        for file in os.listdir():

            if file.endswith('.py') or file.endswith('.PY'):
                os.rename(curr_dir + '/' + file, curr_dir + '/PY Files/' + file)

            for iformat in IMG_FORMAT:
                if file.endswith(iformat) or file.endswith(iformat.lower()):
                    os.rename(curr_dir + '/' + file, curr_dir + '/IMAGE Files/' + file)

            for vformat in VID_FORMAT:
                if file.endswith(vformat) or file.endswith(vformat.lower()):
                    os.rename(curr_dir + '/' + file, curr_dir + '/VIDEO Files/' + file)

            for dformat in DOC_FORMAT:
                if file.endswith(dformat) or file.endswith(dformat.lower()):
                    os.rename(curr_dir + '/' + file, curr_dir + '/DOC Files/' + file)

            if file.endswith('.html') or file.endswith('.HTML'):
                os.rename(curr_dir + '/' + file, curr_dir + '/HTML Files/' + file)

            for tformat in TXT_FORMAT:
                if file.endswith(tformat) or file.endswith(tformat.lower()):
                    os.rename(curr_dir + '/' + file, curr_dir + '/TXT Files/' + file)

            if file.endswith('.pdf') or file.endswith('.PDF'):
                os.rename(curr_dir + '/' + file, curr_dir + '/PDF Files/' + file)

            for zformat in ZIP_FORMAT:
                if file.endswith(zformat) or file.endswith(zformat.lower()):
                    os.rename(curr_dir + '/' + file, curr_dir + '/COMPRESS Files/' + file)

            for zformat in AUDIO_FORMAT:
                if file.endswith(zformat) or file.endswith(zformat.lower()):
                    os.rename(curr_dir + '/' + file, curr_dir + '/AUDIO Files/' + file)

            if file.endswith('.xml') or file.endswith('.XML'):
                os.rename(curr_dir + '/' + file, curr_dir + '/PDF Files/' + file)

    def rempty(self):
        for rdir in dir:
            try:
                os.rmdir(rdir)
            except:
                pass


def main():
    Oj = OrganizeJunk()
    Oj.OJunk()
    Oj.rempty()

if __name__ == "__main__":
    main()
