from .models import Nota_Fiscal

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def progresso_obra(contratos):
    soma_empenhos=0
    soma_notas=0  
    previsto=int(contratos.obra.valor_previsto)  
    ids=[]
    for i in contratos.nota_empenho.filter(ativo=True):
        soma_empenhos+=int(i.valor)
        notas_fiscais=Nota_Fiscal.objects.filter(empenho=i)
        for n in notas_fiscais:
            soma_notas+=int(n.valor)
        
    percent=previsto/100.00
    return soma_notas, percent, soma_empenhos, previsto