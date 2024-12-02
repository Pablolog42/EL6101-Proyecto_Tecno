from GeoJSONProcessor import GeoJSONProcessor
from MapMaker import MapMaker
processor = GeoJSONProcessor()
mapper = MapMaker()

manzanas_geojson = r"C:\Users\pablo\Escritorio\EL6101-Proyecto_Tecno\data\Poblacin_Total_Santiago_de_Chile_2012-cud.geojson"
macrozonas_geojson = r"C:\Users\pablo\Escritorio\EL6101-Proyecto_Tecno\app-testing\test\out\Cantidad_de_viajes_de_destino_EOD_06-filtered--33.41449365894426_-70.75006766509088_-33.515023008314486_-70.55780694267634.geojson"
output_geojson = r"C:\Users\pablo\Escritorio\EL6101-Proyecto_Tecno\data\Manzanas_combinadas.geojson"

result_geojson = processor.distribute_trips(manzanas_geojson, macrozonas_geojson, output_geojson)
print(f"Archivo GeoJSON generado: {result_geojson}")

#viajes_destino

