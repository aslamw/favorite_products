import requests

def get_product_id(id):
    
    product = requests.get(f'http://challenge-api.luizalabs.com/api/product/{id}/')
    
    if product.status_code != 200:
        return "error"
    
    return product.text


if __name__ == '__main__':
    
    with open("produto.txt", 'w') as arq:
        arq.write(get_product_id(1))
    
    