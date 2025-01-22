# qxmt-tutorials
This repository provides a collection of tutorials designed to help you become proficient with [QXMT](https://github.com/Qyusu/qxmt) and integrate this tool into your research or experimental workflows. Each tutorial is available in `.ipynb` notebook format, allowing you to start right away after cloning this repository. If you want a hands-on learning experience beyond just reading the documentation, these tutorials are ideal for you!

## Environment Setup
QXMT requires Python >=3.10, and we recommend using Poetry for environment setup. If these are not already installed on your system, refer to the following commands. This repository has minimal external library dependencies, so you are welcome to set up your environment using any preferred method by consulting `pyproject.toml`.

``` bash
# Set up the Python environment with pyenv
pyenv install 3.11
pyenv local 3.11

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install the required libraries and set up the virtual environment
poetry install --no-root
```

## Running the Tutorials
The tutorial notebooks are located in the `notebooks` folder. The necessary folder structure and other setup requirements for using QXMT are configured automatically when cloning the repository, so no additional steps are needed. 
There are two main ways to run the notebooks. Feel free to choose the option that best suits your workflow.

### Option 1: Using Jupyter Lab
`JupyterLab` is installed as part of `poetry install`, so you can start it as follows. After launching, select the `.ipynb` files in the `notebooks` folder to access each tutorial.

```bash
# Enter the virtual environment created by Poetry
poetry shell

# Start Jupyter Lab
# Work in your web browser after startup
jupyter lab
```

### Option 2: Using Notebooks within an IDE
If you are using an IDE like VSCode, you can open `.ipynb` files directly in the IDE for interactive execution and visualization. Select the `.ipynb` files in the `notebooks` folder, and choose the Poetry-created environment as the kernel (e.g., `.venv/bin/python`) to run the notebooks.


## Contributing
In addition to the official tutorials, this repository aims to cover a wide range of use cases.If you've conducted experiments with QXMT, feel free to submit a pull request to share your work. While there are no strict guidelines on notebook format or content at this time, following the structure of existing tutorials is recommended. 
We look forward to your contributions!
