"""lambdata, a collection of data science functions"""

import setuptools

REQUIRED = [
    'numpy',
    'pandas'
]

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name = 'lambdata-dscohen75',
    version='0.0.3',
    author='dscohen75',
    description="Collection of data science functions",
    long_description = LONG_DESCRIPTION,
    long_description_content_type = 'text/markdown',
    url = "https://github.com/dscohen75/lambdata",
    packages = setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIRED,
    classifiers=["Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

