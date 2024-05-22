# Boolean Expressions Practice

A few boolean expression puzzles to solve. The given code in [solutions.py](./solutions.py) contains several incomplete functions that you must complete to achieve the desired behavior. That is all you must do.

To run the program, run the file named [main.py](./main.py).

## Clone this repository

First, clone this repository to your local computer, using Visual Studio Code's cloning feature.

Helpful video:

- [cloning a code repository from GitHub to your local machine](https://www.youtube.com/watch?v=axcny0o1NYo).

## Set up Visual Studio Code

Once cloned, set Visual Studio Code to be suitable for Python development using the "command palette":

- set the interpreter to a Python 3.x interpreter, such as that by [`Anaconda`](https://www.anaconda.com/).
- set the linter to by `pylint`.
- set the test framework to be `pytest`.

Helpful video:

- [Setting up Visual Studio Code for Python development](https://www.youtube.com/watch?v=xsXMzyK1M4I)

## Modify the code

The file named `solutions.py` contains several functions that must be completed in order for the program to work. Each function contains a description of what it should do.

The only modifications you must make in order to complete this assignment are to these functions definitions in this one file. Do not modify any code outside of these function definitions.

### Run the program

To run the program, run the file named `main.py`. The code in this file makes use those functions you have modified in `solutions.py` to produce the intended behavior and output of the program.

### Verify the output is correct

Running the `main.py` program makes use of the functions defined in `solutions.py`. Each function asks the user to enter certain input, and the `main` function prints out some meaningful message in response to the user's input.

### Verify that the tests pass

Pytest-based tests are included in the `tests` directory that will help you determine whether each function is operating as expected. You should not edit any files in the `test` directory. Run these tests from the `Tests` panel within Visual Studio Code. Running the test files directly does nothing.

If your code has been completed correctly, all tests should pass. Failed tests indicate problems in your code. Failed tests will usually show an "`AssertionError`" message that may be helpful identifying where the error is in your code.

If the tests do not appear in the `Tests` panel at all, or seem to never stop loading, or you experience other problems with them that prevent you from running them, open up a Terminal window and run the command, `pytest --collect-only`, to see whether there are any errors in your code that prevent the tests from being discovered. If there are no errors reported from that command, try running the tests directly from the Terminal with the command, `pytest`.

In addition to syntax errors in your code, a common error that prevents the tests from running at all is indentation errors, where your code is incorrectly placed outside of (i.e. not indented within) any function. These usually result in a "`reading from stdin while output is captured!`" error when trying to run the tests from Terminal using the `pytest` command.

## Submit your work

Each student must submit this assignment individually. Use Visual Studio Code to perform git `stage`, `commit` and `push` actions to submit. These actions are all available as menu items in Visual Studio Code's Source Control panel.

1. Type a short note about what you have done to the files in the `Message` area, and then type `Command-Enter` (Mac) or `Control-Enter` (Windows) to perform git `stage` and `commit` actions.
1. Click the `...` icon next to the words, "Source Control" and select "Push" to perform the git `push` action. This will upload your work to your repository on GitHub.com.

![Pushing work in Visual Studio Code](./images/vscode_stage_commit_push.png)
