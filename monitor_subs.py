import subprocess
import time

def obter_subdominios(site):
    processo = subprocess.Popen(['subfinder', '-all', '-silent', '-d', site], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, _ = processo.communicate()
    subdominios = output.splitlines()
    return subdominios

def verificar_novos_subdominios(site, subdominios_anteriores):
    subdominios_atuais = obter_subdominios(site)
    novos_subdominios = [subdominio for subdominio in subdominios_atuais if subdominio not in subdominios_anteriores]
    return novos_subdominios

def main():
    site = 'example.com'  # Substitua pelo site que você deseja monitorar
    arquivo_subdominios = 'subdominios.txt'

    # Verificar se o arquivo de subdomínios existe
    try:
        with open(arquivo_subdominios, 'r') as file:
            subdominios_anteriores = file.read().splitlines()
    except FileNotFoundError:
        subdominios_anteriores = []

    # Verificar novos subdomínios uma vez por dia
    while True:
        novos_subdominios = verificar_novos_subdominios(site, subdominios_anteriores)
        if novos_subdominios:
            print('Novos subdomínios encontrados:')
            for subdominio in novos_subdominios:
                print(subdominio)
            with open(arquivo_subdominios, 'a') as file:
                for subdominio in novos_subdominios:
                    file.write(subdominio + '\n')
        else:
            print('Nenhum novo subdomínio encontrado.')
        time.sleep(86400)  # Espera 24 horas (86400 segundos) antes de verificar novamente

if __name__ == "__main__":
    main()
