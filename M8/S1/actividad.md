1. **Total de películas en `movies`**

````javascript
db.movies.countDocuments({})
````

2. **Total de teatros en `theaters`**

````javascript
db.theaters.countDocuments({})
````

3. **Ver qué información guarda un teatro (ejemplo de campos)**

````javascript
db.theaters.findOne(
  {},
  {
    theaterId: 1,
    "location.address.street1": 1,
    "location.address.city": 1,
    "location.address.state": 1,
    "location.address.zipcode": 1,
    "location.geo": 1,
    _id: 0
  }
)
````

4. **Película “The Great Train Robbery” (actores y géneros)**

````javascript
db.movies.find(
  { title: "The Great Train Robbery" },
  { title: 1, cast: 1, genres: 1, _id: 0 }
)
````

6. **Películas dirigidas por Jack Perez (solo títulos)**

````javascript
db.movies.find(
  { directors: "Jack Perez" },
  { title: 1, _id: 0 }
)
````

7. **Películas con rating ≥ 9.0**

- Para verlas:

````javascript
db.movies.find(
  { "imdb.rating": { $gte: 9.0 } }
)
````

- Para contarlas:

````javascript
db.movies.countDocuments(
  { "imdb.rating": { $gte: 9.0 } }
)
````

8. **Mayor rating (orden descendente, primera película)**

````javascript
db.movies.find(
  { "imdb.rating": { $gte: 9.0 } }
).sort(
  { "imdb.rating": -1 }
).limit(1)
````

9. **Proyección solo de `title` y `imdb.rating`**

````javascript
db.movies.find(
  { "imdb.rating": { $gte: 9.0 } },
  { title: 1, "imdb.rating": 1, _id: 0 }
).sort(
  { "imdb.rating": -1 }
)
````

10. **5 peores evaluadas (título y rating)**

````javascript
db.movies.find(
  {},
  { title: 1, "imdb.rating": 1, _id: 0 }
).sort(
  { "imdb.rating": 1 }
).limit(5)
````

---

Respuestas usando la base `sample_mflix` (versión estándar de MongoDB Atlas) y/o lo que puedes ver en Compass:

1. **¿Cuántas películas hay en `movies`?**En la versión estándar de `sample_mflix` hay **23,539** documentos en `movies`.En tu Compass: pestaña **Documents**, mira el contador **Documents** arriba a la derecha para confirmar.
2. **¿Cuántos teatros hay en `theaters`?**En la versión estándar hay **1,174** documentos en `theaters`.Igualmente, confirma en Compass con el contador **Documents**.
3. **¿Qué información se almacena de un teatro? (al menos 5 campos)**En un documento típico de `theaters` verás, por ejemplo:

   - `_id`
   - `theaterId`
   - `location.address.street1`
   - `location.address.city`
   - `location.address.state`
   - `location.address.zipcode`
   - `location.geo.type`
   - `location.geo.coordinates`

   Con eso ya cumples más de 5 campos.
4. **Película “The Great Train Robbery”**
   Filtro en Compass (barra **Filter**):

   ```json
   { "title": "The Great Train Robbery" }
   ```

   En la versión estándar:

   - **Actores (`cast`)**:`["Gilbert M. 'Broncho Billy' Anderson", "A.C. Abadie", "George Barnes", "Justus D. Barnes"]`
   - **Géneros (`genres`)**:
     `["Short", "Western"]`

---

6. **Director Jack Perez**

   Filtro:

   ```json
   { "directors": "Jack Perez" }
   ```

   En Compass, mira la lista de documentos devueltos y copia los títulos desde el campo `title`.(No puedo ver tu base directamente; los títulos exactos los ves tú en Compass.)
7. **Películas con rating ≥ 9.0**

   Filtro:

   ```json
   { "imdb.rating": { "$gte": 9.0 } }
   ```

   En Compass, arriba a la derecha, revisa el contador **Documents** para contestar:**¿Cuántas películas cumplen esta condición?** → ese número es tu respuesta.
8. **Ordenar por rating descendente**

   Mantén el filtro anterior y en **Sort** escribe:

   ```json
   { "imdb.rating": -1 }
   ```

   La **película con mayor rating** será el **primer documento**.Toma de ahí:

   - `title` → nombre de la película
   - `imdb.rating` → puntuación
9. **Proyección de campos (Project)**

   En **Project** pon:

   ```json
   { "title": 1, "imdb.rating": 1, "_id": 0 }
   ```

   **¿Qué pasó con el resto de la información?**Solo se muestran los campos que pusiste con valor `1` (y se oculta `_id` al ponerlo en `0`).El resto de los campos **no se devuelven en el resultado**, aunque siguen existiendo en la colección.
10. **Peores evaluadas**

   Deja el filtro de 7 (o quítalo si quieres ver todas) y configura:

- **Sort**:

  ```json
  { "imdb.rating": 1 }
  ```
- **Project**:

  ```json
  { "title": 1, "imdb.rating": 1, "_id": 0 }
  ```
- **Limit**: `5`

   Los **5 primeros documentos** serán las peor evaluadas.
   Anota 2 títulos de esa lista para tu respuesta (por ejemplo, las 2 primeras filas en Compass).
