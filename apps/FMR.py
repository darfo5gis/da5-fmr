import streamlit as st
import leafmap.kepler as leafmap
import geopandas as gpd

def app():
    st.title("Region 5 Farm-to-Market Roads")
    
    m= leafmap.Map(center=[13.5, 123.15], zoom=8)
    
    FMRs = (
        'https://raw.githubusercontent.com/darfo5gis/da5-fmr/main/data/2014-2020_FMRs.geojson'
    )
    proposed_FMRs = (
        'https://raw.githubusercontent.com/darfo5gis/da5-fmr/main/data/FMR_Proposed.geojson'
    )
    OSM_Railroads = (
        'https://raw.githubusercontent.com/darfo5gis/da5-fmr/main/data/OSM_Railroads_R5.geojson'
    )
    OSM_Roads = (
        'https://raw.githubusercontent.com/darfo5gis/da5-fmr/main/data/OSM_Roads_R5_new.geojson'
    )

    gdf_FMRs = gpd.read_file(FMRs)
    gdf_proposed_FMRs = gpd.read_file(proposed_FMRs)
    gdf_Railroads = gpd.read_file(OSM_Railroads)
    gdf_Roads = gpd.read_file(OSM_Roads)

    m.add_gdf(gdf_FMRs, layer_name='Existing FMRs (2014-2020)')
    m.add_gdf(gdf_proposed_FMRs, layer_name='Proposed FMRs')
    m.add_gdf(gdf_Railroads, layer_name='Railroad')
    m.add_gdf(gdf_Roads, layer_name='Philippine Road Network')
    #m.load_config(config)
    m.to_streamlit(height=900, width=900, responsive=True, scrolling=True)