#!/bin/sh
# sometimes you just wanna make a temp file with random name then delete it
TEMPFILE='mktemp' || exit 1
echo "This is my tempfile. There are many like it but this is mine." > $TEMPFILE
cat $TEMPFILE
pwd $TEMPFILE
ls -lah $TEMPFILE
rm -rf $TEMPFILE