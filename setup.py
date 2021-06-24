import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bin-http-util",
    version="0.0.1",
    author="Madhava-mng",
    author_email="alformint@gmail.com",
    description="binary files for testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Madhava-mng/bin-http-util",
    scripts = [
        "scripts/http-post",
        ],
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["requests"]
)
