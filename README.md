# Useful-Commands
For personal note-taking of useful commands

## Git
- **New branch:** `git checkout -b [name_of_your_new_branch]`
- 

## Python Module
- **Sibling directory:** 1) Single Method
  ```python
  import sys
  sys.path.append("..")
  from sibling_directory.sibling_script import sibling_method
  ```

  2) Modularization: Create `__init__.py` in the `sibling_directory` with the following
  ```python
  from sibling_script import sibling_method
  ```
  In the `main.py` do:
  ```python
  from sibling_directory import sibling_method
  ```

## Python Environment
- **Use Environment:** `source env/bin/activate`
