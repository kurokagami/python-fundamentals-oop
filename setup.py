from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name="simple_banking_system_oop",
    version='0.1.0',
    author='KuroKagami',
    author_email="jeangabriel0990@gmail.com",
    description='Simple Banking System OOP',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url="https://github.com/kurokagami/python-fundamentals-oop",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.12',
)