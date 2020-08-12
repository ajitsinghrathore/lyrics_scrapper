import pandas as pd
import  matplotlib.pyplot as plt
import numpy as np




data_frame = pd.read_csv(r"C:\Users\Ajit\Desktop\lyrics scraping\L_scrapper\lyrics.csv")

counts = data_frame['genere'].value_counts()

slices = counts._values
labels_here = counts.index.values
explode_here = np.zeros(counts.shape)
explode_here = np.full(counts.shape,0.1)


plt.pie(
        x=slices,
        labels = labels_here,
        startangle=90,
        shadow= True,
        explode=explode_here, 
        autopct="%1.1f%%"
)


plt.show()

print(counts)
