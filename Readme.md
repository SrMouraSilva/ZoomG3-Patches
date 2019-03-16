# Zoom G3 Patches

Scripts to obtain Zoom G3 patches

## Prepare dataset

1. Create virtualenv ```python3 -m venv venv```
1. Start virtualenv ```source venv/bin/activate```
1. Install dependencies ```python setup.py develop```
1. Maybe requires
```
sudo apt-get update -y
sudo apt-get install -y python3-dev
sudo apt-get install -y libxml2-dev libxslt1-dev
sudo apt-get install -y libssl-dev libffi-dev
sudo apt install bsdtar
```

Scrap data

1. Remove the old pedalboards data ```rm data/pedalboard-info.csv```
1. Obtain pedalboard list: ```scrapy runspider scrap.py -o data/pedalboard-info.csv -t csv```

Prepare data

1. ```jupyter notebook```
1. (Optinal) Open and execute all: ```Processing_data_1_-_audio_plugins.ipynb```
1. Open and execute all steps: ```Processing_data_2_-_Collect_patches_data.ipynb```
1. Open and execute all steps: ```Processing_data_3_-_data_transformations```
1. Open and execute all steps: ```Processing_data_3_-_Bag_of_plugins.ipynb```

## Dataset

Dataset info are presented in [Database.ipynb](Database.ipynb) file.