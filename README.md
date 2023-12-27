# Clase final


```bash
cp .env.template .env
python3 -m pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```


## configuracion de postgres

``` bash
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres:13.2-alpine

docker build . -f docker/Dockerfile -t adabaspython
docker run adabaspython python main.py
```

## Modelo de datos
- [DER Adabas](https://frlputneduar-my.sharepoint.com/:u:/g/personal/fetcheverri_alu_frlp_utn_edu_ar/Ed1uzxybvolGp_M6ZvJS0PQBmZpqCW6w-4T-GDW7m4lROQ?e=pPvSlv)