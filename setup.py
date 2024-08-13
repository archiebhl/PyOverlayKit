from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / 'README.md').read_text()

setup(
    name='PyOverlayKit',
    version='0.2.0',
    description='A PyQt package for creating customizable always-on-top overlays, including when applications are full-screen.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/archiebhl/PyOverlayKit',  
    packages=find_packages(),
    install_requires=[
        'PyQt6', 
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
    project_urls={
        'Repository': 'https://github.com/archiebhl/PyOverlayKit',
    },
)
