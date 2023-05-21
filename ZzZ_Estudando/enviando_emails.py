import win32com.client as win32
import pathlib
from string import Template

outlook = win32.Dispatch('outlook.application')

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'texto_email.html'

with open(CAMINHO_HTML, 'r', encoding='utf8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Helena')

mail = outlook.CreateItem(0)
# Insira o endereço de email do destinatário
mail.To = 'mdayvson@outlook.com'
mail.Subject = 'Assunto do email'
mail.HTMLBody = texto_email

attachment = str(CAMINHO_HTML)  # Converte o caminho para string
mail.Attachments.Add(attachment)

mail.Send()
