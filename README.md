# NETRA

**Network Tools & Response Assistant**

O **NETRA** é uma ferramenta de diagnóstico de conectividade de rede desenvolvida em Python. O projeto começou como uma aplicação de terminal para testar dispositivos cadastrados e analisar respostas ICMP/Ping.

O objetivo é evoluir de simples verificações de disponibilidade para diagnósticos que apresentem resultados, evidências e possíveis causas de problemas de infraestrutura.

## Estado atual — V1.0

Atualmente, o NETRA possui:

- Cadastro de dispositivos por arquivo JSON.
- Menu de terminal com listagem dinâmica dos dispositivos cadastrados.
- Consulta das informações de um dispositivo selecionado.
- Verificação de conectividade por ICMP/Ping.
- Exibição da latência informada pelo comando Ping.
- Exibição das estatísticas de pacotes quando disponíveis.
- Teste prolongado de Ping com duração definida pelo usuário.
- Análise das respostas registradas durante o teste prolongado.
- Salvamento local dos outputs utilizados na análise.
- Backup do output anterior do teste de conectividade.

O projeto ainda está em desenvolvimento. A interpretação de perda parcial de pacotes, a padronização dos resultados e o tratamento de algumas entradas e situações excepcionais estão em processo de correção.

## Requisitos

- Windows.
- Python 3 instalado e disponível no PATH.
- Acesso ao terminal.
- Permissão para executar o comando `ping` do Windows.

A implementação atual utiliza recursos específicos do Windows, como `ping -n`, `ping /t` e `taskkill`. Portanto, ainda não é compatível com Linux ou macOS.

## Como executar

1. Clone o repositório:

   ```powershell
   git clone https://github.com/Matheus-Silveiraa/NEXUS-NETRA.git
   cd NEXUS-NETRA
   ```

2. Crie o arquivo local de configuração copiando o exemplo:

   ```powershell
   copy config\devices_exemple.json config\devices.json
   ```

3. Edite `config/devices.json` e cadastre os dispositivos que deseja testar. Utilize endereços IP da sua própria rede e tenha autorização para realizar os testes.

4. Execute a aplicação a partir da pasta raiz do projeto:

   ```powershell
   python main.py
   ```

O arquivo `config/devices.json` é local e está incluído no `.gitignore`. Não publique configurações que contenham endereços, nomes, MAC addresses ou outras informações da sua infraestrutura.

## Cadastro de dispositivos

O cadastro é feito no arquivo `config/devices.json`, dentro da chave `dispositivos`.

O formato atual exige os campos com esta grafia:

- `ID`: identificador numérico utilizado pelo menu.
- `Nome`: nome de exibição do dispositivo.
- `Tipo`: tipo do equipamento.
- `IP`: endereço IPv4 utilizado nos testes.
- `MAC`: endereço MAC informativo.
- `Local`: localização ou identificação do ambiente.

Exemplo fictício:

```json
{
    "dispositivos": [
        {
            "ID": 1,
            "Nome": "Servidor de exemplo",
            "Tipo": "servidor",
            "IP": "192.0.2.10",
            "MAC": "02:00:00:00:00:10",
            "Local": "Laboratório de testes"
        },
        {
            "ID": 2,
            "Nome": "Access Point de exemplo",
            "Tipo": "access_point",
            "IP": "198.51.100.20",
            "MAC": "02:00:00:00:00:20",
            "Local": "Sala de testes"
        }
    ]
}
```

Os endereços IP do exemplo pertencem a faixas reservadas para documentação e não representam equipamentos reais. Substitua-os por endereços válidos da rede autorizada em que o NETRA será utilizado.

O campo `Gateway` ainda não faz parte do formato utilizado pelo código atual. O teste de gateway está planejado para uma versão futura.

## Arquivos gerados

Durante a execução, o NETRA utiliza arquivos locais para armazenar as saídas dos comandos:

- `network/output.txt`: saída do teste de conectividade executado por `check_host`.
- `network/ping_test_output.txt`: saída do teste prolongado de Ping.
- `backups/`: cópias anteriores de `network/output.txt`.

Esses arquivos podem conter informações da rede utilizada nos testes e, por isso, são ignorados pelo Git.

## Estrutura atual

```text
NEXUS-NETRA/
├── config/
│   └── devices_exemple.json
├── core/
│   └── config.py
├── network/
│   └── ping.py
├── main.py
├── .gitignore
└── README.md
```

Arquivos de configuração e outputs locais são criados durante a utilização e não são versionados. A estrutura poderá mudar conforme novos módulos forem implementados.

## Roadmap

### Próximas correções

- [ ] Diferenciar host indisponível de perda parcial de pacotes.
- [ ] Reduzir a dependência do idioma da saída do Windows.
- [ ] Fazer `check_host` retornar um resultado estruturado.
- [ ] Corrigir a contagem de respostas e a leitura de latências no `ping_test`.
- [ ] Validar a duração informada pelo usuário.
- [ ] Garantir o encerramento do processo de Ping em caso de interrupção.
- [ ] Tratar entradas inválidas no menu.

### Funcionalidades planejadas

- [ ] Menu de seleção de testes.
- [ ] Teste de gateway.
- [ ] Teste de conectividade entre dispositivos.
- [ ] Teste de portas TCP configuradas.
- [ ] Motor de diagnóstico baseado em regras.
- [ ] Identificação de possíveis causas e registro de evidências.
- [ ] Geração de relatórios técnicos.
- [ ] Histórico de resultados com SQLite.
- [ ] Dashboard web e monitoramento contínuo.

## Limitações conhecidas

- A versão atual funciona somente no Windows.
- Os testes são direcionados a dispositivos cadastrados por endereço IP.
- A interpretação de algumas mensagens do Ping ainda depende do idioma da saída do Windows.
- O diagnóstico ainda não identifica automaticamente a causa de uma falha; essa capacidade faz parte do desenvolvimento futuro.

## Filosofia

O NETRA não foi projetado para ser apenas um programa que informa se um endereço responde ao Ping.

Cada diagnóstico deverá ajudar a responder:

```text
O que foi testado?
Qual foi o resultado?
O que esse resultado significa?
Quais hipóteses são sustentadas pelas evidências?
```

O objetivo é transformar resultados técnicos de conectividade em informações úteis para investigar problemas reais de infraestrutura de rede.
