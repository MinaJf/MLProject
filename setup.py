from setuptools import find_packages, setup
from typing import List

def get_req(f_path:str)->List[str]:
    requirements = []
    with open(f_path) as f_obj:
        requirements=f_obj.readline()
        requirements=[req.replace("\n", " ") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements 



setup(
name = 'Ml_p',
author = 'Mina',
version = '0.001',
packages=find_packages(),
install_requires=get_req('requirements.txt')



)