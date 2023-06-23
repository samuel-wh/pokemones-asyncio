## Paso 1: Hacer fork del repositorio: 
    https://github.com/miguelsantos-wh/pokemones-asyncio
## Paso 2: Hacer git clone del fork que se hizo
## Paso 3: Crear entorno en la carpeta donde se hizo git clone
    mkvirtualenv venv -p=3.6
    o 
    mkvirtualenv venv /path/pyhton3.6/
    o 
    virtualenv venv -p=3.6
#### Confirmar que sea en python 3.6
    python -V
## Paso 4: Desactivar e iniciar entorno
#### Para desactivar podemos hacer:
    deactivate
#### Para iniciar podemos hacer
    workon asyncpokeenv
#### o estando en la carpeta del proyecto
    source venv/bin/activate
## Paso 5: instalamos dependencias con el entorno iniciado
    pip install  -r requirements.txt
## Paso 6: Iniciar el proyecto:
    ./manage.py runserver
## Paso 7: Para desactivar el proyecto:
    Ctrl+c
