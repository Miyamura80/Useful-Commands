# Useful-Commands
For personal note-taking of useful commands

## Git
- **New branch:** `git checkout -b [name_of_your_new_branch]`

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

## Python Typing
- **Set the same type as class in method's parameter:** 
  ```
  class Foo:
    def foo_method(self, other_foo: "Foo"):
        return "Hello World!"
  ```
  Using [forward declarations](https://peps.python.org/pep-0484/#forward-references) it is `eval`ed after the whole module is loaded, so it can evaluate to the `Foo` class.

## Using `requirements.txt` with pip

- **Create `requirements.txt`:** `pip freeze > requirements.txt` 
- **Install all dependencies:** `pip install -r requirements.txt`

## Python Environment
- **Use Environment:** `source env/bin/activate`
