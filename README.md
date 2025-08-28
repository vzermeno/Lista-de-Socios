# Lista de Socios

Esta es una herramienta web interactiva para gestionar una lista de socios. Permite a los usuarios agregar datos de socios desde un formato de texto crudo, organizarlos en una tabla, agruparlos por número de membresía y editar campos específicos directamente en la interfaz.

## Características Principales

-   **Análisis Inteligente de Datos:** La herramienta utiliza un analizador heurístico para extraer información de líneas de texto con formato irregular (separadas por tabulaciones).
-   **Procesamiento en Lotes:** Permite pegar un bloque de texto con múltiples registros (separados por punto y coma) y procesarlos de forma iterativa.
-   **Agrupación de Socios:** Agrupa automáticamente a los socios por su número de membresía, mostrando una jerarquía visual clara.
-   **Prioridad de "Owner":** Dentro de un grupo, el socio con el estatus "Owner" siempre se muestra en la parte superior.
-   **Interfaz Interactiva:**
    -   La fecha de llegada se establece una vez para un lote de registros, agilizando la entrada de datos.
    -   Las columnas "RC" y "Notas" son editables directamente en la tabla.
    -   La tabla es ordenable por cualquiera de sus columnas.
    -   Se pueden eliminar socios individualmente.
-   **Control de Duplicados:** Evita que se agreguen socios con un ZMGR que ya existe en la lista.

## Instalación

1.  Clona el repositorio a tu máquina local.
2.  Abre una terminal en la raíz del proyecto.
3.  Instala las dependencias necesarias usando npm:
    ```bash
    npm install
    ```

## Uso

1.  Para iniciar el servidor de desarrollo local, ejecuta el siguiente comando en la terminal:
    ```bash
    npm run dev
    ```
2.  Esto abrirá automáticamente la aplicación en tu navegador web en la dirección `http://localhost:3000` (o un puerto similar).
3.  Usa el botón **"Cambiar Fecha de Llegada"** para seleccionar la fecha de llegada para los socios que vas a agregar.
4.  Pega uno o más registros de socios (separados por `;`) en el área de texto.
5.  Haz clic en el botón **"Agregar Socio"** para procesar el primer registro de la lista. El sistema lo analizará, lo agregará a la tabla y lo eliminará del área de texto.
6.  Repite el paso anterior para procesar los registros restantes.
7.  Haz clic en las celdas de las columnas "RC" y "Notas" para añadir o editar información.