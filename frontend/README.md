## React

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