# Proyecto Colaborativo con Git y GitHub

Este repositorio corresponde a un laboratorio práctico donde se trabaja
en equipo utilizando **Git** y **GitHub** para aprender un flujo de
trabajo colaborativo.

------------------------------------------------------------------------

## Objetivos del proyecto

-   Crear una cuenta en GitHub y configurar Git en el equipo local.
-   Crear un repositorio en GitHub y conectarlo con un repositorio
    local.
-   Trabajar en ramas, realizar commits atómicos, sincronizar
    (push/pull).
-   Abrir Pull Requests (PR), hacer code review y merge.
-   Gestionar Issues, Milestones y Projects (tablero kanban).
-   Resolver conflictos de fusión de manera práctica.
-   Entregar evidencias comprobables de la colaboración de todos los
    integrantes.

------------------------------------------------------------------------

## Requisitos previos

-   Instalar **Git** (Windows/Mac/Linux).
-   Instalar un editor de código (recomendado: **VS Code**).
-   Crear una cuenta en **GitHub**.
-   Formar equipos de **3--4 estudiantes**.
-   Tiempo estimado: **1 clase de 2--3 horas**.

------------------------------------------------------------------------

## Parte 0 --- Preparación

### 0.1 Crear cuenta en GitHub

1.  Ingresar a [github.com](https://github.com) → **Sign up**.
2.  Completar registro y verificación.
3.  Configurar el perfil (nombre completo en *Settings → Profile*) para
    identificar la autoría.

### 0.2 Configurar Git local

Usar el mismo correo registrado en GitHub para que los commits se
asocien correctamente:

``` bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@ejemplo.com"
```

------------------------------------------------------------------------

## Parte 1 --- Crear el repositorio y preparar el flujo

1.  Crear un repositorio en GitHub (líder del equipo).
    -   Nombre sugerido:
        **paradigmas-git-lab-`<sección>`{=html}-`<equipo>`{=html}**
    -   Marcar: *Add a README file* y *Add .gitignore* → seleccionar
        Python (o el lenguaje usado).
    -   Agregar colaboradores en *Settings → Collaborators*.
2.  Clonar el repositorio en local:

``` bash
git clone <URL>
```

3.  (Opcional) Proteger la rama `main` para que solo se fusione mediante
    Pull Requests.

------------------------------------------------------------------------

## Parte 2 --- Proyecto base con código de ejemplo

Se construirá un **mini-proyecto en Python** con funciones simples y
pruebas, ideal para practicar PRs y conflictos controlados.

Estructura de carpetas:

    src/
       utils.py
       app.py
    tests/
       test_utils.py

Funciones de ejemplo en `utils.py`: - `saludo()` - `suma(a, b)` -
`es_par(n)`

Cada integrante deberá: - Crear funciones adicionales (ejemplo:
`producto`, `es_primo`). - Documentar en el `README.md`. - Hacer commit
y push inicial.

------------------------------------------------------------------------

## Parte 3 --- Flujo de trabajo colaborativo

1.  Crear **Issues** asignados a cada integrante (ejemplo: implementar
    función, pruebas o documentación).

2.  Crear ramas con el formato:

        feature/<usuario>/<tarea>

3.  Editar código, agregar funciones y pruebas.

4.  Realizar commit y push.

5.  Abrir **Pull Request** vinculado al Issue correspondiente.

6.  Revisar código de compañeros y aprobar PR (nadie aprueba su propio
    PR).

7.  Realizar merge a `main`.

------------------------------------------------------------------------

## Parte 4 --- Ejercicio de conflicto de fusión

1.  Dos integrantes modifican la misma función `saludo()` en
    `src/utils.py` en ramas diferentes.
    -   **Rama A:** modifica el mensaje de saludo de una forma.
    -   **Rama B:** modifica el saludo de otra forma.
2.  Integrante A hace merge primero.
3.  Integrante B intenta mergear → se genera conflicto.
4.  Resolver manualmente el conflicto en `utils.py`.
5.  Realizar commit, push y completar el PR.

------------------------------------------------------------------------

## Evidencias

Se entregarán capturas y el historial de commits en GitHub para
comprobar la colaboración activa de todos los integrantes.

------------------------------------------------------------------------

## Autoría

Este proyecto fue desarrollado en equipo como parte del laboratorio de
**Paradigmas de Programación** y prácticas de control de versiones con
Git y GitHub.
