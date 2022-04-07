from setuptools import setup, find_packages


setup(
    name='m3_project',
    version='1.0',
    description='m3_project, version 1.0',
    author='Yaroslav M.',
    author_email='mestkovskyyaroslavd@mail.ru',
    url='https://github.com/YaroslavMestkovsky',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    package_dir={'': 'project'},
    packages=find_packages('project'),
    include_package_data=True,
)
