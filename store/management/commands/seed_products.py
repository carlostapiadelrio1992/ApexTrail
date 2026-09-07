from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Seeds database with distinct products and exact matching product images'

    def handle(self, *args, **options):
        self.stdout.write('Starting database seeding with exact matching images...')

        categories_map = {
            'zapatillas-trail': 'Zapatillas Trail',
            'mochilas-e-hidratacion': 'Mochilas e Hidrataci\u00f3n',
            'ropa-y-capas-tecnicas': 'Ropa y Capas T\u00e9cnicas',
            'nutricion-y-suplementos': 'Nutrici\u00f3n y Suplementos',
            'accesorios-de-montana': 'Accesorios de Monta\u00f1a',
        }

        cat_objs = {}
        for c_slug, c_name in categories_map.items():
            cat_obj, _ = Category.objects.get_or_create(
                slug=c_slug,
                defaults={'name': c_name}
            )
            cat_obj.name = c_name
            cat_obj.save()
            cat_objs[c_slug] = cat_obj

        data = [
            # CATEGORIA 1: Zapatillas Trail (5 Productos)
            {
                "category_slug": "zapatillas-trail",
                "name": "Terrex Agravic Speed Ultra",
                "description": "Dise\u00f1ada para ritmos r\u00e1pidos en distancias ultra. Suela de caucho Continental\u2122 y mediasuela ligera Lightstrike Pro para m\u00e1xima respuesta y retorno de energ\u00eda.",
                "price": 220000,
                "sizes": [38, 39, 40, 41, 42, 43, 44],
                "image": "products/terrex_agravic_speed_ultra.png"
            },
            {
                "category_slug": "zapatillas-trail",
                "name": "Terrex Soulstride Flow",
                "description": "Comodidad suprema en senderos largos. Cuenta con amortiguaci\u00f3n premium Repetitor y suela adherente para transiciones fluidas de asfalto a monta\u00f1a.",
                "price": 160000,
                "sizes": [39, 40, 41, 42, 43, 44, 45],
                "image": "products/terrex_soulstride_flow.png"
            },
            {
                "category_slug": "zapatillas-trail",
                "name": "Terrex Agravic Flow 2",
                "description": "Zapatilla vers\u00e1til ideal para terrenos h\u00famedos y rocosos. Membrana transpirable, amortiguaci\u00f3n Lightstrike y chasis de protecci\u00f3n contra rocas.",
                "price": 180000,
                "sizes": [38, 39, 40, 41, 42, 43, 44, 45],
                "image": "products/terrex_agravic_flow_2.png"
            },
            {
                "category_slug": "zapatillas-trail",
                "name": "Terrex Swift R3 GORE-TEX",
                "description": "Resistente, impermeable y de corte bajo. Construcci\u00f3n de senderismo r\u00e1pido equipada con GORE-TEX para mantener los pies secos y tracci\u00f3n excepcional.",
                "price": 195000,
                "sizes": [39, 40, 41, 42, 43, 44],
                "image": "products/terrex_swift_r3.png"
            },
            {
                "category_slug": "zapatillas-trail",
                "name": "Terrex Free Hiker 2.0",
                "description": "Comodidad de zapatilla deportiva con el soporte de una bota de monta\u00f1a. Mediasuela Boost para retorno de energ\u00eda constante y amortiguaci\u00f3n inigualable.",
                "price": 240000,
                "sizes": [38, 39, 40, 41, 42, 43, 44],
                "image": "products/terrex_free_hiker_2.png"
            },

            # CATEGORIA 2: Mochilas e Hidratación (4 Productos Únicos de Distinto Tipo)
            {
                "category_slug": "mochilas-e-hidratacion",
                "name": "Mochila Chaleco Hidrataci\u00f3n Terrex 12L Ultra Vest",
                "description": "Chaleco ergon\u00f3mico de trail running de 12 litros de capacidad. Incluye 2 soft flasks de 500ml, bolsillos el\u00e1sticos de acceso r\u00e1pido, silbato de emergencia y sujeci\u00f3n para bastones.",
                "price": 115000,
                "sizes": ["Capacidad 12L (Talla S-M)", "Capacidad 12L (Talla M-L)"],
                "image": "products/trail_hydration_vest.jpg"
            },
            {
                "category_slug": "mochilas-e-hidratacion",
                "name": "Chaleco Mochila Salomon Adv Skin 4L Soft Flasks",
                "description": "Mochila chaleco ultra-ligera de 4 litros para entrenamientos y carreras cortas. Tejido de malla mesh transpirable, libre de rebote, con 2 botellas de hidrataci\u00f3n 500ml.",
                "price": 89000,
                "sizes": ["Capacidad 4L (Talla S)", "Capacidad 4L (Talla M)", "Capacidad 4L (Talla L)"],
                "image": "products/trail_salomon_4l_vest.jpg"
            },
            {
                "category_slug": "mochilas-e-hidratacion",
                "name": "Mochila de Alta Monta\u00f1a Alpine Pack 20L Terrex",
                "description": "Mochila t\u00e9cnica de 20 litros resistente a la abrasi\u00f3n para salidas largas de trekking y trail running de autosuficiencia. Compartimento para bolsa de agua de 3L.",
                "price": 135000,
                "sizes": ["Capacidad 20L (Ajustable)"],
                "image": "products/trail_alpine_20l_pack.jpg"
            },
            {
                "category_slug": "mochilas-e-hidratacion",
                "name": "Cintur\u00f3n Ri\u00f1onera Hidrataci\u00f3n Trail Runner 2L",
                "description": "Cintur\u00f3n ergon\u00f3mico sin rebote para llevar 1 soft flask de 500ml, llaves, smartphone y geles. Dise\u00f1o transpirable ultraligero.",
                "price": 35000,
                "sizes": ["Talla S-M (65-80cm)", "Talla L-XL (80-100cm)"],
                "image": "products/trail_running_belt.jpg"
            },

            # CATEGORIA 3: Ropa y Capas Técnicas (4 Productos Únicos de Distinto Tipo)
            {
                "category_slug": "ropa-y-capas-tecnicas",
                "name": "Chaqueta Cortaviento Impermeable TERREX GORE-TEX",
                "description": "Membrana ligera GORE-TEX Paclite transpirable e 100% impermeable (20.000 mm). Capucha ajustada para casco/visera, costuras selladas y plegado compacto ultra-ligero (180g).",
                "price": 175000,
                "sizes": ["S", "M", "L", "XL"],
                "image": "products/trail_waterproof_jacket.jpg"
            },
            {
                "category_slug": "ropa-y-capas-tecnicas",
                "name": "Polera Compresi\u00f3n T\u00e9rmica Transpirable Trail Pro",
                "description": "Polera t\u00e9cnica de secado r\u00e1pido con tejido microperforado en axilas y espalda. Mantiene la temperatura corporal constante en ascensos intensos.",
                "price": 42000,
                "sizes": ["S", "M", "L", "XL"],
                "image": "products/trail_compression_shirt.jpg"
            },
            {
                "category_slug": "ropa-y-capas-tecnicas",
                "name": "Shorts 2-en-1 de Trail con Malla Interna & Bolsillos",
                "description": "Shorts ligeros de 5 pulgadas con malla interna anti-roce de compresi\u00f3n. Cintura el\u00e1stica multi-bolsillo para llevar hasta 4 geles y llaves sin rebote.",
                "price": 48000,
                "sizes": ["S", "M", "L", "XL"],
                "image": "products/trail_shorts_2in1.jpg"
            },
            {
                "category_slug": "ropa-y-capas-tecnicas",
                "name": "Calza T\u00e9rmica Compresi\u00f3n Ultra Trail Tight",
                "description": "Calza larga de compresi\u00f3n graduada con protecci\u00f3n UV50+ y soporte lumbar. Paneles reforzados en rodillas contra la vegetaci\u00f3n de monta\u00f1a.",
                "price": 65000,
                "sizes": ["S", "M", "L", "XL"],
                "image": "products/trail_tights_leggings.jpg"
            },


            # CATEGORIA 4: Nutrición y Suplementos (4 Productos Únicos de Distinto Tipo)
            {
                "category_slug": "nutricion-y-suplementos",
                "name": "Pack Surtido 30 Geles Energ\u00e9ticos & Electr\u00f3litos Ultra Trail",
                "description": "Set completo de 30 geles energ\u00e9ticos surtidos (Maurten, GU, 226ERS) y 4 tubos de electroliitos. Coincide exactamente con la variedad y cantidad mostrada en la imagen.",
                "price": 48000,
                "sizes": ["Mega Pack 30 Geles + Electr\u00f3litos"],
                "image": "products/trail_energy_gels.jpg"
            },
            {
                "category_slug": "nutricion-y-suplementos",
                "name": "Caja 12 Geles Energ\u00e9ticos GU Energy Gel Surtidos",
                "description": "Caja con 12 sobres de geles energ\u00e9ticos GU surtidos (Caramelo Salado, Espresso con Cafe\u00edna, Frutos del Bosque). Carbohidratos de r\u00e1pida absorci\u00f3n con amino\u00e1cidos.",
                "price": 26000,
                "sizes": ["Caja 12 Unidades (Sabores Mix)"],
                "image": "products/trail_gu_gel_box.jpg"
            },
            {
                "category_slug": "nutricion-y-suplementos",
                "name": "Frasco Sales de Hidrataci\u00f3n Electr\u00f3litos SaltStick Caps",
                "description": "100 c\u00e1psulas de electrolitos con sodio, potasio, calcio y magnesio. Previene calambres musculares y la deshidrataci\u00f3n en climas c\u00e1lidos o carreras largas.",
                "price": 24000,
                "sizes": ["Frasco 100 Capsulas"],
                "image": "products/trail_saltstick_bottle.jpg"
            },
            {
                "category_slug": "nutricion-y-suplementos",
                "name": "Prote\u00edna de Recuperaci\u00f3n Muscular BCAA Maurten Recovery",
                "description": "Mezcla de nutrici\u00f3n post-entrenamiento con 20g de prote\u00edna de suero aislada y 5g de BCAA por porci\u00f3n. Acelera la reparaci\u00f3n muscular tras entrenamientos intensos.",
                "price": 54000,
                "sizes": ["Pote 1kg (Chocolate)", "Pote 1kg (Vainilla)"],
                "image": "products/trail_recovery_protein.jpg"
            },

            # CATEGORIA 5: Accesorios de Montaña (4 Productos Únicos con Fotos Exactas)
            {
                "category_slug": "accesorios-de-montana",
                "name": "Bastones Plegables Carbono Trailblaze Z-Pole",
                "description": "Par de bastones ultraligeros de fibra de carbono 100% plegables en 3 tramos con sistema Z-Pole. Empu\u00f1adura de corcho natural anti-sudor y punta de carburo de tungsteno.",
                "price": 98000,
                "sizes": ["115 cm", "120 cm", "125 cm", "130 cm"],
                "image": "products/trail_carbon_poles.jpg"
            },
            {
                "category_slug": "accesorios-de-montana",
                "name": "Linterna Frontal Alta Potencia 900 Lumens Petzl Nao",
                "description": "Frontal recargable de 900 l\u00famenes con tecnolog\u00eda Reactive Lighting que adapta la potencia lum\u00ednica de forma autom\u00e1tica al entorno nocturno de monta\u00f1a.",
                "price": 120000,
                "sizes": ["Unica (Ajustable con Bateria Recargable)"],
                "image": "products/trail_petzl_headlamp.jpg"
            },
            {
                "category_slug": "accesorios-de-montana",
                "name": "Reloj GPS Multideporte Garmin Fenix 7X Solar Sapphire",
                "description": "Reloj multideporte con carga solar Power Sapphire, mapas TopoActive de Chile preinstalados, m\u00e9tricas de estamina en tiempo real y autonom\u00eda de hasta 37 d\u00edas en GPS.",
                "price": 690000,
                "sizes": ["Caja 51mm (Cristal Zafiro Solar)"],
                "image": "products/trail_garmin_watch.jpg"
            },
            {
                "category_slug": "accesorios-de-montana",
                "name": "Visera Deportiva Transpirable & Cuello T\u00e9rmico Buff",
                "description": "Set de visera ultraligera curvada con protecci\u00f3n solar UV50+ y tubular de microfibra multifuncional para proteger cuello y cara contra el viento y sol.",
                "price": 22000,
                "sizes": ["Talla Unica (Elastica)"],
                "image": "products/trail_visor_buff.jpg"
            }
        ]

        for item in data:
            cat_obj = cat_objs[item["category_slug"]]
            prod_slug = slugify(item["name"])
            product, created = Product.objects.get_or_create(
                slug=prod_slug,
                defaults={
                    "category": cat_obj,
                    "name": item["name"],
                    "description": item["description"],
                    "price": item["price"],
                    "sizes": item["sizes"],
                    "image": item["image"],
                    "available": True,
                }
            )
            product.category = cat_obj
            product.description = item["description"]
            product.price = item["price"]
            product.sizes = item["sizes"]
            product.image = item["image"]
            product.save()

        self.stdout.write(self.style.SUCCESS(f'Seeding finished successfully. Total products updated: {Product.objects.count()}'))
