"""
This file contains the Piccolo models for the database.
"""

from piccolo.table import Table
from piccolo.columns import Timestamptz, Text, JSON, UUID, ForeignKey, M2M
from piccolo.columns.indexes import IndexMethod
from piccolo.columns.column_types import ForeignKey, LazyTableReference, Varchar


class User(Table):
    user_id = UUID(primary_key=True)
    phone_number = Varchar(length=12)
    created_at = Timestamptz()
    properties = M2M(LazyTableReference("UserFavoriteProperty", module_path=__name__))


class RealEstateProperty(Table):
    property_id = UUID(primary_key=True)
    title = Text(required=True, index=True)
    location = Text(required=True, index=True)
    description = Text()
    price = Varchar(length=100, required=True)
    image_url = Text()
    latitude = Varchar(length=100)
    longitude = Varchar(length=100)
    created_at = Timestamptz()
    updated_at = Timestamptz()
    deleted_at = Timestamptz()
    metadata = JSON()
    users = M2M(LazyTableReference("UserFavoriteProperty", module_path=__name__))


class UserFavoriteProperty(Table):
    user = ForeignKey(User)
    property = ForeignKey(RealEstateProperty)
