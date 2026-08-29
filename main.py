from pathlib import Path
import shutil


def organizar_arquivos(arquivo_entrada: str) -> None:
    arquivo = Path(arquivo_entrada).expanduser()

    if not arquivo.exists():
        print(f"Arquivo não encontrado: {arquivo_entrada}")
        return

    if not arquivo.is_file():
        print(f"O caminho informado não é um arquivo válido: {arquivo_entrada}")
        return

    organizador = Path("organizador")
    organizador.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(arquivo), str(organizador))
    except (shutil.ReadError, ValueError) as erro:
        print(f"Arquivo inválido ou não suportado: {erro}")
        return

    for item in organizador.iterdir():
        if item.is_dir():
            continue

        extensao = item.suffix.lower().lstrip(".")

        if not extensao:
            print(f"Arquivo sem extensão ignorado: {item.name}")
            continue

        pasta_destino = organizador / extensao
        pasta_destino.mkdir(exist_ok=True)
        shutil.move(str(item), str(pasta_destino / item.name))

    print(f"Arquivos organizados em: {organizador.resolve()}")


if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo com extensão: ").strip()
    organizar_arquivos(nome_arquivo)
    