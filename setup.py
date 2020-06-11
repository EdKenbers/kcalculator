from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='kcalculator',
    version='0.1.2',
    author='Ed. Kenbers',
    author_email='git@kenbers.com',
    description='A simple calculator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/EdKenbers/kcalculator',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'kcalculator=kcalculator:main'
    ]
    },
)