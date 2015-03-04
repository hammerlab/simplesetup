# Copyright (c) 2015. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

def parse_readme():
    readme_filename = os.path.join(os.path.dirname(__file__),
                                   'README.md')
    with open(readme_filename, 'r') as f:
        readme = f.read()

    try:
        import pypandoc
        readme = pypandoc.convert(readme, to='rst', format='md')
    except:
        print('Conversion of long_description from MD to '
              'reStructuredText failed...')
        pass

def parse_requirements():
    try:
        from pip.req import parse_requirements
        parsed_reqs = parse_requirements('requirements.txt')
        return [str(req.req) for req in parsed_reqs]
    except ImportError:
        print("Please install pip before proceeding")

import setuptools

DEFAULT_CLASSIFICATION = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Operating System :: OS Independent',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
]

def setup(name, version, description, author, author_email,
                url_prefix='https://github.com/hammerlab/',
                license=('http://www.apache.org/licenses/'
                         'LICENSE-2.0.html'),
                classifiers=DEFAULT_CLASSIFICATION):
    if __name__ == '__main__':
        setuptools.setup(
            name=name,
            version=version,
            description=description,
            author=author,
            author_email=author_email,
            url='%s%s' % (url_prefix, name),
            license=license,
            classifiers=classifiers,
            install_requires=parse_requirements(),
            long_description=parse_readme(),
            packages=[name],
        )
