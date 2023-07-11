class Komputer(object):
    def __init__(self, nama, pabrikan, harga, jenis):
        self.nama = nama
        self.pabrikan = pabrikan
        self.harga = harga
        self.jenis = jenis

    def info(self):
        print(f'Nama\t\t: {self.nama}')
        print(f'Pabrikan\t: {self.pabrikan}')
        print(f'Harga\t\t: Rp. {self.harga}')
        print(f'Jenis\t\t: {self.jenis}')


class Processor(Komputer):
    def __init__(self, nama, pabrikan, harga, jenis, cpu, generasi, core):
        super().__init__(nama, pabrikan, harga, jenis)
        self.cpu = cpu
        self.generasi = generasi
        self.core = core

    def infoCPU(self):
        print(f'CPU\t\t: {self.cpu} generasi ke-{self.generasi}, {self.core} core')


class RAM(Komputer):
    def __init__(self, nama, pabrikan, harga, jenis, memori):
        super().__init__(nama, pabrikan, harga, jenis)
        self.memori = memori

    def infoRAM(self):
        print(f'RAM\t\t: {self.memori} GB')


class Hardisk(Komputer):
    def __init__(self, nama, pabrikan, harga, jenis, penyimpanan):
        super().__init__(nama, pabrikan, harga, jenis)
        self.penyimpanan = penyimpanan

    def infoHardisk(self):
        print(f'Hardisk\t\t: {self.penyimpanan} TB')


cpu = Processor('Lenovo Slim 15i', '14ITL05', 15000000, 'laptop', 'Intel', 11, 8)
ram = RAM('Lenovo Slim 15i', '14ITL05', 15000000, 'laptop', 16)
hardisk = Hardisk('Lenovo Slim 15i', '14ITL05', 15000000, 'laptop', 1)


Komputer.info(cpu)
cpu.infoCPU()
ram.infoRAM()
hardisk.infoHardisk()
