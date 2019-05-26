# alto-tools

**Warning: not fully implemented - work in progress**

> [Python](https://www.python.org/) script for performing various operations on [ALTO](http://www.loc.gov/standards/alto/) files.

[![image](https://travis-ci.org/cneud/alto-tools.svg?branch=master)](https://travis-ci.org/cneud/alto-tools)

Planned operations:

* extract **OCR confidence** of the ALTO document(s)  
  ``python alto_tools.py {INPUT} --confidence``
* extract **text** content of the ALTO document(s)  
  ``python alto_tools.py {INPUT} --text``
* extract **graphical elements** of the ALTO document(s)  
  ``python alto_tools.py {INPUT} --graphic``
* extract **metadata** of the ALTO document(s)  
  ``python alto_tools.py {INPUT} --metadata``
* xsl **transform** ALTO document(s) to target format(s)  
  ``python alto_tools.py {INPUT} --transform {XSL_STYLESHEET}``
* xpath **query** content of the ALTO document(s)  
  ``python alto_tools.py {INPUT} --query {XPATH_EXPRESSION}``
* xsd **validate** the ALTO document(s)  
  ``python alto_tools.py {INPUT} --validate``

Requirements:

* [lxml](http://lxml.de/)
