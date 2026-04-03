from setuptools import setup
import setup_translate

pkg = 'Extensions.BitrateViewer'
setup(name='enigma2-plugin-extensions-bitrateviewer',
       version='3.0',
       description='BitrateViewer',
       package_dir={pkg: 'bitrateviewer'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
