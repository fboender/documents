#!/bin/sh

DOC=weighted_random_dist.txt
asciidoc -a theme=classy -a toc -a toclevels=3 -a numbered "$DOC"
asciidoc -a toc -a toclevels=3 -a numbered -a imagesdir=`pwd`/ -b docbook "$DOC"
DBFILE=`basename "$DOC" .txt`.xml
#sed -i -e "/<\/*mediaobject>/ d" -e "/<\/*imageobject>/d" -e "/<textobject>/d" -e "s/imagedata/graphic/" $DBFILE
db2pdf $DBFILE > /dev/null
a2x -f epub --stylesheet=/etc/asciidoc/stylesheets/classy.css "$DOC"
