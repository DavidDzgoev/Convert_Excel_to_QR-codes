import qrcode
import pandas as pd
import json

data = pd.read_excel('input_data.xlsx')
rows_as_json = json.loads(data.to_json(orient="records"))

for i, row in enumerate(rows_as_json):
    qr_input = row
    filename = f"qr_codes/{i}.png"
    img = qrcode.make(qr_input)
    img.save(filename)
