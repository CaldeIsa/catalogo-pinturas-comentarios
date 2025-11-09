import json
import os

# Datos de pinturas
pinturas = [
    {
        "id": "mona-lisa",
        "titulo": "Mona Lisa (La Gioconda)",
        "año": "1503-1519",
        "tecnica": "Óleo sobre tabla de álamo",
        "descripcion": "Retrato de Lisa Gherardini, esposa del comerciante florentino Francesco del Giocondo. Es famosa por su enigmática sonrisa y su mirada penetrante. Representa una innovación en el arte renacentista.",
        "dimensiones": "77 cm × 53 cm",
        "artista_id": "leonardo-da-vinci",
        "museo_id": "museo-del-louvre",
        "imagen": "mona-lisa.jpg"
    },
    {
        "id": "la-ultima-cena",
        "titulo": "La Última Cena",
        "año": "1495-1498",
        "tecnica": "Fresco",
        "descripcion": "Representa el momento en que Jesús anuncia que uno de sus apóstoles lo traicionará. Es una obra maestra de la perspectiva y composición renacentista.",
        "dimensiones": "460 cm × 880 cm",
        "artista_id": "leonardo-da-vinci",
        "museo_id": "santa-maria-delle-grazie",
        "imagen": "la-ultima-cena.jpg"
    },
    {
        "id": "la-noche-estrellada",
        "titulo": "La Noche Estrellada",
        "año": "1889",
        "tecnica": "Óleo sobre lienzo",
        "descripcion": "Vista nocturna desde la ventana del manicomio de Saint-Rémy-de-Provence. Caracterizada por pinceladas arremolinadas y colores vibrantes de azul y amarillo.",
        "dimensiones": "73.7 cm × 92.1 cm",
        "artista_id": "vincent-van-gogh",
        "museo_id": "moma",
        "imagen": "la-noche-estrellada.jpg"
    },
    {
        "id": "los-girasoles",
        "titulo": "Los Girasoles",
        "año": "1888",
        "tecnica": "Óleo sobre lienzo",
        "descripcion": "Serie de naturalezas muertas con girasoles en un jarrón. Representa la búsqueda de Van Gogh por capturar la luz y el color del sur de Francia.",
        "dimensiones": "92 cm × 73 cm",
        "artista_id": "vincent-van-gogh",
        "museo_id": "museo-van-gogh",
        "imagen": "los-girasoles.jpg"
    },
    {
        "id": "guernica",
        "titulo": "Guernica",
        "año": "1937",
        "tecnica": "Óleo sobre lienzo",
        "descripcion": "Alegato contra la guerra que representa el bombardeo de la ciudad vasca de Guernica durante la Guerra Civil Española. Obra maestra del cubismo.",
        "dimensiones": "349 cm × 776 cm",
        "artista_id": "pablo-picasso",
        "museo_id": "museo-reina-sofia",
        "imagen": "guernica.jpg"
    },
    {
        "id": "las-senoritas-de-avignon",
        "titulo": "Las Señoritas de Avignon",
        "año": "1907",
        "tecnica": "Óleo sobre lienzo",
        "descripcion": "Considerada la obra que inició el movimiento cubista. Representa cinco figuras femeninas con influencias del arte africano e ibérico.",
        "dimensiones": "243.9 cm × 233.7 cm",
        "artista_id": "pablo-picasso",
        "museo_id": "moma",
        "imagen": "las-senoritas-de-avignon.jpg"
    },
    {
        "id": "el-beso",
        "titulo": "El Beso",
        "año": "1907-1908",
        "tecnica": "Óleo sobre lienzo con pan de oro",
        "descripcion": "Pareja abrazándose con túnicas decoradas con motivos geométricos. Obra cumbre del Período Dorado de Klimt con influencias bizantinas.",
        "dimensiones": "180 cm × 180 cm",
        "artista_id": "gustav-klimt",
        "museo_id": "belvedere",
        "imagen": "el-beso.jpg"
    },
    {
        "id": "la-joven-de-la-perla",
        "titulo": "La Joven de la Perla",
        "año": "1665",
        "tecnica": "Óleo sobre lienzo",
        "descripcion": "Tronie de una joven con turbante azul y dorado y un pendiente de perla. Conocida como la 'Mona Lisa del Norte' por su expresión enigmática.",
        "dimensiones": "44.5 cm × 39 cm",
        "artista_id": "johannes-vermeer",
        "museo_id": "mauritshuis",
        "imagen": "la-joven-de-la-perla.jpg"
    },
    {
        "id": "el-grito",
        "titulo": "El Grito",
        "año": "1893",
        "tecnica": "Óleo, temple y pastel sobre cartón",
        "descripcion": "Figura andrógina en un puente con las manos en el rostro, expresando angustia existencial. Icono del expresionismo y símbolo de la ansiedad moderna.",
        "dimensiones": "91 cm × 73.5 cm",
        "artista_id": "edvard-munch",
        "museo_id": "museo-nacional-noruega",
        "imagen": "el-grito.jpg"
    },
    {
        "id": "las-meninas",
        "titulo": "Las Meninas (La Familia de Felipe IV)",
        "año": "1656",
        "tecnica": "Óleo sobre lienzo",
        "descripcion": "Obra maestra del barroco español que muestra a la infanta Margarita rodeada de sus damas de compañía. Juega con la perspectiva y los reflejos.",
        "dimensiones": "318 cm × 276 cm",
        "artista_id": "diego-velazquez",
        "museo_id": "museo-del-prado",
        "imagen": "las-meninas.jpg"
    },
    {
        "id": "el-nacimiento-de-venus",
        "titulo": "El Nacimiento de Venus",
        "año": "1485",
        "tecnica": "Temple sobre lienzo",
        "descripcion": "Representa a la diosa Venus emergiendo del mar sobre una concha. Uno de los primeros desnudos paganos del Renacimiento italiano.",
        "dimensiones": "172.5 cm × 278.9 cm",
        "artista_id": "sandro-botticelli",
        "museo_id": "galeria-uffizi",
        "imagen": "el-nacimiento-de-venus.jpg"
    },
    {
        "id": "la-creacion-de-adan",
        "titulo": "La Creación de Adán",
        "año": "1511",
        "tecnica": "Fresco",
        "descripcion": "Fresco del techo de la Capilla Sixtina que muestra a Dios dando vida a Adán. Icónica imagen de las manos casi tocándose.",
        "dimensiones": "280 cm × 570 cm",
        "artista_id": "miguel-angel",
        "museo_id": "capilla-sixtina",
        "imagen": "la-creacion-de-adan.jpg"
    }
]

# Datos de artistas
artistas = [
    {
        "id": "leonardo-da-vinci",
        "nombre": "Leonardo da Vinci",
        "nacimiento": "1452",
        "fallecimiento": "1519",
        "nacionalidad": "Italia",
        "movimiento": "Renacimiento",
        "biografia": "Polímata del Renacimiento italiano, fue pintor, escultor, arquitecto, científico e inventor. Considerado uno de los mayores genios de la humanidad, sus obras representan la perfección técnica y el humanismo renacentista.",
        "imagen": "leonardo-da-vinci.jpg"
    },
    {
        "id": "vincent-van-gogh",
        "nombre": "Vincent van Gogh",
        "nacimiento": "1853",
        "fallecimiento": "1890",
        "nacionalidad": "Países Bajos",
        "movimiento": "Post-impresionismo",
        "biografia": "Pintor post-impresionista holandés cuya obra, notable por su belleza, emoción y color, influyó enormemente en el arte del siglo XX. A pesar de su genio, vivió en la pobreza y luchó con enfermedades mentales.",
        "imagen": "vincent-van-gogh.jpg"
    },
    {
        "id": "pablo-picasso",
        "nombre": "Pablo Picasso",
        "nacimiento": "1881",
        "fallecimiento": "1973",
        "nacionalidad": "España",
        "movimiento": "Cubismo",
        "biografia": "Pintor y escultor español, cofundador del cubismo y uno de los artistas más influyentes del siglo XX. Su obra abarca múltiples estilos y períodos, desde el azul y rosa hasta el cubismo y el surrealismo.",
        "imagen": "pablo-picasso.jpg"
    },
    {
        "id": "gustav-klimt",
        "nombre": "Gustav Klimt",
        "nacimiento": "1862",
        "fallecimiento": "1918",
        "nacionalidad": "Austria",
        "movimiento": "Art Nouveau / Simbolismo",
        "biografia": "Pintor simbolista austriaco y figura prominente del movimiento Art Nouveau vienés. Conocido por sus pinturas decorativas, retratos y murales con pan de oro y motivos eróticos.",
        "imagen": "gustav-klimt.jpg"
    },
    {
        "id": "diego-velazquez",
        "nombre": "Diego Velázquez",
        "nacimiento": "1599",
        "fallecimiento": "1660",
        "nacionalidad": "España",
        "movimiento": "Barroco",
        "biografia": "Pintor barroco español, considerado uno de los máximos exponentes de la pintura española y maestro de la pintura universal. Fue pintor de la corte del rey Felipe IV.",
        "imagen": "diego-velazquez.jpg"
    },
    {
        "id": "edvard-munch",
        "nombre": "Edvard Munch",
        "nacimiento": "1863",
        "fallecimiento": "1944",
        "nacionalidad": "Noruega",
        "movimiento": "Expresionismo",
        "biografia": "Pintor y grabador noruego, pionero del expresionismo. Su obra explora temas como la vida, el amor, el miedo, la muerte y la melancolía, reflejando su propia angustia existencial.",
        "imagen": "edvard-munch.jpg"
    }
]

# Datos de museos
museos = [
    {
        "id": "museo-del-louvre",
        "nombre": "Museo del Louvre",
        "ciudad": "París",
        "pais": "Francia",
        "fundacion": "1793",
        "descripcion": "El museo de arte más grande y visitado del mundo. Ubicado en el antiguo palacio real del Louvre, alberga aproximadamente 380,000 objetos y exhibe 35,000 obras de arte en ocho departamentos curatoriales.",
        "sitio_web": "https://www.louvre.fr",
        "imagen": "museo-del-louvre.jpg"
    },
    {
        "id": "moma",
        "nombre": "Museum of Modern Art",
        "ciudad": "Nueva York",
        "pais": "Estados Unidos",
        "fundacion": "1929",
        "descripcion": "Uno de los museos de arte moderno y contemporáneo más influyentes del mundo. Fundado por Abby Aldrich Rockefeller, Lillie P. Bliss y Mary Quinn Sullivan. Alberga obras desde finales del siglo XIX hasta la actualidad.",
        "sitio_web": "https://www.moma.org",
        "imagen": "moma.jpg"
    },
    {
        "id": "museo-reina-sofia",
        "nombre": "Museo Nacional Centro de Arte Reina Sofía",
        "ciudad": "Madrid",
        "pais": "España",
        "fundacion": "1992",
        "descripcion": "Museo nacional español de arte del siglo XX y contemporáneo. Alberga la colección más completa de arte español moderno, incluyendo obras maestras de Picasso, Dalí y Miró.",
        "sitio_web": "https://www.museoreinasofia.es",
        "imagen": "museo-reina-sofia.jpg"
    },
    {
        "id": "museo-del-prado",
        "nombre": "Museo Nacional del Prado",
        "ciudad": "Madrid",
        "pais": "España",
        "fundacion": "1819",
        "descripcion": "Uno de los museos más importantes del mundo, con la mejor colección de pintura española. Diseñado por Juan de Villanueva en 1785, alberga obras maestras de Velázquez, Goya, El Bosco y muchos otros.",
        "sitio_web": "https://www.museodelprado.es",
        "imagen": "museo-del-prado.jpg"
    },
    {
        "id": "galeria-uffizi",
        "nombre": "Galería de los Uffizi",
        "ciudad": "Florencia",
        "pais": "Italia",
        "fundacion": "1581",
        "descripcion": "Uno de los museos de arte más antiguos y famosos del mundo. Alberga la colección más importante de arte renacentista italiano, con obras de Botticelli, Leonardo, Miguel Ángel y Rafael.",
        "sitio_web": "https://www.uffizi.it",
        "imagen": "galeria-uffizi.jpg"
    },
    {
        "id": "belvedere",
        "nombre": "Österreichische Galerie Belvedere",
        "ciudad": "Viena",
        "pais": "Austria",
        "fundacion": "1903",
        "descripcion": "Complejo de palacios barrocos que alberga la colección de arte austriaco más importante del mundo, desde la Edad Media hasta la actualidad. Famoso por su colección de obras de Gustav Klimt.",
        "sitio_web": "https://www.belvedere.at",
        "imagen": "belvedere.jpg"
    }
]

# Crear directorios si no existen
os.makedirs('/home/ubuntu/catalogo-pinturas/client/public/data/pinturas', exist_ok=True)
os.makedirs('/home/ubuntu/catalogo-pinturas/client/public/data/artistas', exist_ok=True)
os.makedirs('/home/ubuntu/catalogo-pinturas/client/public/data/museos', exist_ok=True)

# Generar archivos JSON para pinturas
for pintura in pinturas:
    filename = f"/home/ubuntu/catalogo-pinturas/client/public/data/pinturas/{pintura['id']}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(pintura, f, ensure_ascii=False, indent=2)

# Generar archivos JSON para artistas
for artista in artistas:
    filename = f"/home/ubuntu/catalogo-pinturas/client/public/data/artistas/{artista['id']}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(artista, f, ensure_ascii=False, indent=2)

# Generar archivos JSON para museos
for museo in museos:
    filename = f"/home/ubuntu/catalogo-pinturas/client/public/data/museos/{museo['id']}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(museo, f, ensure_ascii=False, indent=2)

# Generar índices
indices = {
    "pinturas": [p['id'] for p in pinturas],
    "artistas": [a['id'] for a in artistas],
    "museos": [m['id'] for m in museos]
}

with open('/home/ubuntu/catalogo-pinturas/client/public/data/indices.json', 'w', encoding='utf-8') as f:
    json.dump(indices, f, ensure_ascii=False, indent=2)

print("Archivos JSON generados exitosamente!")
print(f"- {len(pinturas)} pinturas")
print(f"- {len(artistas)} artistas")
print(f"- {len(museos)} museos")
