from setuptools import setup

setup(
    name="smart_lambda",
    version="1.0.0",
    description="",

    license='MIT',

    python_requires=">=3.8",

    packages=
    [
        'smart_lambda',
    ],

    package_dir=
    {
        'smart_lambda': 'smart_lambda',
    },

    author="Thomas Linner",
    author_email="linner.thomas@gmx.net",

    classifiers=
    [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
