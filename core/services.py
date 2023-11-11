import camelot
import os
import sys
from django.conf import settings
import pandas as pd
import numpy as np
import glob
import pdfplumber

#https://www.youtube.com/watch?v=INXc_0pKrJg&ab_channel=RajeshJakhotia


def extract_data_content(filename, year):
    # tables = camelot.read_pdf(
    #     filename, flavor='stream', pages=str(2), row_tol=10, strip_text='\n')
    try:

        pdf = pdfplumber.open(filename)
        page = pdf.pages[0]
        tb = page.extract_table(table_settings={"horizontal_strategy": "lines",
                                                "vertical_strategy": "text",
                                                "snap_tolerance": 5, })
        df = pd.DataFrame(tb[1:], columns=tb[0])

        # print(df1.shape[1])
        print(df.head())
    except ValueError as e:
        print("An error occurred:", str(e))

    # num_columns = df1.shape[1]

    # new_column_names = ['TXN DATE', 'DESCRIPTION', 'VALUE DATE', 'MONEY OUT', 'MONEY IN', 'LEDGER BALANCE']

    # df1.columns = new_column_names[:num_columns]

    # df1.to_csv(os.path.join(settings.MEDIA_ROOT, str(year)+".csv"))

    # for col in table_content.columns:
    #     print(col)
