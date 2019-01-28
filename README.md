Documents
=========

This is the source code (and accompanying tools, stylesheets and other matter)
for the document I wrote. You can probably find some of them
[here](https://www.electricmonk.nl/#writings).

Most of these documents are written in Asciidoc or Pandoc. This is then
converted into:

* HTML
* DocBook
* PDF
* Epub

The rest of this README describes how to set up things so that you can
generate the above target formats.

### Installation

If you want to convert the sources to various formats, you must install some
software first.

Install required packages (Debian / Ubuntu)

    apt-get install asciidoc docbook-utils pandoc
    
Install the Asciidoc style

    sudo cp -a style/asciidoc/ /etc/asciidoc/themes/classy

Install the `pp` text preprocessor from
[github](https://github.com/CDSoft/pp).
    
Install the [simple little automator](https://github.com/fboender/sla).
    
### Generating documents

For AsciiDoc

    cd src/document/
    ../../tools/mk_asciidoc.sh document.txt

For Pandoc

    sla src/finite_state_machines_in_practice/
