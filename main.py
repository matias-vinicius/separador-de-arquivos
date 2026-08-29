from pathlib import Path
import shutil

arquivo_escolha = input("Digite o nome do arquivo com extensão: ")

arquivo = Path(f'{arquivo_escolha}')

organizador = Path('organizador')

shutil.unpack_archive(arquivo, organizador)

for arquivo in organizador.iterdir():
    extensao = arquivo.suffix
    arquivos_organizados = organizador / extensao

    if not arquivos_organizados.exists():
        arquivos_organizados.mkdir(parents=True, exist_ok=True)

    shutil.move(arquivo, arquivos_organizados)