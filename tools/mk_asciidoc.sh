#!/bin/sh

BASEDIR=$(readlink -f $(dirname $0)/..)

# Generate HTML
asciidoc -a theme=classy -a toc -a toclevels=3 -a numbered -b html5 $1

# Generate Docbook xml
asciidoc -a toc -a toclevels=3 -a numbered -a imagesdir=`pwd`/ -b docbook $1

# Fix docbook and generate PDF
DBFILE=`basename $1 .txt`.xml
sed -i -e "/<\/*mediaobject>/ d" -e "/<\/*imageobject>/d" -e "/<textobject>/d" -e "s/imagedata/graphic/" $DBFILE
db2pdf $DBFILE > /dev/null

# Generate Epub
#a2x -f epub --stylesheet=/etc/asciidoc/stylesheets/classy.css $1

cp $BASEDIR/style/asciidoc/classy.css $(dirname $1)
a2x -f epub --stylesheet=classy.css $1
rm $(dirname $1)/classy.css
