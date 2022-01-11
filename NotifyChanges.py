import win32file, win32con, os
global path_to_watch
path_to_watch = r'C:\Users\student\Downloads'

#this function opens the file it catches, therefore interrupting its
#downloading process. It doesn't close it, making another problem
#for the client of sending it. Solutions: find a way to close the file / use another library.
def create_handle():
  '''creats a handle for a directory to watch and returns it.'''
  handle = win32file.CreateFile(
    path_to_watch,
    win32con.GENERIC_READ,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
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
      win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
      win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,
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
        return  [full_filename,action]
    except IOError:
      print("could'nt open file, which means it hasn't downloaded yet.")
      pass

def main():
  handle = create_handle()
  while True:
    result = monitor(handle)
    print(result[0],result[1])

main()
