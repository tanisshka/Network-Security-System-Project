from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    requirements_lst:List[str]=[]
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file is not found")
        
    return requirements_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Tanishka Patil",
    author_email="tanishkapatil0102@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)