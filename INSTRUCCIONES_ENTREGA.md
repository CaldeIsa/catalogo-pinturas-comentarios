# Instrucciones para la Entrega del Proyecto

## Archivos a Entregar

Para entregar este proyecto, debes incluir los siguientes archivos y carpetas:

### 1. Documentación (OBLIGATORIO)
- `Documentacion_Catalogo_Pinturas.pdf` - Documento PDF con el modelo E/R y explicación del proyecto

### 2. Código Fuente y Datos
- Carpeta `client/` completa (SIN la carpeta `node_modules`)
- Archivo `generar_datos.py` - Script para generar los datos
- Archivo `README.md` - Instrucciones del proyecto
- Archivo `package.json` - Dependencias del proyecto

### 3. Archivos de Configuración
- `tsconfig.json`
- `vite.config.ts`
- `tailwind.config.ts`
- `.gitignore`

## IMPORTANTE: NO Incluir node_modules

**NUNCA incluyas la carpeta `node_modules` en tu entrega.** Esta carpeta contiene miles de archivos de dependencias que se pueden reinstalar fácilmente con el comando `pnpm install`.

## Cómo Preparar la Entrega

### Opción 1: Archivo ZIP (Recomendado)

```bash
# Desde el directorio catalogo-pinturas
cd /home/ubuntu/catalogo-pinturas

# Crear archivo ZIP excluyendo node_modules
zip -r catalogo-pinturas-entrega.zip . -x "*/node_modules/*" -x "node_modules/*" -x ".git/*"
```

### Opción 2: Copiar archivos manualmente

1. Crea una carpeta nueva llamada `catalogo-pinturas-entrega`
2. Copia todos los archivos EXCEPTO `node_modules`
3. Comprime la carpeta en un archivo ZIP

## Verificación Antes de Entregar

Asegúrate de que tu entrega incluya:

- ✅ Documento PDF con el modelo E/R
- ✅ Carpeta `client/public/data/` con todos los archivos JSON
- ✅ Carpeta `client/public/images/` con todas las imágenes
- ✅ Carpeta `client/src/` con todo el código fuente
- ✅ Archivos de configuración (package.json, vite.config.ts, etc.)
- ✅ README.md con instrucciones
- ❌ NO incluir carpeta `node_modules`
- ❌ NO incluir carpeta `.git`

## Despliegue en Netlify

Para desplegar el proyecto en Netlify:

1. Crea una cuenta en https://www.netlify.com
2. Sube tu proyecto (puedes arrastrarlo directamente a Netlify)
3. Configura los comandos de build:
   - Build command: `pnpm build`
   - Publish directory: `client/dist`
4. Netlify instalará automáticamente las dependencias y construirá el proyecto
5. Copia la URL generada y agrégala al documento PDF

## Reinstalar Dependencias (Para el Profesor)

Si el profesor necesita ejecutar el proyecto localmente:

```bash
# Instalar dependencias
pnpm install

# Ejecutar en modo desarrollo
pnpm dev
```

## Contacto

Si tienes dudas sobre la entrega, consulta con el profesor.
