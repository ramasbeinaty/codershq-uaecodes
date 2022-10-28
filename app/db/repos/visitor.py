
from sqlalchemy.orm import Session

import string
from ipaddress import ip_address

from app.db.models import Visitor


def add_visitor_repo(db:Session, ip_address: string, url_key: string):

    visitor = Visitor(ip_address=ip_address, url=url_key)

    db.add(visitor)
    db.commit()
    db.refresh(visitor)
    return visitor
