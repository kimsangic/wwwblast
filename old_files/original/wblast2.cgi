#!/bin/csh -f

#
# $Id: wblast2.cgi,v 1.1 2002/08/06 19:03:52 dondosha Exp $
#

echo "Content-type: text/html"
echo ""

#setenv DEBUG_COMMAND_LINE TRUE
setenv BLASTDB db

cat ./HEADER_2.html
./wblast2.REAL
