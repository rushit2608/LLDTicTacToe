from setuptools import setup, find_packages

setup(
    name='LLDTicTacToe',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here, e.g.:
        # 'numpy',
    ],
    author='Rushikesh Tonde',
    author_email='rushisa123@gmail.com',
    description='A Low level Design with code of Tictactoe',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rushit2608/LLDTickTacToe',
)
