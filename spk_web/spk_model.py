from settings import NAMA_HP, REPUTASI_BRAND

class BaseMethod():

    def __init__(self, data_dict, **atur_bobot):

        self.database = data_dict

        # 1-6
        self.raw_weight = {
            'Nama_HP': 4,
            'Reputasi_Brand': 5,
            'Processor_Antutu': 3,
            'Baterai': 2,
            'Harga': 6,
            'Ukuran_Layar': 1
        }

        if atur_bobot:
            for item in atur_bobot.items():
                temp1 = atur_bobot[item[0]]
                temp2 = {v: k for k, v in atur_bobot.items()}[item[1]]
                atur_bobot[item[0]] = item[1]
                atur_bobot[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'Nama': handphone['Nama_HP'],
            'Nama_HP': NAMA_HP["".join([x for x in NAMA_HP.keys() if x.lower() in handphone['Nama_HP'].lower()])],
            'Reputasi_Brand': REPUTASI_BRAND[handphone['Reputasi_Brand']],
            'Processor_Antutu': handphone['Processor_Antutu'],
            'Baterai': int(handphone['Baterai'].replace(" mAh", "")),
            'Harga': float(handphone['Harga'].replace(" jutaan", "")),
            'Ukuran_Layar': handphone['Ukuran_Layar']
        } for handphone in self.database]

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
            'Nama': data['Nama'],
            'Nama_HP': data['Nama_HP']/max_nama_hp,
            'Reputasi_Brand': data['Reputasi_Brand']/max_reputasi_brand,
            'Processor_Antutu': data['Processor_Antutu']/max_processor_antutu,
            'Baterai': data['Baterai']/max_baterai,
            'Harga': min_harga/data['Harga'],
            'Ukuran_Layar': data['Ukuran_Layar']/max_ukuran_layar,
        } for data in self.data]
 

class WeightedProduct(BaseMethod):
    def __init__(self, database, atur_bobot:dict):
        super().__init__(data_dict=database, **atur_bobot)

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
        print(self.data)
        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1]))
