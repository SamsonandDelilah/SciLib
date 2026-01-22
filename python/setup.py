from setuptools import setup, find_packages

setup(
    name="scilib",
    version="0.1.0",
    packages=find_packages(),  # Findet python/ automatisch
    install_requires=["numpy"],
    extras_require={
        "precision": ["gmpy2>=2.1.0"],
        "dev": ["pytest", "black"]
    },
)
