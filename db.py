import subprocess

# Rutas y nombres de archivos
input_ruta_genome = input("Ingrese el nombre de la secuencia: ")
input_ruta_path = f'./db/{input_ruta_genome}_datasets/ncbi_dataset/data/protein.faa'
db_type = input("Ingrese el tipo de base de datos (prot/nucl): ")
fasta = input_ruta_path
db_name = input_ruta_genome + "_db"

# Comando para crear la base de datos
makeblastdb_cmd = [
    "makeblastdb",
    "-in", fasta,
    "-dbtype", db_type,
    "-out", f'./_db/{input_ruta_genome}/{db_name}',
]

# Ejecutar el comando para crear la base de datos
try:
    subprocess.run(makeblastdb_cmd, check=True)
    print("Base de datos creada exitosamente.")
except subprocess.CalledProcessError as e:
    print("Error al crear la base de datos:", e)
