# it is resposnible for creating my machine learning application as a package
# which can be installed and used by me or any one


from setuptools import find_packages, setup
from typing import List
'''
so this will automatically find out all the packages 
that are available in the entire ML application directory that we created
 '''

HYPEN_E_DOT = '- e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]  #there will be \n value when we use readline so inorder to remove that we replace \n with ""
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name ="mlproject",
    version ="0.0.1",
    author = 'Soorya',
    author_email = 'sooryasdk@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')
)