from fastapi import FastAPI

app = FastAPI()

vendas = {
    1 : {'Item': 'Coca Lata', 'Valor': 4, 'Quantidade': 5},
    2 : {'Item': 'Coca 3L', 'Valor': 12, 'Quantidade': 5},
    3 : {'Item': 'Coca 600ml', 'Valor': 7, 'Quantidade': 5},
    4 : {'Item': 'Coca Caçulinha', 'Valor': 2, 'Quantidade': 5}
}

@app.get('/')
def home():
    return {'Vendas': len(vendas)}

@app.get('/vendas/{id_venda}')
def capturar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {'Erro': 'ID Venda não existe'}