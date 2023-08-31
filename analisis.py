# Biblio: BioPython
from Bio.Blast import NCBIXML
from blast import output_file

# Cargar los resultados BLAST desde el archivo XML
blast_records = NCBIXML.parse(open(output_file))

# Iterar sobre los registros BLAST y obtener información
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print("Secuencia:", alignment.title)
            print("Score:", hsp.score)
            print("E-value:", hsp.expect)
            print("Identidad:", hsp.identities)
            print("Alineación:", hsp.query)
            print("             ", hsp.match)
            print("             ", hsp.sbjct)
            print()
