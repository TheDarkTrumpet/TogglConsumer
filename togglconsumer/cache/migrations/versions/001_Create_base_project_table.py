from migrate.tests.fixture.models import meta
from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    projects = Table(
        'project', meta,
        Column('id', Integer, primary_key=True, autoincrement=true),
        Column('workspace_id', Integer),
        Column('name', String(255)),
        Column('billable', Boolean),
        Column('is_private', Boolean),
        Column('active', Boolean),
        Column('actual_hours', Integer)
    )


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pass
