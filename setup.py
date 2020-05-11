# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['anysay']

package_data = \
{'': ['*'], 'anysay': ['default_pics/*']}

install_requires = \
['colored>=1.4.2,<2.0.0',
 'pillow>=7.0,<8.0',
 'python-magic>=0.4.15,<0.5.0',
 'sty>=1.0.0-beta.12,<2.0.0',
 'tqdm>=4.46.0,<5.0.0']

entry_points = \
{'console_scripts': ['anysay = anysay:main']}

setup_kwargs = {
    'name': 'anysay',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'n0nvme',
    'author_email': 'svmpl3nvm3@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

# This setup.py was autogenerated using poetry.
