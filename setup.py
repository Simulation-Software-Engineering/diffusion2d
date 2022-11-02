from setuptools import setup
import setuptools

setup(
    name="MarkAshraf96_diff_2d",
    version="0.0.2",
    author="Mark Youssef",
    description="This code solves the diffusion equation using the Finite Difference Method.",
    url="https://github.com/Simulation-Software-Engineering/diffusion2d",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["numpy"]
)