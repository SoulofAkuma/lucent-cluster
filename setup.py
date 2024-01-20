import lucent
from setuptools import setup, find_packages

version = lucent.__version__

setup(
    name="torch-lucent",
    packages=find_packages(exclude=[]),
    version=version,
    description=(
        "Lucid for PyTorch. "
        "Collection of infrastructure and tools for research in "
        "neural network interpretability."
    ),
    license="Apache License 2.0",
    install_requires=[
        "torch>=1.5.0",
        "torchvision",
        "kornia<=0.4.1",
        "tqdm",
        "numpy",
        "ipython",
        "pillow",
        "future",
        "decorator",
        "pytest",
        "pytest-mock",
        "coverage",
        "coveralls",
        "scikit-learn"
    ],
)
