from django.shortcuts import render
from .forms import InputUnico
from django.http import HttpResponse, FileResponse
from io import BytesIO

import openai
from deep_translator import GoogleTranslator

# Create your views here.
def home_screen_view(request):
    context = {}
    context['form_individual'] = InputUnico()
    return render(request, "site_app/home.html", context)

def view_test(request):
    resposta_formulario = []
    try:
      #Colocar chave api aqui
        if request.method == 'POST':
            print(resposta_formulario)
            resposta_formulario.append(request.POST.get('nome_aluno'))
            resposta_formulario.append(request.POST.get('nome_disciplina'))
            resposta_formulario.append(request.POST.get('como_avaliar'))
            resposta_formulario.append(request.POST.get('nota_max'))
            resposta_formulario.append(request.POST.get('nota_min'))
            resposta_formulario.append(request.POST.get('trabalho'))

            tradutor = GoogleTranslator(source="pt", target="en")
            traducao = tradutor.translate("Imagine que você é um professor avaliador da disciplina: " +  resposta_formulario[1] + " e siga essa regra: " +  resposta_formulario[2] + ". A maior nota que um aluno pode receber é: " +  resposta_formulario[3] + " e menor nota é: " +  resposta_formulario[4] + ". Dê a nota que o aluno tirou e um feedback do porque da nota. Responda tudo em PT-BR.")

            mensagens = [{"role":"system", "content": traducao}]

            conteudo_final = "Avalie este trabalho: " + request.POST.get('trabalho')

            mensagens.append({"role":"user", "content":conteudo_final})

            chatGPT = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            # response_format={ "type": "json_object" },
            #gpt-3.5-turbo
            messages=mensagens
            )

            buffer_memoria = BytesIO()
            resposta_gpt = str(chatGPT.choices[0].message.content)
            buffer_memoria.write(resposta_gpt.encode('utf-8'))
            buffer_memoria.seek(0)
            response = FileResponse(buffer_memoria)
            response['Content-Type'] = 'application/octet-stream'
            nome_arquivo = resposta_formulario[0] + ".txt"
            response['Content-Disposition'] = 'attachment; filename=' + nome_arquivo

            return response
    except Exception as e:
        return HttpResponse(f"erro no script: {e}")
    
    # return render(request, "site_app/home.html")
