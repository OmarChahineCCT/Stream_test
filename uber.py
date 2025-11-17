import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in NY")

DATA_URL = ('https://s3-us-west-2.amazonaws.com streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DATE_COLUMN="date/time"
def load_data(nrows):
	data=pd.read_csv(DATA_URL,nrows=nrows)
	lowercase=lambda x:str(x).lower()
	data.rename(lowecase, axis="columns", inplace=True)
	data[DATE_COLUMN]=pd.to_datetime(data[DATECOLUMN])
	return data

data_load_state=st.text("Loading Data ...")
data=load_data(10000)
data_load_state=st.tect("Loading Data ... Done!")