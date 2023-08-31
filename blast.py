import subprocess

# Rutas a los archivos de entrada y salida
input_ruta_genome = input("Ingrese el nombre de la secuencia: ")
input_db = input("Ingrese el nombre de la base de datos: ")
input_fasta_path = f'./db/{input_ruta_genome}_datasets/ncbi_dataset/data/protein.faa'
db_path = f'./_db/{input_ruta_genome}/{input_ruta_genome}_db'
output_file = f'./blast/{input_ruta_genome}.xml'

# Comando BLAST a ejecutar
blast_cmd = [
    "blastp",         # Puedes cambiar esto según el tipo de BLAST que desees ejecutar
    "-query", input_fasta_path,
    "-out", output_file,
    "-db", db_path,
    "-outfmt", "5",   # Formato de salida XML
    "-evalue", "0.001"
]

# Ejecutar BLAST+ y capturar la salida
try:
    subprocess.run(blast_cmd, check=True, text=True)
    print("BLAST ejecutado exitosamente.")
except subprocess.CalledProcessError as e:
    print("Error al ejecutar BLAST:", e)

# Procesar el archivo de salida XML
