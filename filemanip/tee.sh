# tee the disk usage into a file
df -h | tee disk_usage.txt
# tee out a cron and sed old to new
crontab -l | tee crontab-backup.txt | sed 's/old/new/' | crontab –
# ping someone and tee out the result to a file
ping google.com -c 10 | tee -i ping.txt