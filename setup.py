from setuptools import setup, find_packages


setup(
    name='stackstats',
    version='0.1.0',
    packages=find_packages(),
    install_requires=(
        'Click',
        'Jinja2',
        'python-dateutil',
        'requests',
        'tabulate'
    ),
    package_data={
        'stats': ['templates/*.j2'],
    },
    entry_points='''
        [console_scripts]
        stats=stats.main:main
    '''
)
