# Proyecto Template en Python

Este es un proyecto template en Python que puedes usar como base para tus propios proyectos. La estructura del proyecto está organizada de manera que sea fácil de entender y extender.

## Estructura del Proyecto

```
📦python-project
 ┣ 📂data
 ┃ ┣ 📜mock_data.csv
 ┃ ┗ 📜mock_data.txt
 ┣ 📂modules
 ┃ ┣ 📂module1
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜file.py
 ┃ ┗ 📂module2
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜file.py
 ┣ 📂notebooks
 ┃ ┗ 📜file.ipynb
 ┣ 📂tests
 ┃ ┗ 📜test_main.py
 ┣ 📂utils
 ┃ ┗ 📜common.py
 ┣ 📜.gitignore
 ┣ 📜README.md
 ┣ 📜main.py
 ┗ 📜requirements.txt
```

## Cómo Empezar

1. **Clonar el repositorio**:

   ```sh
   git clone https://github.com/JaviCeRodriguez/python-project
   cd python-project
   ```

2. **Crear y activar un entorno virtual**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Ejecutar el proyecto**:
   ```sh
   python main.py
   ```

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
