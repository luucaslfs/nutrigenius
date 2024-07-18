# Canvas de Mapeamento de Fontes de Dados

## Instruções de Preenchimento

Preencha cada seção deste canvas para mapear as fontes de dados relevantes para a solução de IA. Este documento ajudará a identificar e organizar as fontes de dados necessárias para a construção e treinamento do modelo de IA.

### 1. Nome da Fonte de Dados

- Base de Dados de Pacientes
- Base de Dados de Receitas

### 2. Descrição da Fonte de Dados

- **Pacientes:** Base de dados com informações do paciente, do nutricionista, datas das ultimas consultas, descrição da Dieta, restrições alimentares; 
- **Receitas:** Base de dados de receitas com informações como nome da receita, ingredientes, modo de preparo, tempo estimado, quantidade de calorias;

### 3. Origem dos Dados

- Sistema de Gestão de Atendimento Nutricional
- Formulário preenchido pelo Profissional Nutricionista descrevendo a Dieta
- Fontes Externas de Receitas, como [Vitat](https://vitat.com.br/receitas/)

### 4. Tipo de Dados

- Dados numéricos (quantidade de calorias das receitas), dados textuais (nomes de pacientes e nutricionistas, descrição da dieta, receitas), dados temporais (datas e horários das últimas consultas).

### 5. Formato dos Dados

- **Pacientes:** Banco de dados NoSQL com id do paciente, id do nutricionista, datas das ultimas consultas, perfil do paciente, descrição da Dieta, restrições alimentares; 
- **Receitas:** Banco de Dados NoSQL com nome da receita, ingredientes, modo de preparo, tempo estimado, quantidade de calorias;

### 6. Frequência de Atualização

- Dados de Pacientes serão atualizados pelo profissional nutricionista.
- Dados de Receitas serão atualizados de acordo com a demanda e disponibilidade.

### 7. Qualidade dos Dados

- A preencher
- **Instruções:** Avalie a qualidade dos dados na fonte. Considere a completude, precisão, e a presença de dados faltantes ou errôneos.
- **Exemplo:** Dados geralmente completos, com algumas entradas com informações faltantes que precisam ser limpas.

### 8. Métodos de Coleta

- **Pacientes:** Inserção Manual pelo Profissional Nutricionista
- **Receitas:** Dados serão raspados e haverá importação automática via API

### 9. Acesso aos Dados

- **Pacientes:** Acesso via API REST fornecida pelo sistema de gestão de pacientes.
- **Receitas:** Acesso via API REST fornecida pelo sistema de gestão de receitas.

### 10. Proprietário dos Dados

- **Pacientes:** Os próprios Pacientes e o Profissional Nutricionista.
- **Receitas:** Propriedade do sistema em que forem coletadas (externo).

### 11. Restrições de Privacidade e Segurança

- Dados sensíveis de pacientes precisam de criptografia durante a transmissão e armazenamento, conforme regulamentações de proteção de dados pessoais.

### 12. Requisitos de Integração

- Necessidade de criar APIs para gerenciar os dados e fornece-los ao assistente.
