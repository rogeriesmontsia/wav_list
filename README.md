# WaveList: React + Vite + Docker + FastAPI

## Description
Educational aplication to learn tecnhologies

## Usage

### Installing
Use this command:
```sh
docker
```


### Folder structure

Here's a folder structure :

```
wave-list/     # Root directory.
|- backend/        # Folder with the server side API (FastAPI)
    |- src/   
|- frontend/       # Folder with the client (REACT)

```

### Tailwindcss
Use this command:
```sh
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm install @headlessui/react @heroicons/react
```

# React

<aside>
💡 Instruccions per a la creació projecte React + Vite + Docker

</aside>

```bash

npm create vite@latest .

```

Aquesta comanda utilitza npm per crear un nou projecte Vite amb la versió més recent (latest) de Vite. Aquí està una desglossament de la comanda:

- **npm**: Aquesta és la interfície de línia de comandes per a la gestió de paquets de Node.js. npm es fa servir per instal·lar, gestionar i compartir paquets de JavaScript.
- **create**: Aquesta és una subcomanda proporcionada per npm que es fa servir per crear nous projectes basats en plantilles predefinides o en generadors.
- **vite@latest**: Aquesta part de la comanda especifica que vols utilitzar la versió més recent (latest) del paquet Vite com a plantilla per al nou projecte. Vite és un entorn de desenvolupament ràpid per a aplicacions basades en JavaScript i TypeScript.
- **.**: Aquest punt indica el directori actual com a destinació per al nou projecte. En aquest cas, el projecte Vite es crearà dins del directori on estàs executant la comanda.

Per tant, quan executes aquesta comanda, npm descarregarà la versió més recent de Vite i utilitzarà aquesta plantilla per crear un nou projecte Vite al directori actual. Després d'executar aquesta comanda, pots navegar al directori del nou projecte i començar a treballar en el teu codi.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f73331bd-c47b-4250-834e-e23ac210f93e/af8dccd0-5cd7-4105-af55-bec20c943a41/Untitled.png)

```bash
npm install

```

La comanda **`npm install`** s'utilitza per instal·lar les dependències d'un projecte Node.js. Quan executes aquesta comanda al directori del teu projecte, npm examina el fitxer **`package.json`** del teu projecte per veure quines dependències estan especificades i les descarrega i instal·la

```bash
npm run dev

```

La comanda **`npm run dev`** s'utilitza per executar un script anomenat "dev" que està definit al fitxer **`package.json`** del teu projecte. Aquest script generalment es configura per iniciar un entorn de desenvolupament local per al teu projecte.

<aside>
💡 Si dona error  Unexpected token o semblant revisar la versió de nodejs i instala·lar la última. Amb node -v podeu veure la versió (amb la v14.19 no funciona)

</aside>

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f73331bd-c47b-4250-834e-e23ac210f93e/3806cd64-506e-467c-8c99-e92960abc1fd/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f73331bd-c47b-4250-834e-e23ac210f93e/8c3716c2-7bd0-4b9b-8937-a491199aab0b/Untitled.png)

Creem fitxer Dockerfile i .dockerignore

```docker
FROM node AS build_stage
WORKDIR /app
COPY package.json .
RUN npm i
COPY . .
RUN npm run build

#Production stage
FROM node:latest AS production_stage
WORKDIR /app
COPY --from=build_stage /app/dist/ /app/dist/
EXPOSE 8080

COPY package.json .
CMD ["npm", "run","preview"]
```

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

Tailwindcss

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```css
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
```

```bash
npm install @headlessui/react @heroicons/react
```

https://tailwindcomponents.com/