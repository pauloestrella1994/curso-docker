import redis, json
from time import sleep
from random import randint


if __name__=='__main__':
    r = redis.Redis(host='queue', port=6379, db=0)
    print('Aguradando mensagens...')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        # Simulando o envio do email
        print('Mandando mensagem: ', mensagem['assunto'])
        sleep(randint(15, 45))
        print('Mensagem', mensagem['assunto'], 'enviada')