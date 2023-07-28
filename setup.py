from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="search_impact_factor",
    version="0.0.11",
    description="A package to query the impact factor database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Brritany/search_impact_factor',
    project_urls={
        'Tracker': 'https://github.com/Brritany/search_impact_factor/issues',
    },
    author="hyz",
    author_email="m946111005@tmu.edu.tw",
    packages=find_packages(),
    keywords=['python', 'impact factor', 'IF'],
    install_requires=[
        "pandas",
    ],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Traditional)",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
