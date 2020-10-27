import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='py-cheats',
    version='1.0',
    author="Christian L.",
    author_email="christianlaforest45@gmail.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Shadow2ube",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',

)