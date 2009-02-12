#!/bin/sh

/usr/local/bin/asciidoc -a theme=classy -a toc -a toclevels=3 -a numbered $1
/usr/local/bin/asciidoc -a toc -a toclevels=3 -a numbered -a imagesdir=`pwd`/ -b docbook $1

# Clean up Docbook source
DBFILE=`basename $1 .txt`.xml
TMPFILE=`tempfile -d ./`

sed -e "/<\/*mediaobject>/ d" -e "/<\/*imageobject>/d" -e "/<textobject>/d" -e "s/imagedata/graphic/" $DBFILE > $TMPFILE
mv $TMPFILE $DBFILE
