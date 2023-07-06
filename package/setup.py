from setuptools import setup, find_packages

setup(
    name='framepackage',
    version='1.0.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='A simple package for drawing frames around text',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/frame',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='framepackage drawing text',
)