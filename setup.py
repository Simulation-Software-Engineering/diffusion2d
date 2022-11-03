from setuptools import setup
import setuptools

setup(
    name="tarpansa-diffusion2d",
    version="0.0.1",
    author="<Sena Tarpan>",
    description="",
    url="https://github.com/senatirpan/diffusion2d",
    package_dir={"": "/Users/SenaTirpan/Desktop/repos/diffusion2d-main/"},
    packages=setuptools.find_packages(where="/Users/SenaTirpan/Desktop/repos/diffusion2d-main/"),
    python_requires=">=3.6",
    install_requires=["numpy==1.19.5","matplotlib==3.3.4"],
)