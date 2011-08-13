#!/bin/sh

asciidoc -a theme=classy -a toc -a toclevels=3 -a numbered $1
asciidoc -a toc -a toclevels=3 -a numbered -a imagesdir=`pwd`/ -b docbook $1
DBFILE=`basename $1 .txt`.xml
sed -i -e "/<\/*mediaobject>/ d" -e "/<\/*imageobject>/d" -e "/<textobject>/d" -e "s/imagedata/graphic/" $DBFILE
db2pdf $DBFILE > /dev/null
a2x -f epub --stylesheet=/etc/asciidoc/stylesheets/classy.css $1
