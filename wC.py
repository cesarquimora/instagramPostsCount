import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator

def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 21.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

def generar_wordcloud(dataframe):
    colors = ImageColorGenerator(np.array(Image.open('bicep.jpeg')))
    dataframe['diferencia'] = dataframe['conteo'].diff().fillna(0)
    dataframe.loc[0, 'diferencia'] = 373
    print(dataframe.head())
    # Crea un diccionario de palabras y sus recuentos
    word_counts = {row[0]: row[4] for _, row in dataframe.iterrows()}
    # Crea un objeto WordCloud
    wordcloud = WordCloud(width=2000, 
                          height=1000,
                          background_color='white',
                          color_func=random_color_func,
                          max_font_size = 1000,
                          min_font_size = 25).generate_from_frequencies(word_counts)

    # Visualiza el WordCloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

generar_wordcloud(pd.read_csv('linksRecorded.csv'))