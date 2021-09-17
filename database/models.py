from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Clientes(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key= True, index=True, auto_increment=True)
    Nome = Column(String, index=True)
    NumeroUC = Column(String)
    UCsCompensacao = Column(Text, default=Null)
    Localizacao = Column(String)
    CEP = Column(String)
    Bairro = Column(String)
    Email = Column(String, unique=True, index=True)
    Telefone = Column(String)
    CPF_CNPJ = Column(String, unique=True, index=True)
    FormaPagamento = Column(Text)
    Notas = Column(Text)

class DadosConcessionarias(Base):
    __tablename__ = "concessionarias"
    id = Column(Integer, primary_key= True, index=True, auto_increment=True)
    CargaInstalada = Column(Float, precision=3)
    PadraoEntrada = Column(String)
    TensaoAtendimento = Column(String)
    TipoConexao = Column(String)
    PotenciaInstalada = Column(Float, precision=3)
    PotenciaModulos = Column(Float, precision=3)
    PotenciaInversores = Column(Float, precision=3)
    NumeroArranjos = Column(Integer)

    id_clientes = Column(Integer, ForeignKey('clientes.id'))