from setuptools import setup, find_packages

setup(
    name="nobsdownloader",
    version="0.1",
    py_modules=["nobsdownloader"],
    entry_points={
        'console_scripts': [
            'nobsdownloader=nobsdownloader:main',
        ],
    },
)

