# NEXUS NETRA

**Network Tools & Response Assistant**

O **NETRA** é uma ferramenta de diagnóstico e monitoramento de dispositivos de rede desenvolvida como parte do ecossistema **NEXUS Tools**.

O objetivo do NETRA é auxiliar na identificação de problemas de conectividade e infraestrutura de rede através da execução de testes objetivos e da análise dos resultados obtidos.

A ferramenta foi projetada inicialmente para utilização em ambientes de rede controlados, começando pelo monitoramento de roteadores e access points, mas com arquitetura preparada para futuramente trabalhar com servidores, switches, DVRs e outros dispositivos.

## Objetivo

O NETRA não deve simplesmente informar que um dispositivo está "offline".

A ferramenta deve reunir informações suficientes para responder:

> **Qual é o possível problema e quais evidências sustentam essa hipótese?**

Para isso, o sistema executa diferentes testes de conectividade e apresenta seus resultados de forma organizada.

## Principais funcionalidades

A primeira versão deverá possuir:

* Cadastro de dispositivos através de arquivo JSON
* Dashboard web de monitoramento
* Visualização do status dos dispositivos
* Página individual para cada dispositivo
* Teste de conectividade através de ICMP/Ping
* Medição de latência
* Cálculo de perda de pacotes
* Teste de gateway
* Teste de conectividade entre dispositivos
* Teste de portas TCP previamente configuradas
* Diagnóstico baseado em regras
* Identificação de possíveis causas
* Registro das evidências encontradas
* Geração de relatórios técnicos
* Salvamento dos resultados dos diagnósticos
* Registro de data e hora dos testes

## Arquitetura

O projeto será dividido em módulos para facilitar manutenção, testes e futuras expansões.

```text
netra/
│
├── app.py
│
├── config/
│   └── devices.json
│
├── core/
│   ├── config.py
│   ├── models.py
│   └── utils.py
│
├── network/
│   ├── ping.py
│   ├── gateway.py
│   ├── ports.py
│   └── connectivity.py
│
├── diagnostics/
│   └── engine.py
│
├── reports/
│   └── generator.py
│
├── web/
│   ├── routes.py
│   │
│   ├── templates/
│   │
│   └── static/
│       ├── css/
│       └── js/
│
├── data/
│   └── reports/
│
├── tests/
│
├── requirements.txt
└── README.md
```

A estrutura poderá ser modificada durante o desenvolvimento conforme novas necessidades surgirem.

## Cadastro dos dispositivos

Os dispositivos não serão armazenados diretamente no código-fonte.

O NETRA utilizará um arquivo JSON externo para armazenar as informações dos equipamentos.

Cada dispositivo poderá possuir informações como:

* Nome
* Tipo
* Endereço IP
* MAC Address
* Localização
* Gateway
* Descrição
* Status
* Data/hora do último teste

Exemplo:

```json
{
    "dispositivos": [
        {
            "nome": "AP Coordenação",
            "tipo": "access_point",
            "ip": "172.16.0.10",
            "mac": "XX:XX:XX:XX:XX:XX",
            "local": "Coordenação",
            "gateway": "172.16.0.1"
        }
    ]
}
```

O arquivo deverá ser carregado automaticamente pela aplicação.

Alterações nos dispositivos deverão ser realizadas no arquivo de configuração, sem necessidade de modificar o código da aplicação.

## Diagnóstico

O NETRA utilizará regras para interpretar os resultados dos testes.

Exemplo:

```text
Dispositivo responde ao Ping
        │
        └──► Dispositivo provavelmente acessível


Dispositivo não responde
Gateway responde
        │
        └──► Investigar dispositivo,
             cabo, porta do switch
             ou configuração


Dispositivo responde ao Ping
Porta específica não responde
        │
        └──► Serviço pode estar
             indisponível ou bloqueado
```

O sistema não deverá apresentar uma hipótese como certeza quando os testes não forem suficientes para comprovar a causa.

Os resultados deverão ser apresentados como **possíveis causas**, acompanhados das evidências encontradas.

## Relatórios

Após a execução de um diagnóstico, o NETRA poderá gerar um relatório técnico contendo:

* Data e hora
* Dispositivo analisado
* IP
* MAC Address
* Localização
* Status
* Testes executados
* Resultados
* Latências
* Perda de pacotes
* Portas testadas
* Conectividade com outros dispositivos
* Possíveis causas
* Evidências
* Observações

Inicialmente, os relatórios poderão ser armazenados em formatos como TXT e JSON.

## Interface

A aplicação possuirá uma interface web acessível através da rede local.

O dashboard deverá apresentar os dispositivos cadastrados em cards, mostrando informações essenciais e seu estado atual.

Estados previstos:

```text
🟢 ONLINE
🟡 PROBLEMA / TESTE
⚫ OFFLINE
```

A interface deverá priorizar simplicidade, clareza e facilidade de interpretação.

## Segurança

O NETRA será desenvolvido para utilização em ambientes controlados.

A V1 não deverá:

* Executar scans indiscriminados da rede
* Realizar testes agressivos
* Executar ações destrutivas
* Alterar configurações de equipamentos
* Armazenar credenciais de dispositivos
* Executar ações administrativas automaticamente

Os testes deverão possuir finalidade exclusivamente diagnóstica.

## Tecnologias

A primeira versão utilizará:

**Backend**

* Python
* Flask ou FastAPI

**Frontend**

* HTML
* CSS
* JavaScript

**Dados**

* JSON

Futuramente, o projeto poderá utilizar:

* SQLite
* Banco de dados
* Gráficos
* APIs
* Sistema de autenticação
* Monitoramento contínuo

## Roadmap

### V1 — Diagnóstico

* [x] Cadastro via JSON
* [ ] Dashboard
* [ ] Status dos dispositivos
* [ ] Página individual
* [x] Ping
* [x] Latência
* [x] Perda de pacotes
* [ ] Teste de gateway
* [ ] Teste entre dispositivos
* [ ] Teste de portas
* [ ] Motor de diagnóstico
* [ ] Possíveis causas
* [ ] Relatórios
* [x] Salvamento dos resultados

### V2 — Histórico

* [ ] SQLite
* [ ] Histórico completo
* [ ] Gráficos de latência
* [ ] Gráficos de disponibilidade
* [ ] Comparação entre diagnósticos
* [ ] Exportação PDF
* [ ] Dashboard avançado

### V3 — Descoberta e monitoramento

* [ ] Descoberta de dispositivos
* [ ] ARP
* [ ] SNMP
* [ ] Identificação automática
* [ ] Monitoramento contínuo
* [ ] Alertas

### V4 — Acesso

* [ ] Autenticação
* [ ] Acesso remoto seguro
* [ ] Notificações
* [ ] Aplicativo mobile

### V5+ — Automação

* [ ] Automação de diagnóstico
* [ ] Análise de padrões
* [ ] Integração com infraestrutura
* [ ] Recomendações avançadas
* [ ] Monitoramento centralizado
* [ ] Múltiplos agentes

## Filosofia

O NETRA não foi projetado para ser apenas um "ping com interface".

Cada diagnóstico deve tentar responder:

```text
O que foi testado?

Qual foi o resultado?

O que esse resultado significa?

Quais hipóteses podem ser levantadas?
```

O objetivo é transformar informações técnicas da rede em evidências que possam auxiliar na investigação de problemas reais de infraestrutura.

---

**NEXUS Tools**

NETRA — Network Diagnostic & Monitoring Tool
