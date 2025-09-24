# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
print(here)

setup(
    name="TradingViewData",
    version="1.0.0",  # Required
    packages=find_packages(where="TradingViewData"),  # Required
)