#!/Users/gabriele/Library/CloudStorage/GoogleDrive-cavallaro.gabriele@gmail.com/My Drive/Archive/Gabriele/2024/University_of_Iceland/Course_ML4EO_powered_by_Supercomputers/ML4EOwithHPC/venv/bin/python3

# $Id: rst2pseudoxml.py 4564 2006-05-21 20:44:42Z wiemann $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing pseudo-XML.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates pseudo-XML from standalone reStructuredText '
               'sources (for testing purposes).  ' + default_description)

publish_cmdline(description=description)
