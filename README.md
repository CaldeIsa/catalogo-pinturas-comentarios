# Catálogo de Pinturas Famosas

Proyecto académico de manejo de datos con React - Catálogo interactivo de pinturas famosas con información sobre artistas y museos.

## Descripción

Este proyecto implementa un catálogo web interactivo que presenta 12 pinturas famosas, 6 artistas destacados y 6 museos de renombre mundial. El sitio permite navegar entre las entidades relacionadas (pinturas, artistas y museos) de manera fluida e intuitiva.

## Estructura de Datos

El proyecto utiliza tres entidades:

- **Pintura** (Entidad Principal): 12 registros con 6 campos de datos
- **Artista** (Entidad Secundaria): 6 registros con 4 campos de datos
- **Museo** (Entidad Secundaria): 6 registros con 4 campos de datos

Los datos se almacenan en archivos JSON individuales en `client/public/data/`.

## Tecnologías Utilizadas

- React 19
- TypeScript
- Wouter (enrutamiento)
- Tailwind CSS 4
- shadcn/ui (componentes)
- Vite (build tool)

## Instalación y Ejecución

```bash
# Instalar dependencias
pnpm install

# Ejecutar en modo desarrollo
pnpm dev

# Construir para producción
pnpm build
```

## Estructura del Proyecto

```
catalogo-pinturas/
├── client/
│   ├── public/
│   │   ├── data/          # Archivos JSON de datos
│   │   └── images/        # Imágenes de pinturas, artistas y museos
│   └── src/
│       ├── components/    # Componentes reutilizables
│       ├── pages/         # Páginas de la aplicación
│       └── App.tsx        # Configuración de rutas
├── documentacion.md       # Documentación del proyecto
├── Documentacion_Catalogo_Pinturas.pdf  # Documentación en PDF
└── generar_datos.py       # Script para generar archivos JSON
```

## Navegación

El sitio permite navegar:

- Desde pinturas hacia artistas y museos
- Desde artistas hacia sus pinturas
- Desde museos hacia las pinturas que albergan

## Autor

Proyecto académico desarrollado para la asignatura de Desarrollo Web.

## Licencia

Este proyecto tiene fines exclusivamente educativos.
