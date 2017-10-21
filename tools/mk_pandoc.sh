#!/bin/sh

BASEDIR=$(readlink -f $(dirname $0)/..)
BASENAME=$(basename $1 .md)

# Generate HTML
pandoc -s -S --toc -H ../../style/pandoc/index.css $1 -o $BASENAME.html

# Generate PDF
pandoc -s -S --toc $1 -o $BASENAME.pdf

# Generate EPUB
pandoc -s -S --toc -H ../../style/pandoc/index.css $1 -o $BASENAME.epub
