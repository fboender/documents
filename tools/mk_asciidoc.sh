#!/bin/sh

asciidoc -a theme=classy -a toc -a toclevels=3 -a numbered $1
asciidoc -a toc -a toclevels=3 -a numbered -a imagesdir=`pwd`/ -b docbook $1

# Clean up Docbook source
DBFILE=`basename $1 .txt`.xml
db2pdf $DBFILE > /dev/null
#TMPFILE=`tempfile -d ./`
#
#sed -e "/<\/*mediaobject>/ d" -e "/<\/*imageobject>/d" -e "/<textobject>/d" -e "s/imagedata/graphic/" $DBFILE > $TMPFILE
#mv $TMPFILE $DBFILE

a2x -f epub --stylesheet=/etc/asciidoc/stylesheets/classy.css $1
#a2x -f pdf --stylesheet=/etc/asciidoc/stylesheets/classy.css $1
