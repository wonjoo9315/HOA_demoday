"""empty message



Revision ID: 3dce9f2e2c56

Revises: 242df53cef59

Create Date: 2014-09-27 19:51:35.145000



"""



# revision identifiers, used by Alembic.

revision = '3dce9f2e2c56'

down_revision = '242df53cef59'



from alembic import op

import sqlalchemy as sa





def upgrade():

    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('view_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=50), nullable=True),
    sa.Column('humans_id', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['humans_id'], ['humans.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('humans_id', 'ip', name='_view_humans')
    )
    op.create_table('like_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=50), nullable=True),
    sa.Column('humans_id', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['humans_id'], ['humans.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('humans_id', 'ip', name='_like_humans')
    )
    op.add_column(u'humans', sa.Column('like_count', sa.Integer(), nullable=True))
    op.add_column(u'humans', sa.Column('view_count', sa.Integer(), nullable=True))
    ### end Alembic commands ###





def downgrade():

    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'humans', 'view_count')
    op.drop_column(u'humans', 'like_count')
    op.drop_table('like_record')
    op.drop_table('view_record')
    ### end Alembic commands ###
