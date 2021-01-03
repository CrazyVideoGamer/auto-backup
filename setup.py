import setuptools
from pathlib import Path

long_description = Path("README.md").read_text()

setuptools.setup(
  name="auto-backup",
  version="0.1.0-alpha.1",
  author="CrazyVideoGamez",
  author_email="crazyvideogamez.help@gmail.com",
  description="A tool to easily backup your files and folders",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/CrazyVideoGamez/auto-backup',
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
  ],
  python_requires='>=3.8',
)