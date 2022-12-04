from setuptools import setup,find_packages

setup(
    name="snowflake",
    version="0.1",
    author="dsss_ex5",
    author_email="dsss_ex5@virtual.com",
    description="draw 10 snow flowers on screen with defined color",
    packages=find_packages(),
    python_requires=">3",
    install_requires=["numpy","turtles"]
)