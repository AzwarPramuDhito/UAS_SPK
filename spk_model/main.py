import sys

from colorama import Fore, Style
from models import Base, Handphone
from engine import engine

from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import NAMA_HP, REPUTASI_BRAND

session = Session(engine)

def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!')

class BaseMethod():

    def __init__(self):
        # 1-6
        self.raw_weight = {
            'Nama_HP': 4,
            'Reputasi_Brand': 5,
            'Processor_Antutu': 3,
            'Baterai': 2,
            'Harga': 6,
            'Ukuran_Layar': 1
        }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Handphone)
        return [{
            'Nama': handphone.Nama_HP,
            'Nama_HP': NAMA_HP["".join([x for x in NAMA_HP.keys() if x.lower() in handphone.Nama_HP.lower()])],
            'Reputasi_Brand': REPUTASI_BRAND[handphone.Reputasi_Brand],
            'Processor_Antutu': handphone.Processor_Antutu,
            'Baterai': int(handphone.Baterai.replace(" mAh", "")),
            'Harga': float(handphone.Harga.replace(" jutaan", "")),
            'Ukuran_Layar': handphone.Ukuran_Layar
        } for handphone in session.scalars(query)]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]

        nama_hp = [] # max
        reputasi_brand = [] # max
        processor_antutu = [] # max
        baterai = [] # max
        harga = [] # min
        ukuran_layar = [] # max


        for data in self.data:
            nama_hp.append(data['Nama_HP'])
            reputasi_brand.append(data['Reputasi_Brand'])
            processor_antutu.append(data['Processor_Antutu'])
            baterai.append(data['Baterai'])
            harga.append(data['Harga'])
            ukuran_layar.append(data['Ukuran_Layar'])

        max_nama_hp = max(nama_hp)
        max_reputasi_brand = max(reputasi_brand)
        max_processor_antutu = max(processor_antutu)
        max_baterai = max(baterai)
        min_harga = min(harga)
        max_ukuran_layar = max(ukuran_layar)

        return [{
            'Nama': data['Nama_HP'],
            'Nama_HP': data['Nama_HP']/max_nama_hp,
            'Reputasi_Brand': data['Reputasi_Brand']/max_reputasi_brand,
            'Processor_Antutu': data['Processor_Antutu']/max_processor_antutu,
            'Baterai': data['Baterai']/max_baterai,
            'Harga': min_harga/data['Harga'],
            'Ukuran_Layar': data['Ukuran_Layar']/max_ukuran_layar,
        } for data in self.data]
 

class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {row['Nama']:
            round(
                row['Nama_HP'] ** weight['Nama_HP'] *
                row['Reputasi_Brand'] ** weight['Reputasi_Brand'] *
                row['Processor_Antutu'] ** weight['Processor_Antutu'] *
                row['Baterai'] ** weight['Baterai'] *
                row['Harga'] ** weight['Harga'] *
                row['Ukuran_Layar'] ** weight['Ukuran_Layar']
                , 2
            )
            for row in self.normalized_data}
        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1]))

class SimpleAdditiveWeighting(BaseMethod):
    
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result = {row['Nama']:
            round(
                row['Nama_HP'] * weight['Nama_HP'] +
                row['Reputasi_Brand'] * weight['Reputasi_Brand'] +
                row['Processor_Antutu'] * weight['Processor_Antutu'] +
                row['Baterai'] * weight['Baterai'] +
                row['Harga'] * weight['Harga'] +
                row['Ukuran_Layar'] * weight['Ukuran_Layar']
                , 2
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1]))

def run_saw():
    saw = SimpleAdditiveWeighting()
    print('result:', saw.calculate)

def run_wp():
    wp = WeightedProduct()
    print('result:', wp.calculate)

if len(sys.argv)>1:
    arg = sys.argv[1]

    if arg == 'create_table':
        create_table()
    elif arg == 'saw':
        run_saw()
    elif arg =='wp':
        run_wp()
    else:
        print('command not found')
