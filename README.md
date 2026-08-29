# Separador de Arquivos

Este projeto organiza automaticamente arquivos extraídos de um pacote compactado. Ele descompacta o arquivo informado pelo usuário e separa os itens em pastas diferentes conforme a extensão de cada arquivo.

## Como funciona

1. O usuário digita o nome do arquivo compactado, por exemplo: `arquivo.zip`.
2. O programa usa `shutil.unpack_archive()` para extrair os arquivos dentro de uma pasta chamada `organizador`.
3. Em seguida, ele percorre todos os arquivos extraídos.
4. Para cada arquivo, verifica a extensão, como `.pdf`, `.jpg`, `.txt`, `.zip` e outras.
5. Se a pasta correspondente a essa extensão ainda não existir, ela é criada automaticamente.
6. O arquivo é movido para a pasta correta.

Com isso, documentos, imagens, textos e outros tipos de arquivos ficam organizados de forma automática em subpastas.

## Como usar

1. Coloque o arquivo compactado na mesma pasta do projeto.
2. Execute o programa com Python.
3. Digite o nome do arquivo com a extensão.
4. O programa irá extrair e separar os arquivos automaticamente.

Exemplo:

```bash
Digite o nome do arquivo com extensão: arquivos.zip
```

O resultado será uma pasta `organizador` com subpastas como:

```text
organizador/
├── pdf/
├── jpg/
├── txt/
└── zip/
```

## Tecnologias usadas

- Python
- `pathlib`
- `shutil`

## Objetivo

Simplificar a organização de arquivos após a extração de pastas compactadas, sem precisar separar manualmente cada tipo de arquivo.