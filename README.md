# Tool-for-Grabing-Lessons-in-UM-SJTU
This is a tool for grab lessons in Joint Institute UM-SJTU based mainly on *Selenium* in Python. The tool can automatically test whether the course is available in a high frequency and tick the course when available.

## Suggested Environment and Installation
OS: MacOS
 
Otherwise you should change 
```python 
browser = webdriver.Safari()
``` 
into other browsers like 
```python 
browser = webdriver.Chrome()
``` 
Python Version: Anaconda/Miniconda 

Use `conda create -n your_env_name python=X.X` to create a virtual environment for grabing lessons. `your_env_name` should be replaced by the name you want.

Use `conda activate your_env_name` to activate and enter the environment for this tool

Use `conda install selenium` to install selenium in this environment

Use `conda install -c conda-forge tesserocr` to install tesserocr in this environment

## How to Edit the Script to Choose the Course You Want?
Enable the Web Inspector of your browser

