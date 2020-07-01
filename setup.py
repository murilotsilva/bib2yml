import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="bib2yml-murilotsilva",
    version="0.1",
    author="Murilo Silva",
    author_email="murilotxs@gmail.com",
    description="A package to convert .bib files to YAML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/murilotsilva/bib2yml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    python_requires=">=3.6",
)
