from setuptools import find_packages, setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = []

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']

setup(
    author="Sulyak M S",
    author_email='michael@sulyak.info',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='pycomponents',
    name='pycomponents',
    packages=find_packages(include=['pycomponents']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/expert-m/pycomponents',
    version='0.1.0',
    zip_safe=False,
)
