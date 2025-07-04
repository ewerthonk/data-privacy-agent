# Política de Segurança da Informação e Proteção da Privacidade em Comunicações Externas

## 1. Objetivo
Garantir a proteção de dados pessoais e corporativos durante comunicações com partes externas (clientes, fornecedores, parceiros), alinhando-se à LGPD, GDPR, Marco Civil da Internet e normas ISO 27001/27002/27701. **Foco principal:** regulamentar práticas seguras para colaboradores e terceiros em interações externas.

## 2. Âmbito de Aplicação
Aplica-se a:
- Comunicações via e-mail, mensagens instantâneas, redes sociais, videoconferências e transferência de arquivos.
- Dispositivos corporativos e pessoais utilizados para atividades relacionadas à empresa (*BYOD*).
- Prestadores de serviços que acessam ou processam dados da organização.

## 3. Princípios para Comunicação Externa
1. **Necessidade:** Compartilhar apenas dados estritamente essenciais para a finalidade acordada.
2. **Verificação de Identidade:** Confirmar a autenticidade do destinatário antes de enviar dados sensíveis.
3. **Canais Autorizados:** Utilizar exclusivamente plataformas aprovadas pela TI (ex.: Microsoft 365, Zoom com criptografia).
4. **Rastreabilidade:** Manter logs de comunicações envolvendo dados confidenciais.

## 4. Protocolos Obrigatórios para Colaboradores

### 4.1. E-mails Externos
- **Criptografia:** Usar criptografia TLS para dados pessoais (ex.: CPF, endereço) ou sigilosos (ex.: contratos).
- **Assunto:** Evitar termos como "Confidencial" ou "Urgente" que possam atrair ataques de phishing.
- **Anexos:** 
  - Substituir arquivos não editáveis por PDFs protegidos por senha (senha enviada por canal separado).
  - Usar plataformas seguras de compartilhamento (ex.: SharePoint, OneDrive) em vez de anexos diretos.

### 4.2. Mensagens Instantâneas e Redes Sociais
- **Proibido:** Discussões sobre dados sensíveis em plataformas não corporativas (ex.: WhatsApp pessoal, Facebook Messenger).
- **Permitido:** Apenas ferramentas aprovadas com criptografia de ponta a ponta (ex.: Microsoft Teams, Slack Enterprise).

### 4.3. Videoconferências
- **Controle de Acesso:** Habilitar salas virtuais com senha e lista de participantes pré-aprovada.
- **Gravações:** Armazenar apenas em ambientes seguros da empresa, nunca em dispositivos locais.

### 4.4. Transferência de Dados para Terceiros
- **Acordo Prévio:** Assinar cláusula de proteção de dados (DPA) antes do compartilhamento.
- **Ferramentas:** Utilizar SFTP ou serviços com MFA (ex.: Box, Citrix ShareFile).

## 5. Classificação de Dados e Níveis de Proteção
| **Categoria**         | **Exemplos**                          | **Medidas Obrigatórias**                              |
|------------------------|---------------------------------------|-------------------------------------------------------|
| **Dados Críticos**     | CPF, RG, dados de saúde               | Criptografia AES-256 + aprovação do DPO               |
| **Dados Confidenciais**| Contratos, estratégias comerciais     | Criptografia em trânsito e repouso + logs de acesso   |
| **Dados Internos**     | Manuais, políticas                    | Restrição a domínios corporativos                     |

## 6. Responsabilidades Específicas
| **Função**             | **Obrigações em Comunicações Externas**                              |
|------------------------|-----------------------------------------------------------------------|
| **Colaboradores**      | Reportar e-mails suspeitos ao TI; validar identidade de terceiros.   |
| **Gestores**           | Autorizar compartilhamento de dados críticos; revisar NDAs.          |
| **DPO**                | Investigar violações; notificar autoridades dentro de 72 horas.      |
| **TI**                 | Bloquear plataformas não seguras; monitorar vazamentos em tempo real.|

## 7. Práticas Proibidas
- Enviar dados críticos via SMS ou redes sociais públicas.
- Usar serviços de e-mail pessoal (ex.: Gmail, Yahoo) para assuntos corporativos.
- Armazenar senhas de acesso em documentos não criptografados.
- Compartilhar credenciais de sistemas com terceiros sem autorização do DPO.

## 8. Resposta a Incidentes
1. **Bloqueio Imediato:** Revogar acessos e isolar sistemas comprometidos.
2. **Análise Forense:** Preservar logs e evidências digitais para investigação.
3. **Comunicação:** 
   - Titulares afetados: Notificar dentro de 72 horas (LGPD/GDPR).
   - ANPD: Relatório detalhado com causas e medidas corretivas.

## 9. Treinamento Obrigatório
- **Módulos:** 
  1. Identificação de phishing em comunicações externas.
  2. Uso correto de ferramentas criptografadas.
  3. Procedimentos para compartilhamento seguro com terceiros.
- **Frequência:** Treinamento inicial + atualizações semestrais.

## 10. Sanções
Violações resultarão em:
- **Leves** (ex.: uso de canal não autorizado): Advertência escrita + treinamento reforçado.
- **Graves** (ex.: vazamento de dados críticos): Suspensão + ação judicial por danos.