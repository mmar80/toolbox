#!/bin/sh
# sometimes you just wanna make a tempdir, do a thing, and then delete it

TEMPDIR=`mktemp -d` || exit 1
echo "This is a file in my temporary directory" > $TEMPDIR/file1
echo "This is another file in my temporary directory" > $TEMPDIR/file2
pwd $TEMPDIR
ls -la $TEMPDIR
rm -rf $TEMPDIR
