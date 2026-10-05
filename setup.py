from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e .'
def get_requirements(filepath:str)->list[str]:
    '''
    this fuction will return requirements
    '''
    requirements = []
    with open(filepath) as obj:
        requirements = obj.readlines()
        requirements =  [req.replace("\n","")  for req in requirements] 

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements



setup(
name="MLproject",
version="0.0.1",
author="Dhruv Baberwal",
author_email="dhruvbaberwal13@gmail.com",
packages= find_packages(),
install_requires=get_requirements('requirements.txt')
)