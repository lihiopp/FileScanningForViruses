import win32file
import win32con, os
global path_to_watch
path_to_watch = r'C:\Users\idd\Downloads'

#this function opens the file it catches, therefore interrupting its
#downloading process. It doesn't close it, making another problem
#for the client of sending it. Solutions: find a way to close the file / use another library.
def create_handle():
  '''creats a handle for a directory to watch and returns it.'''
  handle = win32file.CreateFile(
    path_to_watch,
    win32con.GENERIC_READ,
    win32con.FILE_SHARE_READ,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None)

  return handle

  
def monitor(handle):
  '''monitors and notifies when there was a change in the directory.'''
  while 1:
    results = win32file.ReadDirectoryChangesW (
      handle,
      1024,
      True,
      win32con.FILE_NOTIFY_CHANGE_FILE_NAME,
      None,
      None)

    #Checks if the file has finished downloading.
    #If not, the script continues until it is
    #(and the name of it changes to what it's supposed to be)
    try:
      for action, file in results:
        full_filename = os.path.join (path_to_watch, file)
        f = open(full_filename,'rb')
        f.close()
        print("the file has finished downloading!")
        return  full_filename
    except IOError:
      print("could'nt open file, which means it hasn't downloaded yet.")
      pass

def main():
  handle = create_handle()
  result = monitor(handle)
  return result

main()
