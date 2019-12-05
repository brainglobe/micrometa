from setuptools import setup, find_packages

requirements = ["configparser", "natsort", "pyyaml"]

setup(
    name="micrometa",
    version="0.0.3",
    description="Reading of microsocopy metadata",
    install_requires=requirements,
    extras_require={"dev": ["black", "pytest-cov", "pytest"]},
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/adamltyson/micrometa",
    author="Adam Tyson",
    author_email="adam.tyson@ucl.ac.uk",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    zip_safe=False,
)
