from setuptools import find_packages, setup

setup(
    name="grok",
    packages=find_packages(),
    version="0.0.1",
    install_requires=[
        "pytorch_lightning==1.2.9",
        "wandb",
        "sympy",
        "blobfile",
        "numpy",
        "torch",
        "tqdm",
        "scipy",
        "mod",
        "matplotlib",
    ],
)
