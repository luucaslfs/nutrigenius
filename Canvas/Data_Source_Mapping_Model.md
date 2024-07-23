# Canvas de Mapeamento de Fontes de Dados

## Instruções de Preenchimento

Preencha cada seção deste canvas para mapear as fontes de dados relevantes para a solução de IA. Este documento ajudará a identificar e organizar as fontes de dados necessárias para a construção e treinamento do modelo de IA.

### 1. Nome da Fonte de Dados

- **Base de Dados de Usuários**
- **Base de Dados de Receitas**

### 2. Descrição da Fonte de Dados

- **Usuários:** Base de dados contendo informações dos usuários, incluindo preferências alimentares, restrições dietéticas, metas de saúde, histórico de interação com o assistente, e dados de progresso.
- **Receitas:** Base de dados de receitas com informações como nome da receita, ingredientes, modo de preparo, tempo estimado, quantidade de calorias, nutrientes e categorias.

### 3. Origem dos Dados

- **Usuários:** Input do usuário através do aplicativo.
- **Receitas:** Fontes externas de receitas, como [Vitat](https://vitat.com.br/receitas/), e receitas inseridas manualmente.

### 4. Tipo de Dados

- **Usuários:** Dados textuais (preferências e restrições), dados numéricos (metas de saúde, calorias), dados categóricos (categorias de dieta), dados temporais (histórico de interação).
- **Receitas:** Dados textuais (ingredientes, modo de preparo), dados numéricos (calorias, nutrientes), dados categóricos (categorias de receita), dados temporais (tempo de preparo).

### 5. Formato dos Dados

- **Usuários:** Banco de dados com id do usuário, preferências alimentares, restrições dietéticas, metas de saúde, histórico de interação.
- **Receitas:** Banco de dados com nome da receita, ingredientes, modo de preparo, tempo estimado, quantidade de calorias, nutrientes, categorias.

### 6. Frequência de Atualização

- **Usuários:** Dados atualizados continuamente conforme os usuários interagem com o aplicativo e atualizam suas informações.
- **Receitas:** Dados de receitas atualizados de acordo com a demanda e a disponibilidade de novas receitas.

### 7. Qualidade dos Dados

- **Usuários:** Dados geralmente completos, mas sujeitos a variações na precisão dependendo da entrada do usuário.
- **Receitas:** Dados geralmente completos, com algumas entradas necessitando de validação manual para assegurar precisão e completude.

### 8. Métodos de Coleta

- **Usuários:** Inserção manual pelos usuários através do aplicativo.
- **Receitas:** Dados raspados de fontes externas e importação automática via API, além de inserção manual.

### 9. Acesso aos Dados

- **Usuários:** Acesso via API REST fornecida pelo sistema de gestão de usuários.
- **Receitas:** Acesso via API REST fornecida pelo sistema de gestão de receitas.

### 10. Proprietário dos Dados

- **Usuários:** Os próprios usuários e a empresa que opera o aplicativo.
- **Receitas:** Propriedade do sistema em que foram coletadas (externo) e da empresa que opera o aplicativo.

### 11. Restrições de Privacidade e Segurança

- Dados sensíveis de usuários necessitam de criptografia durante a transmissão e armazenamento, conforme regulamentações de proteção de dados pessoais, como a LGPD.
- As receitas, embora menos sensíveis, devem ser geridas com respeito aos direitos autorais e de propriedade intelectual.

### 12. Requisitos de Integração

- Necessidade de criar APIs para gerenciar os dados e fornecê-los ao assistente.
- Transformação de dados de formatos externos (como CSV ou JSON) para o formato interno do banco de dados NoSQL.
- Sincronização contínua com a base de dados de usuários e receitas para garantir atualizações em tempo real.
