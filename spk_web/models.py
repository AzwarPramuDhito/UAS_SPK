import numpy as np
import pandas as pd
from spk_model import WeightedProduct

class Handphone():

    def __init__(self) -> None:
        self.handphone = pd.read_csv('uas_spk.csv')

    def get_recs(self, kriteria:dict):
        wp = WeightedProduct(self.handphone.to_dict(orient="records"), kriteria)
        return wp.calculate

