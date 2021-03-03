# Import create_engine
from sqlalchemy import create_engine, MetaData, Table

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')
engine.connect()

# Print table names
print(engine.table_names())


# Create a metadata object: metadata
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
txt = repr(census)
print(txt)
# for i in txt.split():
#     print(i)
