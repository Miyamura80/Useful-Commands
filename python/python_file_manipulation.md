# Python File Manipulation 

## Basics

- Path of file, file dir, file parent dir, file grandparent dir:
  ```python
  from os.path import dirname, realpath
  filepath = realpath(__file__)

  dir_of_file = dirname(filepath)
  parent_dir_of_file = dirname(dir_of_file)
  parents_parent_dir_of_file = dirname(parent_dir_of_file)
  ```
- Current working directory: 
  ```python
  import os 
  cwd = os.getcwd()
  ```
- `os.join`:
  Takes `n` arguments, concatenates paths by "/" messily. Output string starts from first leading "/" string
  <details>
    <summary> Examples: </summary>
      
      import os
      # 1
      path = "/home"
      print(os.path.join(path, "User/Desktop", "file.txt"))
      # >>> /home/User/Desktop/file.txt
  
      # 2
      path = "User/Documents"
      print(os.path.join(path, "/home", "file.txt"))
      # >>> /home/file.txt
      # NOTE: Overriden by "/" symbol
  
      # 3
      path = "/User"
      print(os.path.join(path, "Downloads", "file.txt", "/home"))
      # >>> /home
      # NOTE: Again, overriden by "/" symbol
  
      # 4
      path = "/home"
      print(os.path.join(path, "User/Public/", "Documents", ""))
      # >>> /home/User/Public/Documents
        
  </details>
- Glob module:
  ```python
  import glob
  # All files and directories ending with .txt and that don't begin with a dot:
  print(glob.glob("/home/adam/*.txt")) 
  # All files and directories ending with .txt with depth of 2 folders, ignoring names beginning with a dot:
  print(glob.glob("/home/adam/*/*.txt")) 
  
  >>> ['/home/adam/file1.txt', '/home/adam/file2.txt', .... ]
  ```
