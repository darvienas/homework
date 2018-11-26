'''Zip file attached contains newest Norway geospatial data for postal codes and their areas.

Please draw Norway map separating each and every postal code area(could be a bit clustered in more
densely populated areas) and provide the number of unique postal codes.

When finished please create a repository in Github and upload the solution there.

Result: map picture in easily readable format(.jpeg,.png etc.), number of unique numbers, link to Github repository.
'''

import matplotlib.pyplot as plt
import geopandas as gpd


# file_link = '/home/justis/PycharmProjects/homework/Basisdata_0000_Norge_25833_Postnummeromrader_SOSI_PostnummeromrЖde_FLATE.shp'

file = gpd.read_file('Basisdata_0000_Norge_25833_Postnummeromrader_SOSI_PostnummeromrЖde_FLATE.shp')
unique_codes = file['POSTNUMMER'].nunique()
print('Unique values: ', unique_codes)

file.plot(figsize=(10, 10), edgecolor='black', linewidth=0.1, column='POSTNUMMER')
plt.title('Postal code areas in Norway')
plt.xticks(ticks=[0, 1E6])
plt.show()
    # plt.savefig('map_N.jpeg')







