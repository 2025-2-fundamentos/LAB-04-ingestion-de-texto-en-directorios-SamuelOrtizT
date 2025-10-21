# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import glob
import os
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    def read_data(input_folder, sentiment):
        data = []
        files = glob.glob(f"{input_folder}*")
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                line = f.readline()
                data.append((line, sentiment))

        return data

    folder_routes = ["files/input/test/negative/",
                     "files/input/test/neutral/", 
                     "files/input/test/positive/",
                     "files/input/train/negative/", 
                     "files/input/train/neutral/", 
                     "files/input/train/positive/"]

    complete_data_test = []
    complete_data_train = []
    counter = 0
    for folder in folder_routes:
        counter += 1
        sentiment = folder.split("/")[3]
        data = read_data(folder, sentiment)
        if counter <= 3:
            complete_data_test += data
        else:
            complete_data_train += data

    df_test = pd.DataFrame(complete_data_test, columns=["phrase", "target"])
    df_train = pd.DataFrame(complete_data_train, columns=["phrase", "target"])

    directory = "files/output/"
    if os.path.exists(directory):
        for file in glob.glob(f"{directory}/*"):
            os.remove(file)
    else:
        os.makedirs(directory)

    df_test.to_csv("files/output/test_dataset.csv", sep=",", header=True, index=False)
    df_train.to_csv("files/output/train_dataset.csv", sep=",", header=True, index=False)

if __name__ == "__main__":
    pregunta_01()
