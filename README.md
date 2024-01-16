# WaveList: React + Vite + Docker + FastAPI

## Description
Educational aplication to learn tecnhologies

## [FastAPI](/backend/README.md) 

## [React ](/frontend/README.md)

## Usage
Use this command:
```
docker-compose up --build
npm run dev
```
### Installing
Use this command:
```
npm run install
```


### Folder structure

Here's a folder structure :

```
wave-list/     # Root directory.
|- backend/        # Folder with the server side API (FastAPI)
    |- src/   
|- frontend/       # Folder with the client (REACT)

```

## Tailwindcss
Use this command:
```sh
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm install @headlessui/react @heroicons/react
```


https://tailwindcomponents.com/


## Docker

Creem fitxer Dockerfile i .dockerignore

```bash
docker build -t vite-react-app:latest .
```
La comanda **`docker build -t vite-react-app:latest .`** s'utilitza per construir una imatge de Docker a partir del context actual (**`.`**, que significa el directori actual) i etiquetar-la amb el nom **`vite-react-app`** i la versió **`latest`**.

Aquí tens una desglossament de la comanda:

- **`docker build`:** Aquesta comanda s'utilitza per construir una imatge de Docker a partir d'un fitxer Dockerfile i d'un context específic.
- **`t vite-react-app:latest`:** L'opció **`t`** es fa servir per etiquetar la imatge amb un nom i opcionalment una versió o etiqueta. En aquest cas, l'etiqueta **`t vite-react-app:latest`** significa que l'imatge es etiquetarà com a **`vite-react-app`** amb la versió **`latest`**. L'etiqueta **`latest`** és una convenció que sovint es fa servir per indicar l'última versió d'una imatge.
- **`.`:** Aquest és el context de construcció, és a dir, el directori on es troba el fitxer Dockerfile i qualsevol recurs necessari per a la construcció de la imatge. En aquest cas, **`.`** indica el directori actual

```bash
docker images | grep vite-react-app
docker run -p 8080:8080 vite-react-app:latest
```


