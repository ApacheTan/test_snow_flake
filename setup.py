from setuptools import setup

setup(
    name="snowflake",
    version="0.1",
    description="draw 10 snow flowers on screen with defined color",
    packages=["snow_flaker"],
    python_requires=">3",
    install_requires=["numpy>=1.19"]
)