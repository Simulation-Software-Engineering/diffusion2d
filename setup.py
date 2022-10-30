from setuptools import setup
import setuptools

setup(
    name="bhawsina_diffusion2D",
    version="0.0.2",
    author="Nistha Bhawsinka",
    description="diffusion equation solver in 2D",
    url="https://github.com/Simulation-Software-Engineering/diffusion2d",
    package_dir={"": "bhawsina_diffusion2D"},
    packages=setuptools.find_packages(where="bhawsina_diffusion2D"),
    python_requires=">=3.6",
    install_requires=["numpy","matplotlib"]
)