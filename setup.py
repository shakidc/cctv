from setuptools import setup

setup(
    name='mcam',
    entry_points={
        "console_scripts": [
            'mcam=lib:app'
        ]
    },
)
