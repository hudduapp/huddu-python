from setuptools import setup

readme_file = open("Readme.md", "r")
readme_content = readme_file.read()

setup(
    name="huddu",

    version="1.0",

    packages=["huddu"],

    url="https://github.com/hudduapp/huddu-python",

    requires=["json", "requests"],

    license="MIT",

    author="Joshua3212",

    author_email="",

    description="",

    long_description_content_type="text/markdown",

    long_description=readme_content,
)
