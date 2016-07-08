from distutils.core import setup

import sys
# patch distutils if it can't cope with the "classifiers" keyword
if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

setup(name="CherryTemplate",
      version="1.0.0",
      description="Yet another templating system for Python",
      long_description="""A simple but effective templating system for Python.""",
      classifiers=["Development Status :: Alpha",
                   "Intended Audience :: Developers",
                   "License :: Freely Distributable",
                   "Programming Language :: Python",
                   "Topic :: Internet ",
                   ],
      author="CherryPy Team",
      author_email="team@cherrypy.org",
      url="http://www.cherrypy.org",
      license="BSD",
      packages=["cherrytemplate", "cherrytemplate.unittest"],
      # download_url="TODO"
)

