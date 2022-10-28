from setuptools import setup
import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()
# long_description = (here / "README.md").read_text(encoding="utf-8")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mananij_diffusion2D",
    version="0.0.3",
    author="Jayesh Manani",
    author_email='jsmanani@gmail.com',
    description="This code solves the diffusion equation using the Finite Difference Method.",
    long_description=long_description,
    long_description_content_type="text/markdown",  
    url="https://github.com/Simulation-Software-Engineering/diffusion2d",
    keywords="simulation, setuptools, siffusion, equation",  
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["matplotlib",
                        "numpy"],
    zip_safe = False,
)

# from setuptools import setup

# if __name__ == "__main__":
#   setup()