import os
from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

if __name__ == "__main__":
  setup(
        long_description=long_description,
        long_description_content_type='text/markdown')