## Interface de Linha de Comando (CLI)

### 🚀 Configuração Recomendada
#### Variáveis de ambiente

```bash
  export VVCLI_API_ENDPOINT="https://api.under.com.br/v1"
```

Após instalação, execute no terminal:

```bash
  # Estrutura básica de comandos
  vvcli [COMANDO_PRINCIPAL] [SUBCOMANDO] [PARÂMETROS] [OPÇÕES]
```

### 🔐 `auth` - Autenticação e Sessão
Gerencia credenciais e tokens de acesso

#### Subcomandos essenciais:
```bash
    vvcli auth info         # Exibe dados do usuário autenticado
    vvcli auth configure    # Autentica usuário recebendo API Token
```

**Exemplo de autenticação**:
```bash
  vvcli auth configure -t API_TOKEN  #Inclua sua chave de API fornecida pelo under control
```

### 🏢 `account` - Gestão de Contas
Administra contas de clientes e contratos

#### Subcomandos disponíveis:
```bash
    vvcli account list       # Lista contas disponíveis
    vvcli account contracts  # Lista contratos ativos
```

### 📦 `obj` - Armazenamento de Objetos

Gerencie recursos compatíveis com S3, incluindo usuários, subusuários e buckets. Utilize os subcomandos para criar, listar e administrar permissões e quotas de armazenamento.

#### Subcomandos principais:
```bash
    vvcli obj user      # Gerencia usuários S3 (criação, listagem)
    vvcli obj subuser   # Gerencia subusuários S3 (vinculação, permissões)
    vvcli obj bucket    # Gerencia buckets S3 (criação, listagem, exclusão) 
```

#### 👤 `user` - Usuários S3

Gerencie usuários S3, incluindo criação, listagem e definição de quotas. Permite vincular subusuários, configurar permissões e visualizar detalhes dos usuários.

Principais operações:
- `add`: Cria um novo usuário S3 com quota definida.
  
    **Parâmetros aceitos:**
    - `-c`, `--client-id` _(obrigatório)_: ID do cliente ao qual o usuário será vinculado.
    - `-j`, `--json` _(opcional)_: Retorna o resultado em formato JSON.
    - `-s`, `--size-quota` _(obrigatório)_: Quota de armazenamento em GB para o usuário S3.
    - `--help`: Exibe ajuda detalhada sobre o comando e seus parâmetros.

- `get`: Retorna usuário S3 cadastrados. 

    **Parâmetros aceitos:**
    - `-c`, `--client-id` _(obrigatório)_: ID do cliente ao qual o usuário será vinculado.
    - `-j`, `--json` _(opcional)_: Retorna o resultado em formato JSON.
    - `--help`: Exibe ajuda detalhada sobre o comando e seus parâmetros.

**Exemplo de uso**:
```bash
  vvcli obj user add -c 1001011 -j -s 100 # Cria usuário S3 com quota de 100GB e retorna resultado em JSON
```

#### 👤 `subuser` - Sub Usuários S3

Gerencie subusuários S3, incluindo criação, listagem e vinculação a usuários S3. Permite configurar permissões específicas para cada subusuário.
Um subusuário é um tipo de utilizador associado a um utilizador principal, permitindo uma gestão de acesso mais granular

**Principais operações:**
- `add`: Cria um novo subusuário S3.

  **Parâmetros aceitos:**
  - `-c`, `--client-id` _(opcional)_: ID do cliente ao qual o subusuário será vinculado.
  - `-d`, `--display-name` _(opcional)_: Nome de exibição do subusuário.
  - `-a`, `--access` _(opcional)_: Permissões de acesso (`read`, `write`, `readwrite`).
  - `-j`, `--json` _(opcional)_: Retorna o resultado em formato JSON.
  - `--help`: Exibe ajuda detalhada sobre o comando e seus parâmetros.

- `list`: Lista todos os subusuários S3 cadastrados. 

  **Parâmetros aceitos:**
    - `-c`, `--client-id` _(opcional)_: ID do cliente ao qual o subusuário será vinculado.
    - `-j`, `--json` _(opcional)_: Retorna o resultado em formato JSON.
    - `--help`: Exibe ajuda detalhada sobre o comando e seus parâmetros.

**Exemplo de uso:**
```bash
  vvcli obj subuser add -c 1001011 -d "João Sub" -a readwrite -j
```

####  👤 `bucket` - Buckets S3

Gerencie buckets S3, incluindo criação, listagem e exclusão. Permite configurar quota e visualizar detalhes dos buckets.
**Principais operações:**
- `add`: Cria um novo bucket para armazenamento de objetos S3.

  **Parâmetros aceitos:**
  - `-c`, `--client-id` _(opcional)_: ID do cliente ao qual o bucket será associado.
  - `-b`, `--bucket-name` _(opcional)_: Nome do bucket a ser criado.
  - `-s`, `--size-quota` _(opcional)_: Quota do bucket em megabytes (MB).
  - `-m`, `--max-objects` _(opcional)_: Número máximo de objetos permitidos no bucket.
  - `-j`, `--json` _(opcional)_: Retorna o resultado em formato JSON.
  - `--help`: Exibe ajuda detalhada sobre o comando e seus parâmetros.

- `list`: Lista todos os buckets S3 cadastrados.

  **Parâmetros aceitos:**
  - `-c`, `--client-id` _(opcional)_: ID do cliente para filtrar os buckets.
  - `-j`, `--json` _(opcional)_: Retorna o resultado em formato JSON.
  - `--help`: Exibe ajuda detalhada sobre o comando e seus parâmetros.

- `rm`: Remove um bucket S3 cadastrados. 

    **Parâmetros aceitos:**
    - `-c`, `--client-id` _(opcional)_: ID do cliente associado ao bucket.
    - `-n`, `--name` _(opcional)_: Nome do bucket a ser removido.
    - `--help`: Exibe ajuda detalhada sobre o comando e seus parâmetros.

**Exemplos de uso:**
```bash
  vvcli obj bucket add -c 1001011 -b "meu-bucket" -s 10240 -m 10000 -j
  vvcli obj bucket list -c 1001011 -j
  vvcli obj bucket rm -c 1001011
```
---
### ❓ Ajuda Adicional
Acesse documentação detalhada com:  
`vvcli [comando] --help`  
Exemplo: `vvcli obj user add --help`
