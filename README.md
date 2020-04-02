
# Métodos Numéricos II (CK0048)

### Configuração
É necessário instalar alguns requisitos para iniciar o projeto. Na pasta raiz, execute:

```console
pip3 install -r requirements.txt
```

Também é possível criar um ambiente virtual para a instalação dos requisitos. Esse ambiente deve ser nomeado ```.env```.
Exemplo:

```console
python3 -m venv .env/
```
```console
/bin/bash .env/bin/pip3 install -r requirements.txt
```

Após a configuração, execute o programa.

```console
python3 src/main.py
```

### Metodologia
Foram usadas as libs **numpy** e **OpenCV** nesse projeto. A última, apesar de fazer tratamento completo de imagens (entre outros), foi utilizada apenas para leitura e conversão.

Os filtros de imagem estão no arquivo ``main.py``.
Três filtros foram implementados:

 - Box blur
 - Gaussian blur
 - Edge detection

O arquivo ``Image.py`` é a classe que engloba a imagem. Ela é responsável por:

 - Ler a imagem
 - Converter para escala de cinza
 - Normalizar (0 - 255 :arrow_right: 0 - 1)
 - Aplicar filtros
 
Por padrão, a imagem ``cubes.png`` está sendo tratada com os filtros *box_blur* e *edge_detection*.
