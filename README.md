# Extract csv read and writer
### Ambiente de desenvolvimento
Tecnologias utilizadas:
* src/requirements.txt
* Docker/Docker compose


## Caso não queira rodar o docker configure sua ide para o python 3.10 ou superior e execure via run
### Run file:///home/eduardorodriguesdelfino/Documentos/laboratorio/extract-csv/src/img/run_script.png


## Run com o docker
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




