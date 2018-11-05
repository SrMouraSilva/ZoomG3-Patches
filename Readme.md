# Zoom G3 Audio Plugins Presets

## Steps

1. Remove only the old pedalboards ```rm data/pedalboard-info.csv```
1. Obtain pedalboard list: ```scrapy runspider scrap.py -o data/pedalboard-info.csv -t csv```
1. Execute: ```Tratamento de dados 1.ipynb```
1. Execute: ```Tratamento de dados 2.ipynb```
1. Execute: ```Tratamento de dados 3 - Categorias.ipynb```
