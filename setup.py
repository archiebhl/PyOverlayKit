from setuptools import setup, find_packages

setup(
    name='PyOverlayKit',
    version='0.1.0',
    description='A PyQt package for creating customizable always-on-top overlays',
    url='https://github.com/yourusername/my_overlay_package',  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        'PyQt6',  # Specify the PyQt version you’re using
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Adjust the Python version requirement as needed
)
