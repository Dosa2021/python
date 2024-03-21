from sqlalchemy import Table
from setting import Engine
from setting import Base


class Common(Base):
    """
    共通(キー)データテーブルのモデルクラス

    物理名: common
    論理名: 共通(キー)データ
    """
    __table__ = Table('common', Base.metadata,
                      autoload_with=Engine)
