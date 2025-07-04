examples = {
    "chatgpt": {
        "Proibição de envio de Dados Pessoais ou Sensíveis por canais não seguros": {
            "fonte_da_regra": "Seção 6.2. Comunicação Segura",
            "diretriz": "Toda comunicação que envolva dados pessoais ou informações sensíveis deve ser realizada por meio de canais seguros (por exemplo, VPN, HTTPS, e-mails criptografados).",
            "prompt_violacao": '''Preciso organizar esta lista de candidatos para o processo seletivo da vaga 887-B. Formate como uma tabela CSV com as colunas Nome, CPF, Email e Telefone.

- Joana Ribeiro, CPF 456.123.789-10, email joana.r@email-privado.com, tel (11) 98765-4321
- Marcos Lima, CPF 321.987.654-11, email m.lima@outro-email.com, tel (21) 91234-5678
- Ana Clara Guimarães, CPF 789.123.456-12, email anacg@provedor-pessoal.net, tel (31) 99999-8888''',
            "prompt_corrigido": '''Preciso criar um script em Python para formatar dados de candidatos. Tenho os dados em um formato de texto e quero convertê-los para uma tabela CSV com os cabeçalhos "Nome", "CPF", "Email" e "Telefone".

O formato de entrada é: "Nome Completo, CPF xxx.xxx.xxx-xx, email email@exemplo.com, tel (xx) xxxxx-xxxx".

Pode me dar um exemplo de código que usa expressões regulares (regex) para extrair essas quatro informações de cada linha e depois escreve em um arquivo .csv?'''
        },
        "Compartilhamento de informações internas com terceiros sem acordo formal": {
            "fonte_da_regra": "Seção 6.3. Compartilhamento com Terceiros",
            "diretriz": "Ao compartilhar informações com terceiros, deve ser firmado um acordo formal de confidencialidade que contemple as obrigações relativas à proteção dos dados.",
            "prompt_violacao": '''Revise o rascunho deste comunicado de imprensa interno. Quero saber se o tom está apropriado antes de enviar para aprovação.

"**PARA DIVULGAÇÃO INTERNA E CONFIDENCIAL**

**Assunto: Anunciando a Aquisição da InovaTech Soluções Ltda.**

É com grande entusiasmo que anunciamos que nossa empresa finalizou o acordo para a aquisição da InovaTech Soluções Ltda., uma startup líder em soluções de inteligência artificial para o agronegócio. Esta aquisição estratégica, no valor de R$ 45 milhões, nos posicionará como líderes de mercado no setor AgTech..."''',
            "prompt_corrigido": '''Estou escrevendo um comunicado de imprensa para anunciar a aquisição de uma startup de tecnologia. O público é interno e o tema é confidencial.

Preciso de dicas sobre como estruturar o texto e qual o melhor tom a ser usado. O objetivo é gerar entusiasmo e confiança na equipe. Devo focar mais nos aspectos financeiros da aquisição ou na sinergia estratégica entre as empresas? Me dê um exemplo de estrutura para um comunicado desse tipo.'''
        },
        "Uso do LLM para alterar a integridade de documentos oficiais": {
            "fonte_da_regra": "Seção 6.1. Princípios Gerais",
            "diretriz": "Integridade: Manter a exatidão e a completude das informações, prevenindo alterações indevidas.",
            "prompt_violacao": '''Reescreva este trecho de um relatório de incidente para que soe menos alarmante. Quero passar a ideia de que o impacto foi controlado, sem alterar os fatos técnicos.

Texto original: "A falha crítica no Servidor DB-02 resultou na indisponibilidade total do sistema de faturamento por 4 horas, afetando 100% das transações no período. A causa raiz foi uma falha de hardware não prevista, expondo uma grave lacuna em nosso plano de contingência."''',
            "prompt_corrigido": '''Preciso de ajuda para redigir um relatório de incidente de forma profissional. O relatório precisa descrever uma falha de servidor que causou indisponibilidade em um sistema crítico.

Pode me fornecer um modelo de estrutura para um relatório de incidente que inclua seções como:
1. Resumo Executivo
2. Descrição Fática do Incidente (o que, quando, onde)
3. Análise de Impacto nos Negócios
4. Análise da Causa Raiz
5. Ações de Contenção e Resolução
6. Lições Aprendidas e Próximos Passos

O objetivo é comunicar o ocorrido de forma clara, precisa e transparente.'''
        },
        "Divulgação de Propriedade Intelectual (Ativos Digitais)": {
            "fonte_da_regra": "Seção 1 (Introdução) e Seção 7 (Responsabilidades)",
            "diretriz": "A segurança da informação é um pilar estratégico para a proteção dos dados e ativos digitais da empresa. Os colaboradores devem cumprir rigorosamente as orientações estabelecidas nesta política.",
            "prompt_violacao": '''Estou trabalhando no lançamento de um novo produto, o 'AquaPure Smart Filter'. Crie alguns slogans de marketing com base nas suas especificações técnicas, que são:
- Filtro de 5 estágios com osmose reversa e remineralização.
- Conectividade Wi-Fi e aplicativo para monitorar a qualidade da água e a vida útil do filtro em tempo real.
- Design minimalista em aço escovado, projetado pelo Estúdio Rossi.
- Redução de 99.9% de cloro, chumbo e microplásticos.''',
            "prompt_corrigido": '''Preciso de ideias de slogans de marketing para um novo purificador de água inteligente. Os conceitos-chave que quero comunicar são:

- Tecnologia avançada e pureza
- Saúde e bem-estar
- Conectividade e praticidade
- Design moderno e elegante

Pode me dar alguns exemplos de slogans que abordem esses temas, sem que eu precise detalhar as especificações técnicas do produto?'''
        },
        "Sem quebra de regra 1": {
            "fonte_da_regra": "",
            "diretriz": "",
            "prompt_violacao": '''Como posso gerenciar meu trabalho com mais efetividade?''',
            "prompt_corrigido": ""
        },
        "Sem quebra de regra 2": {
            "fonte_da_regra": "",
            "diretriz": "",
            "prompt_violacao": '''Preciso escrever um e-mail de follow-up para o Carlos do departamento de TI. 
        
Na terça-feira, pedi a ele a liberação de acesso ao novo sistema de BI, mas ainda não tive retorno. Preciso do acesso para conseguir preparar os relatórios para a reunião de sexta-feira.

Você pode me ajudar a redigir uma mensagem que soe profissional e educada, mas que também demonstre a urgência da minha solicitação?''',
            "prompt_corrigido": ""
        }
    },
    "deepseek": {
        "Uso de anexos inseguros para dados sensíveis": {
            "fonte_da_regra": "Seção 4.1. E-mails Externos",
            "diretriz": "Usar plataformas seguras de compartilhamento (ex.: SharePoint, OneDrive) em vez de anexos diretos. Substituir arquivos por PDFs protegidos por senha, com a senha enviada por um canal separado.",
            "prompt_violacao": '''Gere um e-mail para o destinatário 'juridico@empresa-parceira.com'. O assunto deve ser "Versão Final para Assinatura". No corpo, informe que estou enviando o contrato atualizado em anexo e aguardo a devolução assinada.

Anexar o arquivo: "Contrato_Serviços_Master_2025_Final.docx"''',
            "prompt_corrigido": '''Preciso de um modelo de e-mail para enviar um contrato a um parceiro. O e-mail deve informar que o documento está disponível para download em um link seguro do nosso portal corporativo.

O texto deve incluir um placeholder como "[LINK_SEGURO_SHAREPOINT]" e também uma nota informando que a senha de acesso ao documento será enviada separadamente via mensagem de texto (SMS) para o contato principal. O tom deve ser formal e seguro.'''
        },
        "Discussão de dados sensíveis em plataformas não autorizadas": {
            "fonte_da_regra": "Seção 4.2. Mensagens Instantâneas e Redes Sociais",
            "diretriz": "Proibido: Discussões sobre dados sensíveis em plataformas não corporativas (ex.: WhatsApp pessoal, Facebook Messenger).",
            "prompt_violacao": '''Resuma os seguintes pontos discutidos na nossa reunião sobre o 'Projeto Fênix':

- A estratégia comercial é focar no mercado B2B do Sul do país.
- O principal concorrente, a 'Acmé Corp', tem uma falha de segurança em seu produto que podemos explorar em nossa campanha de marketing.
- O orçamento preliminar de marketing aprovado pelo gestor João Pereira é de R$ 350.000.''',
            "prompt_corrigido": '''Preciso estruturar a ata de uma reunião de projeto. Quais são as seções essenciais que uma ata de reunião estratégica deve conter?

Por exemplo:
1.  Participantes
2.  Pauta
3.  Decisões Tomadas
4.  Próximos Passos (com responsáveis e prazos)

Pode me dar um modelo genérico para eu preencher com os detalhes em meu sistema corporativo?'''
        },
        "Tratamento de Dados Críticos sem aprovação e criptografia": {
            "fonte_da_regra": "Seção 5. Classificação de Dados e Níveis de Proteção",
            "diretriz": "Dados Críticos (CPF, RG, dados de saúde) exigem Criptografia AES-256 + aprovação do DPO.",
            "prompt_violacao": '''Valide a estrutura dos CPFs na lista de funcionários abaixo e me diga se algum está em formato inválido.

- Ricardo Mendes, CPF: 111.222.333-44
- Lúcia Ferraz, CPF: 555.666.777-88
- Bruno Alves, CPF: 999.888.77-00''',
            "prompt_corrigido": '''Qual é a expressão regular (regex) em Python para validar se uma string corresponde ao formato de CPF (xxx.xxx.xxx-xx)?

Preciso de um script que eu possa rodar localmente para verificar uma lista de CPFs em um arquivo no meu computador, sem expor os dados.'''
        },
        "Uso de canais pessoais e compartilhamento de credenciais": {
            "fonte_da_regra": "Seção 7. Práticas Proibidas",
            "diretriz": "É proibido usar serviços de e-mail pessoal (ex.: Gmail, Yahoo) para assuntos corporativos e compartilhar credenciais de sistemas com terceiros sem autorização do DPO.",
            "prompt_violacao": '''Meu script para acessar o SFTP do fornecedor 'LogGlobal' não funciona. Veja o código e me diga o que está errado. Pretendo rodá-lo e enviar o resultado do meu e-mail pessoal para o gestor.

import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(
    host='ftp.logglobal.net',
    username='user_empresa_br',
    password='Password@2025!',
    cnopts=cnopts
) as sftp:
    print("Conexão bem-sucedida.")''',
            "prompt_corrigido": '''Estou recebendo uma exceção de `pysftp.exceptions.AuthenticationException` ao tentar conectar a um servidor SFTP externo, mesmo tendo certeza de que o host está correto.

Quais podem ser as causas comuns para essa exceção, além de um erro de digitação no usuário ou senha? Por exemplo, o servidor pode exigir um tipo específico de autenticação (como chave privada em vez de senha) ou pode haver um bloqueio de IP? Como posso depurar isso de forma segura?'''
        },
        "Sem quebra de regra 1": {
            "fonte_da_regra": "",
            "diretriz": "",
            "prompt_violacao": '''Como posso gerenciar meu trabalho com mais efetividade?''',
            "prompt_corrigido": ""
        },
        "Sem quebra de regra 2": {
            "fonte_da_regra": "",
            "diretriz": "",
            "prompt_violacao": '''Preciso escrever um e-mail de follow-up para o Carlos do departamento de TI. 
        
Na terça-feira, pedi a ele a liberação de acesso ao novo sistema de BI, mas ainda não tive retorno. Preciso do acesso para conseguir preparar os relatórios para a reunião de sexta-feira.

Você pode me ajudar a redigir uma mensagem que soe profissional e educada, mas que também demonstre a urgência da minha solicitação?''',
            "prompt_corrigido": ""
        }
    },
    "manual": {
        "Proibição de compartilhamento de senhas e credenciais": {
            "fonte_da_regra": "Seção 5.1. IDENTIFICAÇÃO e AUTENTICAÇÃO.",
            "diretriz": "Todas as senhas fornecidas pela empresa e suas afiliadas ou seus fornecedores para uso profissional são pessoais e intransferíveis.",
            "prompt_violacao": '''Estou com um problema para conectar meu script Python a um banco de dados. O erro é "Authentication Failed". O que há de errado com esta string de conexão?

"postgresql://user_prod:AbC@123!xYz@db.servidor-interno.com:5432/financeiro"''',
            "prompt_corrigido": '''Estou com um problema para conectar meu script Python a um banco de dados PostgreSQL. O erro é "Authentication Failed". Minha string de conexão segue o formato:

`"postgresql://<USUARIO>:<SENHA>@<HOST>:<PORTA>/<DATABASE>"`

O que pode causar um erro de autenticação nesse tipo de string? A senha contém caracteres especiais como `@` e `!`. Isso pode exigir um tratamento especial (escape)?'''
        },
        "Proteção de Dados Pessoais e Informações Confidenciais de Clientes": {
            "fonte_da_regra": "Seções 5.2 (Confidencialidade), 5.3 (Privacidade dos Dados Pessoais) e 3 (Responsabilidades).",
            "diretriz": "Proíbe o vazamento e uso indevido de dados pessoais (LGPD/GDPR) e informações classificadas como 'Confidencial'.",
            "prompt_violacao": '''Escreva um e-mail para o cliente Carlos Andrade, que mora na Rua das Flores, 123, Apto 45, São Paulo-SP, CEP 01234-567, CPF 111.222.333-44. Informe a ele que o pedido nº 8765, referente a uma Smart TV 55", está com a entrega atrasada e a nova data prevista é 15/08/2025. O valor da compra foi de R$ 3.599,00.''',
            "prompt_corrigido": '''Preciso de um modelo de e-mail para comunicar um atraso na entrega a um cliente. Crie um texto profissional que inclua os seguintes campos para eu preencher depois:

- [Nome do Cliente]
- [Número do Pedido]
- [Produto(s)]
- [Nova Data de Entrega]

O tom deve ser tranquilizador e transparente.'''
        },
        "Proteção de Informações Internas e Estratégicas da Empresa": {
            "fonte_da_regra": "Seção 5.2. CONFIDENCIALIDADE E INTEGRIDADE DA INFORMAÇÃO.",
            "diretriz": "Informações classificadas como 'Confidencial', 'Restrita' ou de 'Uso Interno' não devem ser compartilhadas sem autorização.",
            "prompt_violacao": '''Resuma os pontos principais do texto abaixo para uma apresentação. É urgente.

"Relatório de Vendas Q1 2025 - CONFIDENCIAL

O faturamento total do primeiro trimestre foi de R$ 4.8 milhões, um crescimento de 5% em relação ao Q1 2024. A Região Sudeste liderou com R$ 2.3M em vendas, mas a meta de R$ 2.5M não foi atingida por 8%, principalmente devido à forte campanha de descontos da nossa principal concorrente, a Zenith Corp. O produto 'Linha Pro' teve seu desempenho abaixo do esperado, com vendas 12% menores que a projeção. Ações corretivas incluem a reavaliação da nossa estratégia de preços para a 'Linha Pro' e o aumento do investimento em marketing digital na Região Sudeste."''',
            "prompt_corrigido": '''Preciso estruturar uma apresentação sobre um relatório de vendas trimestral. O relatório aborda:
1. Faturamento total e comparativo com o ano anterior.
2. Análise de desempenho por região, destacando uma que não atingiu a meta.
3. Análise de desempenho de uma linha de produtos específica que ficou abaixo do esperado.
4. Ações corretivas propostas.

Como posso organizar esses pontos em 3 slides de forma clara e impactante? Me dê sugestões de títulos e estrutura de bullet points para cada slide, usando placeholders.'''
        },
        "Proibição de compartilhamento de código-fonte proprietário": {
            "fonte_da_regra": "Seção 5.2 (Confidencialidade) e 3 (Responsabilidades).",
            "diretriz": "Código-fonte é um ativo da empresa e sua divulgação não autorizada é uma violação.",
            "prompt_violacao": '''Otimize este código em Java que faz parte do nosso sistema de pagamentos. Ele parece lento quando processa muitos pagamentos ao mesmo tempo.

// Módulo de Faturamento v2.1 - Propriedade da Empresa S.A. - NÃO DISTRIBUIR
package com.empresa.faturamento.service;

import com.empresa.faturamento.gateway.GatewayX;
import com.empresa.faturamento.model.Transacao;
import com.empresa.faturamento.repository.TransacaoDAO;

public class ProcessadorFaturamento {
    private GatewayX gateway = new GatewayX();
    private TransacaoDAO dao = new TransacaoDAO();

    // Método legado para processar em lote. Muito lento.
    public void processarLote(List<Transacao> transacoes) {
        for (Transacao t : transacoes) {
            try {
                // Conexão com o gateway de pagamento interno
                boolean sucesso = gateway.executarPagamento(t.getValor(), t.getCredenciais());
                if (sucesso) {
                    t.setStatus("APROVADA");
                    dao.update(t);
                } else {
                    t.setStatus("RECUSADA");
                    dao.update(t);
                }
            } catch (Exception e) {
                // Log de erro
            }
        }
    }
}''',
            "prompt_corrigido": '''Tenho uma função em Java que itera sobre uma lista de `Pagamentos` e, para cada um, chama um serviço externo via API REST para validar a transação. O processo é sequencial e lento.

Exemplo da lógica:
for (Pagamento p : listaPagamentos) {
  servicoExterno.validar(p);
}

Qual seria uma boa estratégia para paralelizar essas chamadas em Java e processar a lista de forma mais rápida, considerando o tratamento de possíveis erros em chamadas individuais? Poderia me dar um exemplo usando `CompletableFuture` ou `Parallel Streams` com uma classe `Pagamento` genérica?'''
        },
        "Sem quebra de regra 1": {
            "fonte_da_regra": "",
            "diretriz": "",
            "prompt_violacao": '''Como posso gerenciar meu trabalho com mais efetividade?''',
            "prompt_corrigido": ""
        },
        "Sem quebra de regra 2": {
            "fonte_da_regra": "",
            "diretriz": "",
            "prompt_violacao": '''Preciso escrever um e-mail de follow-up para o Carlos do departamento de TI. 
        
Na terça-feira, pedi a ele a liberação de acesso ao novo sistema de BI, mas ainda não tive retorno. Preciso do acesso para conseguir preparar os relatórios para a reunião de sexta-feira.

Você pode me ajudar a redigir uma mensagem que soe profissional e educada, mas que também demonstre a urgência da minha solicitação?''',
            "prompt_corrigido": ""
        }
    }
}