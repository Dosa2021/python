from setting import session
from model import Common

res = session.query(Common).all()

session.close()
