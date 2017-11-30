#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='overwatch-mongo-agent',
    version='0.0.1',
    url='https://github.com/leadhub-code/overwatch-mongo-agent',
    author='Petr Messner',
    author_email='petr.messner@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='overwatch agent mongodb mongo',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'pymongo',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'overwatch-mongo-agent=overwatch_mongo_agent:mongo_agent_main',
        ],
    },
)
