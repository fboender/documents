Documents
=========

This is the source code (and accompanying tools, stylesheets and other matter)
for the document I wrote. You can probably find some of them
[https://www.electricmonk.nl/#writings](here).

Most of these documents are written in Asciidoc. This is then converted into:

* HTML
* DocBook
* PDF
* Epub

The rest of this README describes how to set up things so that you can
generate the above target formats.

### Installation

    # Install required packages (Debian / Ubuntu)
    apt-get install asciidoc docbook-utils
    
    # Install the Asciidoc style
    sudo cp -a style/asciidoc/ /etc/asciidoc/themes/classy

### Generating documents

    cd src/document/
    ../../tools/mk_asciidoc.sh document.txt

