import os
from setuptools import find_namespace_packages, setup

PROJECT_DIR = os.path.dirname(__file__)

INFO = open(os.path.join(PROJECT_DIR, 'INFO')).readlines()
INFO = dict((line.strip().split('=') for line in INFO))

DEPENDENCIES = open(os.path.join(PROJECT_DIR, 'requirements.txt')).readlines()

setup(name='mlops-pipeline-azure',
      version=INFO['version'],
      author=INFO['author'],
      author_email=INFO['author_email'],
      url=INFO['url'],
      license=open(os.path.join(PROJECT_DIR, 'LICENSE')).read(),
      packages=find_namespace_packages(include=['src.*']),
      namespace_packages=['src', 'src.pipeline'],
      install_requires=[d for d in DEPENDENCIES if '://' not in d],
      python_requires='>=3.8',
      zip_safe=False,
      include_package_data=True,
      entry_points={"console_scripts": [
          "train=src.pipeline.train:main",
          "deploy=src.pipeline.deploy:main",
          "create-workspace=src.pipeline.create_workspace:main"
        ]},
)
