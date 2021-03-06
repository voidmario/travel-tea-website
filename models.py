"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth
from pydal.validators import *


def get_user_email():
    return auth.current_user.get('email') if auth.current_user else "Unknown"


def get_time():
    return datetime.datetime.utcnow()


### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later

db.define_table('country_rating', 
                Field('beaches', 'integer', default=0,requires=IS_INT_IN_RANGE(0, 11)),
                Field('sights', 'integer', default=0,
                requires=IS_INT_IN_RANGE(0, 11)),
                Field('food', 'integer', default=0,
                requires=IS_INT_IN_RANGE(0, 11)),
                Field('nightlife', 'integer', default=0,
                requires=IS_INT_IN_RANGE(0, 11)),
                Field('shopping', 'integer', default=0,
                requires=IS_INT_IN_RANGE(0, 11)),
                   
)


db.define_table('country',
                Field('name', 'string'),
                Field('code', 'string'),
                Field('biography', 'string'),
                Field('thumbnail', 'text'),
                Field('country_rating', 'reference country_rating')
)


db.define_table('place',
                Field('name', 'string'),
                Field('address','string', default=""),
                Field('city','string', default=""),
                Field('state','string', default=""),
                Field('country', 'reference country'),
                Field('thumbnail', 'text'),
                Field('type', 'string', default=""),
)

db.define_table(
    'user',
    Field('user_email', default=get_user_email, writable=False),
    Field('username', 'string'),
    Field('biography', 'string'),
    
)

db.define_table('posts',
                Field('title', default=""),
                Field('post_text', default=""),
                Field('username', default=""),
                Field('email', default=get_user_email()),
                Field('user', 'reference auth_user'),
                Field('image', 'text', default=""),
                Field('place', 'reference place'),
                Field('country', 'string'),
                Field('overall', 'integer', default=0, IS_INT_IN_RANGE=(0, 6)),
                Field('beach', 'integer', default=0, IS_INT_IN_RANGE=(0, 11)),
                Field('sights', 'integer', default=0, IS_INT_IN_RANGE=(0, 11)),
                Field('food', 'integer', default=0, IS_INT_IN_RANGE=(0, 11)),
                Field('night', 'integer', default=0, IS_INT_IN_RANGE=(0, 11)),
                Field('shop', 'integer', default=0, IS_INT_IN_RANGE=(0, 11)),
                Field('num_like', 'integer', default=0),
                Field('num_dislike', 'integer', default=0),
                Field('num_travel', 'integer', default=0),
                Field('time'),
                )

db.define_table('likes',
                Field('is_like', 'boolean'),
                Field('post', 'reference posts'),
                Field('name', default=""),
                Field('email', default=get_user_email()),
                )

db.define_table('travels',
                Field('has_traveled', 'boolean'),
                Field('post', 'reference posts'),
                Field('name', default=""),
                Field('email', default=get_user_email()),
                )

# db.define_table('user',
#                 Field('user_email', default=get_user_email(), reference=auth, writable=False),
#                 Field('user_name', 'string'),
#                 Field('biography', 'string'),
#                 Field('thumbnail', 'text'),
#                 )


# db.define_table(
#     'comment',
#     Field('post', 'reference posts'),
#     Field('username', 'reference user'),
#     Field('content', 'string'),
# )


db.define_table(
    'review',
    Field('author', 'string'),
    Field('email', default=auth.current_user.get('email') if auth.current_user else "Unknown"),
    Field('rating', 'integer', default=0, requires=IS_INT_IN_RANGE(0, 11)),
    Field('description', 'text'),
)

db.review.id.readable = db.review.id.writable = False
db.review.email.writable = db.review.email.readable = False
# db.review.user_email.readable = db.review.user_email.writable = False

db.commit()
