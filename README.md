# Useful-Commands
For personal note-taking of useful commands

## Git
### Standard
- **New branch:** `git checkout -b [name_of_your_new_branch]`
- **List branches:** `git branch`
- **Stage files:** `git add <filename>`
- **See changes:** `git diff <branchname>`
- **Create PR:** `git push` 
- **Delete branch:** `git branch -d <branchname>`
- **Commit Modified File:** `git commit -am "commit message"`
- **See modified files:** `git status`


### Merge Conflicts
- **Catch up with master on a feature branch:** `git merge master`
- **Get rid of modification on file:** `git reset <filename>`
- **Undo 1 commit:** `git reset HEAD~1`
- **See commit log & hashes:** `git log`
- **Unstage but keep all changes after this hash:** `git reset <commithash>`
  - `--hard` to unstage + discard changes also

## Python Module
- **Sibling directory:** 1) Single Method
  ```python
  import os, sys
  currentdir = os.path.dirname(os.path.realpath(__file__))
  parentdir = os.path.dirname(currentdir)
  sys.path.append(parentdir) 
  ```

  2) Modularization: Create `__init__.py` in the `sibling_directory` with the following
  ```python
  from sibling_script import sibling_method
  ```
  In the `main.py` do:
  ```python
  from sibling_directory import sibling_method
  ```

## Python mapping
- **Dictionary:** Doesn't exist. Use comprehension
  ```python
  my_dictionary = {k: f(v) for k, v in my_dictionary.items()}
  ```

## Python Typing
- **Set the same type as class in method's parameter:** 
  ```python
  class Foo:
    def foo_method(self, other_foo: "Foo"):
        return "Hello World!"
  ```
  Using [forward declarations](https://peps.python.org/pep-0484/#forward-references) it is `eval`ed after the whole module is loaded, so it can evaluate to the `Foo` class.

## Using `requirements.txt` with pip

- **Create `requirements.txt`:** `pip freeze > requirements.txt` 
- **Install all dependencies:** `pip install -r requirements.txt`

## Python Environment
- **Use Environment:** 
  - Linux: `source env/bin/activate`
  - Windows: `.\env\Scripts\activate.bat`
