from partsdb.partsdb import PartsDB
from tables import *
import os.path
import sys

partsdb = PartsDB('postgresql:///dnarchive', clean = False, Base = Base)

dbsession=partsdb.Session()

for record in SeqIO.parse(sys.argv[1], "genbank"):
	sequence = str(record.seq).upper()
	description = record.description
	reference = sys.argv[2]
	trace = "upload"
	name = os.path.splitext(sys.argv[1])[0].split("/")[1]
	print name

	if (len(sys.argv) < 4):
		type = "Undefined"
	else:
		type = sys.argv[3]
				
	entry = partsdb.addPart('entry', name = name, description = description, type = type, reference = reference, seq = sequence, score = 0, votes = 0)

	dbsession.commit()

	partsdb.annotate('annotations', fileName = sys.argv[1], type = type, trace=trace, target = entry)
dbsession.close()
