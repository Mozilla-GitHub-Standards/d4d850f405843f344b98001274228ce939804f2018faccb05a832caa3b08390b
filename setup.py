# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup

install_requires = [
    'minion-backend'
]

setup(name="minion-nmap-plugin",
      version="0.2",
      description="NMAP Plugin for Minion",
      url="https://github.com/mozilla/minion-nmap-plugin/",
      author="Mozilla",
      author_email="minion@mozilla.com",
      packages=['minion', 'minion.plugins'],
      namespace_packages=['minion', 'minion.plugins'],
      include_package_data=True,
      install_requires = install_requires)
