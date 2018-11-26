import matplotlib.pyplot as plt
import geopandas as gpd

file_path = '~/Basisdata_0000_Norge_25833_Postnummeromrader_SOSI_PostnummeromrЖde_FLATE.shp'
file = gpd.read_file(file_path)
unique_codes = file['POSTNUMMER'].nunique()
print('Number of unique postal codes: ', unique_codes)

file.plot(figsize=(10, 10), edgecolor='black', linewidth=0.1, column='POSTNUMMER')
plt.title('Postal code areas in Norway')
plt.xticks(ticks=[0, 1E6])
plt.show()

# plt.savefig('map_N.jpeg')







