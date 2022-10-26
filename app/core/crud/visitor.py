import string
from ipaddress import ip_interface
from sqlalchemy.orm import Session

from app.db.repos.visitor import add_visitor_repo

def add_visitor(db:Session, ip_address: string, server_url: string):

    ip = ip_interface(ip_address)
    visitor = None

    try:
        visitor = add_visitor_repo(db=db, ip_address=ip, url=server_url)
    except Exception as e:
        raise Exception("WARNING: visitor could not be added. Visitor might have previously visited url", e)

    return visitor