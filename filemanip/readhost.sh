#!/bin/bash
# pass a url or list of url "./readhost www.example.com" 
function readhost
{
  HOST=$1
  shift
  PORT=80
  COMMAND="HEAD http://${HOST}/HTTP/1.0"
  
  echo "Sending \"$COMMAND\" to $HOST port $PORT"
  netcat ${HOST} ${PORT} <<-EOF
	${COMMAND}
	
	EOF
  echo "Done!"
}

for host in $@
do
  readhost $host
done