def main():
    import pandas as pd
    import geopandas as gpd
    import matplotlib.pyplot as plt

    fp = input('Please, give the file path: ')
    fp1 = input('Please, give shapefile saving location: ')
    fn = input('Please, provide file name: ')
    df = (pd.read_csv(fp))
    df_filtered = df[df['CapacityMWEn'] < 50]
    df_filtered1 = df_filtered.dropna() 
    gdf = gpd.GeoDataFrame(df_filtered1, geometry=gpd.points_from_xy(df_filtered1.Longitude_X, df_filtered1.Latitude_Y ))
    gdf.to_file(f'{fp1}\{fn}')

    restart = input(' Do you want to create a shapefiel? If yes type (Y), else type (N): ').lower()
    if restart == 'y':
        main()

    else:
        exit()

main()




