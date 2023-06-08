import requests

def get_product_id(id):
    
    product = requests.get(f'http://challenge-api.luizalabs.com/api/product/{id}/')
    
    if product.status_code == 200:
        product_data = product.json()
        
        return product_data
        
    else: return False
    
def get_page_product(page):
    
    product_page = requests.get(f'http://challenge-api.luizalabs.com/api/product/{page}/')
    
    
    if product_page.status_code == 200:
        product_data = product_page.json()
        
        return product_data
        
    else: return False
    
def validation_id(id):
    product = requests.get(f'http://challenge-api.luizalabs.com/api/product/{id}/')
    
    if product.status_code == 200:
        return True
    
    return False

if __name__ == '__main__':
    
    print(get_page_product(1))
    
    