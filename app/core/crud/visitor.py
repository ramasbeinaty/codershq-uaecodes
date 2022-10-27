import string
import ipaddress
from sqlalchemy.orm import Session

from app.db.repos.visitor import add_visitor_repo

def add_visitor(db:Session, ip_address: string, url_key: string):

    # ip = ipaddress.ip_address(ip_address)
    visitor = None

    try:
        visitor = add_visitor_repo(db=db, ip_address=ip_address, url_key=url_key)
        print("INFO: Successfully recorded visitor")
    except Exception as e:
        raise Exception("visitor is already recorded or ip address is not in a correct format - ", e)

    return visitor