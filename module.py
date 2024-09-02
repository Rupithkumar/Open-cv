import requests
from tabulate import tabulate
import json


url = "https://www.amazon.in/Daikin-Inverter-Display-Technology-MTKL50U/dp/B0BK1KS6ZD/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.58c90a12-100b-4a2f-8e15-7c06f1abe2be&dib=eyJ2IjoiMSJ9.LpujZ4uISPUK8sa_6yNGVTLp2_seTR9samDUOPD7O27bln-x88VwJsZILZK3UcHDFMzd_8tkDXScm_B-M1ld3WXSWEkR9NQjpSI1oEBqxy7UQAcC1oxMngfvWyJevSVxfQryOFdBe0KwFO94aD0GdsEup9CYNxEbp8T-Zoz6HMt9ekRN9bDwC0X96uNxLOUqfh0Jlonye0_0yr4125Cn_35j_VPBw9OK7VwCwm3L7PA3bbgj44iNRiol5uYuvZjUZIIpr4YyyT5EfJ-k2BbFFyhv685hz0PpOtJNddt7K5c.V392LipuYTBJHiLePgoCIHUW3kzKNXKu17FO4yYGtdk&dib_tag=se&pd_rd_r=c3e106c2-96c5-4165-9980-87731390c25f&pd_rd_w=5KXbu&pd_rd_wg=EEe2u&pf_rd_p=58c90a12-100b-4a2f-8e15-7c06f1abe2be&pf_rd_r=FNBNG98ZXR9N27F74BYV&qid=1718002566&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-1"
response = requests.get(url)


try:
    response_json = json.loads(response.text)
except ValueError:
    print("Response content is not in JSON format.")
    response_json = []


table_data = []
for item in response_json:
    table_data.append([
        item.get("id", ""),
        item.get("title", ""),
        item.get("price", ""),
        item.get("description", ""),
        item.get("category", ""),
        item.get("image", ""),
        item.get("rating", "")
    ])


headers = ["Post ID", "Title", "Price", "Description", "Category", "Image URL", "Rating"]


print(tabulate(table_data, headers, tablefmt="grid"))
