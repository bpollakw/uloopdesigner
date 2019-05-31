from loopDB import *
from domesticate import predomesticateCDS, domesticate, partColors
import config
import sys
import os.path
from Bio import SeqIO

loopDB = LoopDB( config.DATABASE_URL, clean = False  )
#loopDB = LoopDB( "postgres:///uloop", clean = False  )

def submit(name, part, seq ):
	backbone = loopDB.session.query(Backbone).filter(Backbone.dbid == part).first()

	if seq:
		record = SeqRecord( seq = Seq( seq, IUPAC.unambiguous_dna ) )
	else:
		gbFile = StringIO(base64.decodestring( part["GenBank file"][0]["content"] ) )
		record = SeqIO.read(gbFile, format="genbank")

	if (backbone.name == "CD-CDS" or backbone.name == "CE-CDS"):
		record =  predomesticateCDS(record, backbone)

	record = Seq( backbone.adapter.site5, IUPAC.unambiguous_dna)\
				+ record + Seq( backbone.adapter.site3, IUPAC.unambiguous_dna)

	record = domesticate(record, backbone)

	if record:
			record = record[len(backbone.adapter.site5):-len(backbone.adapter.site3)]

			record.features.insert(0, SeqFeature( FeatureLocation(0, len(record)),
				type = "misc_feature", id = "Part Feature", strand = 1,
					qualifiers = {"label" : [name], "ApEinfo_fwdcolor": [ partColors[backbone.adapter.name] ] } ) )
			try:
				newPart = loopDB.addPart(backbone = backbone, name = name, record = record)
			except:                   # * see comment below
			    loopDB.rollback()
			    raise
			else:
				loopDB.commit()

prom5 = "partsdb.backbone.9"
prom = "partsdb.backbone.10"
utr5 = "partsdb.backbone.11"
cds = "partsdb.backbone.12"
ctag = "partsdb.backbone.13"
term = "partsdb.backbone.14"
TU = "partsdb.backbone.15"

for record in SeqIO.parse(sys.argv[1], "genbank"):
	sequence = str(record.seq).upper()
	name = os.path.splitext(sys.argv[1])[0].split("/")[1]
	ptype = name.split("_")[0]
	name = name.split("_")[1]

	if ptype == "PROM5":
		part = prom5
	elif ptype == "PROM":
		part = prom
	elif ptype == "UTR5":
		part = utr5
	elif ptype == "CDS":
		part = cds
	elif ptype == "CTAG":
		part = ctag
	else:
		part = term
	
submit(name,part,sequence)