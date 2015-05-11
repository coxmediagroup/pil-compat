from setuptools import setup

setup(name='pil-compat',
      version='1.0.0',
      packages=['Image',
                'ImageDraw'],
      description='Compatibility modules, bridging PIL -> Pillow',
      author='Alistair Lynn',
      author_email='alistair@alynn.co.uk',
      url='http://github.com/prophile/pil-compat',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: Other/Proprietary License',
          'Programming Language :: Python',
          'Topic :: Multimedia :: Graphics'
      ],
      setup_requires=['wheel'],
      install_requires=['pillow'])
