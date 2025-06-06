# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text analysis.',
      author='Sheikh Md. Sazidul Islam',
      packages=['text_analyzer'],
      install_requires=['matplotlib>=3.0.0'])
