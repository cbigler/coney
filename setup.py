from setuptools import setup

setup(
    name='jackrabbit',
    version='0.0.1',
    author='Canute Bigler',
    author_email='canute@cbigler.com',
    url='https://github.com/cbigler/jackrabbit',
    description='Lightweight, simple RPC via RabbitMQ',
    packages=['jackrabbit'],
    install_requires=['pika', 'tests'],
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: System :: Distributed Computing",
    ],
)
