import geopandas as gpd
import os
from typing import Tuple


class GeoJSONProcessor:
    def __init__(self) -> None:
        pass

    def distribute_trips(
            self, manzanas_geojson: str, macrozonas_geojson: str, output_geojson: str
    ) -> str:
        """
        Combina manzanas y macrozonas, distribuyendo el número de viajes por macrozona a las manzanas que la conforman,
        proporcionalmente a la población o densidad de cada manzana.

        Args:
            manzanas_geojson (str): Ruta del archivo GeoJSON de manzanas.
            macrozonas_geojson (str): Ruta del archivo GeoJSON de macrozonas.
            output_geojson (str): Ruta para guardar el archivo GeoJSON combinado.

        Returns:
            str: Ruta del archivo GeoJSON generado.
        """
        # Cargar los GeoJSON
        print("Cargando archivos GeoJSON...")
        manzanas_gdf = gpd.read_file(manzanas_geojson)
        macrozonas_gdf = gpd.read_file(macrozonas_geojson)

        # Verificar que ambos GeoDataFrames tengan CRS compatible
        if manzanas_gdf.crs != macrozonas_gdf.crs:
            print("Reproyectando manzanas al CRS de macrozonas...")
            manzanas_gdf = manzanas_gdf.to_crs(macrozonas_gdf.crs)

        # Inicializar una columna para almacenar los viajes en las manzanas
        manzanas_gdf["viajes_destino"] = 0

        # Iterar sobre cada macrozona para distribuir sus viajes entre las manzanas
        print("Distribuyendo viajes...")
        for _, macrozona in macrozonas_gdf.iterrows():
            # Geometría y datos de la macrozona
            macrozona_geom = macrozona["geometry"]
            viajes_macro = macrozona["viaj_dest"]

            # Seleccionar las manzanas dentro de la macrozona
            manzanas_en_macro = manzanas_gdf[manzanas_gdf.geometry.intersects(macrozona_geom)]

            # Si no hay manzanas, continuar
            if manzanas_en_macro.empty:
                continue

            # Calcular la población total dentro de la macrozona
            poblacion_total = manzanas_en_macro["pob_tot"].sum()

            # Distribuir los viajes proporcionalmente según la población
            manzanas_gdf.loc[
                manzanas_en_macro.index, "viajes_destino"
            ] += manzanas_en_macro["pob_tot"] / poblacion_total * viajes_macro

        # Guardar el GeoJSON con la nueva información
        print("Guardando archivo GeoJSON combinado...")
        manzanas_gdf.to_file(output_geojson, driver="GeoJSON")

        return output_geojson
