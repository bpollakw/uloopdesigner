# Usage sh load.sh directory_where_files_are_contained reference

DIR=$1
ls  ${DIR}* > list
while read line; do python load.py "$line"; done < list