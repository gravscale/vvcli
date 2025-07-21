## Interface de Linha de Comando (CLI)

### 🚀 Configuração Recomendada
#### Variáveis de ambiente

```bash
  export VVCLI_API_ENDPOINT="https://api.under.com.br/api/v1"
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
  vvcli auth configure -t "SEU_API_TOKEN" 
```

### 🏢 `account` - Gestão de Contas
Administra contas de clientes e contratos

#### Subcomandos disponíveis:
```bash
    vvcli account list       # Lista contas disponíveis
    vvcli account contracts  # Lista contratos ativos
```

### 📦 `obj` - Armazenamento de Objetos
Operações com armazenamento de objetos (S3-compatível)

#### Comandos fundamentais:
```bash
    vvcli obj user      # Gerencia usuários de armazenamento
    vvcli obj subuser   # Gerencia subusuários de armazenamento
```

**Exemplo de uso**:
```bash
  vvcli obj user add -c 1001011 -j # Cria usuário e retorna resultado em JSON
```

---




### ❓ Ajuda Adicional
Acesse documentação detalhada com:  
`vvcli [comando] --help`  
Exemplo: `vvcli obj user add --help`
