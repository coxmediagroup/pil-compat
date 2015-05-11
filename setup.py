from setuptools import setup

setup(name='pil-compat',
      version='1.0.0',
      packages=['Image',
                'ImageChops',
                'ImageColor',
                'ImageDraw',
                'ImageEnhance',
                'ImageFile',
                'ImageFilter',
                'ImageFont',
                'ImageMath',
                'ImageMorph',
                'ImageOps',
                'ImagePalette',
                'ImagePath',
                'ImageSequence',
                'ImageStat'],
      description='Compatibility modules, bridging PIL -> Pillow',
      author='Alistair Lynn',
      author_email='alistair@alynn.co.uk',
      url='http://github.com/prophile/pil-compat',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Multimedia :: Graphics'
      ],
      setup_requires=['wheel'],
      install_requires=['pillow'])
