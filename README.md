# Extract csv read and writer
### Ambiente de desenvolvimento
Tecnologias utilizadas:
* src/requirements.txt
* Docker/Docker compose


## Caso não queira rodar o docker configure sua ide para o python 3.10 ou superior e execure via run

```
file:///home/eduardorodriguesdelfino/Documentos/laboratorio/extract-csv/src/img/configure_sdk.png
![run_script](https://github.com/eduardodelfinozup/extract-csv/assets/116813394/96499831-8cb3-475d-b8b2-fe7eb75404cd)


```

docker-compose up --build
```

```
docker-compose dow
```

## Deverá colocar o arquivo de leitura na pasta: read  ao rodar o docker o csv será criado na pasta writer

```
.
├── docker-compose.yaml
├── README.md
└── src
    ├── Dockerfile
    ├── extract_kafka_event.py
    ├── read
    │   └── BUG410.csv
    ├── requirements.txt
    └── writer
        └── parametros_extraidos.csv

```




