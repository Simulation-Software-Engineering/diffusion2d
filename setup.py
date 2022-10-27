from setuptools import setup
# import os

# Extract install_requires from requirements.txt
#lib_folder = os.path.dirname(os.path.realpath(__file__))
#requirement_path = lib_folder + '/requirements.txt'
#readme_path = lib_folder + '/README.md'
#
#if os.path.isfile(requirement_path):
#    with open(requirement_path) as f:
#        install_requires = f.read().splitlines()
#
#if os.path.isfile(readme_path):
#   with open(readme_path) as f:
#        long_description = f.read()


setup(
    name="diffusion2d",
    version="0.0.1",
    author="Felix Neubauer",
    description="A small description",
    url="https://github.com/Logende/diffusion2d",
    python_requires=">=3.6",
    install_requires=["numpy", "matplotlib"]
)