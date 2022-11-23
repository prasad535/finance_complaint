from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "finance-complaint"
VERSION = "0.0.1"
AUTHOR = "Prasad Nagineni"
DESCRIPTION = "This finance complaint project"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    """
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirements_name.replace("\n","") for requirements_name in requirement_list]
        if(HYPHEN_E_DOT in requirement_list):
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name = PROJECT_NAME, 
    author = AUTHOR, 
    description = DESCRIPTION, 
    packages = find_packages(),
    install_requires = get_requirements_list()
)