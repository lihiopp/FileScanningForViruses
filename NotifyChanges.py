import win32file, win32con, os
global path_to_watch
path_to_watch = r'C:\Users\idd\Downloads'

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

    for action, file in results:
      full_filename = os.path.join (path_to_watch, file)
      suffix = full_filename.split('.')[-1]
      if(suffix!="tmp" and suffix!="crdownload"):
        return full_filename


def main(return_value):
  handle = create_handle()
  while True:
    result = monitor(handle)
    return_value.append(result)
