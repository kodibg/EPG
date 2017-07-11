#!/bin/bash -e
no_proxy=sov02lr02
export no_proxy

arg=""
if [[ $@ == "-f" ]]; then echo "Forced download!"; arg="-f"; fi

cd ~/EPG/
#pull recent updates
git pull

#Run the collector
#cd ~/epg-collector/
#echo "Using argument=$arg"
#./generate.py ${arg}

#./validate.py

#cp ./epg.xml ~/EPG/
#cp ./validation.json ~/EPG/
#cd ~/EPG/

wget http://sov02lr02/guides/epg.xml -O epg.xml
gzip < epg.xml > epg.xml.gz
gzip < epg.xml > alltv-guide.xml.gz

#md5sum epg.xml > checksum.txt
cut -d ' ' -f 1 <<< `md5sum epg.xml` > checksum.txt

#remove epg.xml
rm epg.xml

#commit EPG update
echo "Commiting changes to GIT server"
git add -A
git commit -m "Daily EPG update"
echo "Pushing changes to GIT server"
git push
