from setuptools import setup, find_packages

setup(
    name="a2a-demo",
    version="0.1.0",
    description="Modular multi-agent AI travel planner using Google ADK",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        # Requirements are read from requirements.txt
    ],
    include_package_data=True,
    python_requires='>=3.11',
)
