from setuptools import setup, find_packages

setup(
    name="onurodh",
    version="1.0.0",
    description="A Python CLI for sending requests from JSON or YAML configuration files.",
    author="Maruf",
    author_email="hossain.maruf186@gmail.com",
    license="MIT",
    url="https://github.com/MarufHossain14/onurodh",
    packages=find_packages(),
    install_requires=[
        "requests>=2.0.0,<3.0.0",
        "PyYAML>=6.0.0,<7.0.0",
        "lxml>=4.0.0,<5.0.0",
        "Pygments>=2.0.0,<3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "onurodh=onurodh.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
