import setuptools

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="youtubemusicapp",
    version="0.0.1",
    author="Daniel Silva",
    description="A Youtube Music Wrapper",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/danzkigg/youtubemusicapp",
    project_urls={
        "Bug Tracker": "https://github.com/danzkigg/youtubemusicapp/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "app"},
    packages=setuptools.find_packages(where="app"),
    python_requires=">=3.9",
)