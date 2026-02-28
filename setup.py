import os
from distutils.core import setup
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pet-pet-gif-fix',
    version='1.0.3',
    packages=['petpetgif_fix'],
    keywords=['petpet', 'petthe', 'gif', "fix", "petpetgif-fix", "petpetgif_fix", "patch"],
    url='https://github.com/TheMrRedSlime/pet-pet-gif',
    license='MIT',
    author='TheMrRedSlime',
    author_email='cam.anderson573@gmail.com',
    description='Generate a petting gif from a static image (known as "petpet", "Pet the X", or "PETTHE").',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["pillow", "setuptools"],
    package_data={"petpetgif_fix": ["img/*"]}
)
