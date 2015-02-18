import os
import urlparse
from peewee import *
from peewee import create_model_tables


if 'DATABASE_URL' in os.environ:
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ['DATABASE_URL'])

    db = PostgresqlDatabase(
        url.path[1:],
        user=url.username,
        password=url.password,
        host=url.host,
        port=url.port
    )

else:
    db = PostgresqlDatabase('govt10')

class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    email = CharField(primary_key=True)

    # The randomly assigned send time
    send_time = DateTimeField()

    # The actual send time
    sent_time_actual = DateTimeField()

    # The reply time extracted from the reply email
    reply_time = DateTimeField()

    question = TextField()

create_model_tables([Person], fail_silently=True)
