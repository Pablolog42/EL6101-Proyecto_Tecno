from MapMaker import MapMaker


esquina_superior_izquierda = -33.43965406365402, -70.6759945090866
esquina_inferior_derecha = -33.45702086573408, -70.64393674766406
input_geojson = r"C:\Users\pablo\Escritorio\EL6101-Proyecto_Tecno\data\Manzanas_combinadas.geojson"

map_maker = MapMaker()
filtered_geojson = map_maker.filter_geojson_by_bbox(input_geojson, esquina_superior_izquierda, esquina_inferior_derecha)
print(f"GeoJSON filtrado guardado en: {filtered_geojson}")



## generar heatmap
#parameter = "viaj_dest" # aca igual está segregado por tipo de viaje: compras_06, salud_06, ...
parameter = "viajes_destino" # aca igual está segregado por tipo de viaje: compras_06, salud_06, ...

# output_html = "mapa_calor-EOD.html"

output_html = "mapa_calor-EOD-manzanas-plasmado.html"


map_maker.generate_heatmap(filtered_geojson, parameter, output_html, title="Viajes con destino sector - EOD")
print(f"Mapa de calor guardado en: {output_html}")
