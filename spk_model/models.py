from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Handphone(Base):
    __tablename__ = "handphone"

    Nama_HP : Mapped[str] = mapped_column(primary_key=True)
    Reputasi_Brand : Mapped[str]
    Processor_Antutu : Mapped[int]
    Baterai : Mapped[str]
    Harga : Mapped[str]
    Ukuran_Layar : Mapped[float]

    def __repr__(self) -> str :
        return f"Nama_HP={self.Nama_HP}, Reputasi_Brand={self.Reputasi_Brand}, Processor_Antutu={self.Processor_Antutu}, Baterai={self.Baterai}, Harga={self.Harga}, Ukuran_Layar={self.Ukuran_Layar}"
