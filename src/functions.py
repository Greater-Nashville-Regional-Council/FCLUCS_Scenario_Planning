import sqlite3 as sq

import pandas as pd

from src.paths import CENSUS_DB
from src.paths import WP_DB


def read_census_table(table_name):
	"""Read a table from the Census Bureau SQLite database.

	Parameters
	----------
	table_name : str
		Name of the table to read.

	Returns
	-------
	pandas.DataFrame
		Census table as a DataFrame.
	"""
	query = f"SELECT * FROM [{table_name}]"

	with sq.connect(CENSUS_DB) as conn:
		df = pd.read_sql(query, conn)

	return df

def read_wp23_table(table_name):
	"""Read a table from the Woods and Poole 2023V SQLite database.

	Parameters
	----------
	table_name : str
		Name of the table to read.

	Returns
	-------
	pandas.DataFrame
		Woods and Poole table as a DataFrame.
	"""
	query = f"SELECT * FROM [{table_name}]"

	with sq.connect(WP_DB) as conn:
		df = pd.read_sql(query, conn)

	return df