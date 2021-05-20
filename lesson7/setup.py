from setuptools import setup, find_packages


setup(
    name="clean_folder",
    version="1.0",
    description='Clean folder script',
    url='https://github.com/Bohdan-developer/goit-python/tree/main/lesson7/clean_folder/clean_folder',
    author='Bohdan Kostenko',
    author_email='bohdan.kostenko2020@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
)