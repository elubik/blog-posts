from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='httpie',
    version='1.0',
    description='Altair diagrams inside IPython Jupyter osurced with Pandas',
    long_description=long_description,
    url='https://github.com/elubik/blog-posts',
    download_url='https://github.com/elubik/blog-posts',
    author='Emil Lubikowski',
    author_email='e.lubikowski@gmail.com',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
)
