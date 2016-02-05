from setuptools import setup

setup(
    name='jackrabbit',
    version='0.0.1',
    author='Canute Bigler',
    author_email='canute@cbigler.com',
    url='https://github.com/cbigler/jackrabbit',
    description='Lightweight, simple RPC via RabbitMQ',
    packages=['jackrabbit'],
    install_requires=['pika'],
)
