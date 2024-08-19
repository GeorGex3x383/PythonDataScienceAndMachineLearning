import pandas as pd
ruta = "C:/Users/jemil/Documents/CursosYMas/CursoPythonDSyML/6_Día/medallas.csv"
df = pd.read_csv(ruta)
df.shape
df.head()
df.info()
df.describe()
df_relleno = df.fillna(0)
df_relleno["Oro"] = df_relleno["Oro"].astype(int)
df_relleno["Plata"] = df_relleno["Plata"].astype(int)
df_relleno["Bronce"] = df_relleno["Bronce"].astype(int)
print(df_relleno)
top_3_oro = df_relleno.sort_values('Oro', ascending=False).head(3)
print(top_3_oro)
filtro = df_relleno['Total'] > 10 
mas_de_10_medallas = df[filtro]
mas_de_10_medallas.sort_values('Total', ascending=False)
print(mas_de_10_medallas)