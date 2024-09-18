import os
import sys
import subprocess

# Step 1: Check if venv is installed, if not install it
def install_venv():
    """
    Ensures that the `venv` module is available for creating virtual environments.

    This function attempts to import the `venv` module. If the import fails (i.e., the module is not installed),
    it uses `pip` to install the `venv` module.

    Raises:
        subprocess.CalledProcessError: If the `pip install venv` command fails.
    """
    try:
        import venv
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "venv"])

# Step 2: Create virtual environment
def create_virtualenv():
    """
    Creates a virtual environment in the current directory if it does not already exist.

    This function checks if a directory named 'venv' exists in the current working directory.
    If the directory does not exist, it creates a new virtual environment using the Python
    `venv` module. If the directory already exists, it prints a message indicating that the
    virtual environment already exists.

    Raises:
        subprocess.CalledProcessError: If the virtual environment creation process fails.
    """
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
    else:
        print("Virtual environment already exists.")

# Step 3: Install requirements
def install_requirements():
    """
    Installs the required packages listed in the 'requirements.txt' file.

    This function determines the appropriate Python executable based on the 
    operating system and uses it to install the dependencies specified in 
    'requirements.txt' using pip.

    - For Windows systems, it uses 'venv\\Scripts\\python.exe'.
    - For other systems, it uses 'venv/bin/python'.

    Raises:
        subprocess.CalledProcessError: If the pip installation command fails.
    """
    print("Installing requirements...")
    if os.name == 'nt':  # For Windows systems
        python_exec = os.path.join('venv', 'Scripts', 'python.exe')
    else:
        python_exec = os.path.join('venv', 'bin', 'python')

    subprocess.check_call([python_exec, "-m", "pip", "install", "-r", "requirements.txt"])

# Automating the setup process
if __name__ == "__main__":
    install_venv()
    create_virtualenv()
    install_requirements()

    print("\n\t- To activate the virtual environment, run: \n\nsource venv/bin/activate\n")

    print("\n\t- To deactivate the virtual environment, run: \n\ndeactivate\n")