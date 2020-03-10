from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#Login to Google Drive and create drive object

def google_file_upload():
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    import glob, os
    os.chdir("path_to_download")
    for file in glob.glob("*.pcap"):
        print file
        with open(file,"r") as f:
            fn = os.path.basename(f.name)
            file_drive = drive.CreateFile({'title': fn })  
            file_drive.content = f
            file_drive.Upload()
            print "The file: " + fn + " has been uploaded"
    
    print "All files have been uploaded"



