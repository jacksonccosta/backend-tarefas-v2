# API de Gerenciamento de Tarefas
### 👨🏾‍🏫 Por Jackson Costa | PUC-RIO - Pós Graduação em Engenharia de Software

Esta é a API backend para o projeto Gerenciador de Tarefas, que faz parte do <b>MVP da Sprint 1 do curso de Engenharia de Software</b>.<br />
<h4>Aqui estou utilizando as seguintes tecnologias:</h4>
<ul style="list-style-type: none;">
    <li>
        <img align="center" alt="Python" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
            Linguagem de programação <b>Python</b>
    </li>
    <li>
        <img align="center" alt="SQLite" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original-wordmark.svg" />
        Banco de Dados <b>SQLite</b>
    </li>
    <li>
          <img align="center" alt="SQLAlchemy" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" /> 
           ORM <b>SQLAlchemy</b></li>
    <li>
        <img align="center" alt="Swagger" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/swagger/swagger-original-wordmark.svg" />
        API com <b>Swagger</b> documentado com o Flask
    </li>
</ul>

## Funcionalidades
* Cadastro e listagem de **Usuários**.
* Criação, listagem, atualização e exclusão de **Tarefas por usuário**.
* Acesso seguro às tarefas via `header` de identificação (`X-User-Id`), garantindo que um usuário veja apenas suas próprias tarefas.

## Arquitetura e Padrões
Este projeto foi criado para seguir uma arquitetura de software robusta e escalável, baseada em camadas e nos princípios **SOLID**.

### Arquitetura em Camadas
A aplicação é dividida nas seguintes camadas, cada uma com sua responsabilidade bem definida:
* **Routes (Rotas):** Responsável por lidar com as requisições HTTP e as respostas. Ela atua como a porta de entrada da API, delegando o trabalho para a camada de serviço.
* **Services (Serviços):** Contém a lógica de negócio da aplicação. Orquestra as operações, validações e regras antes de interagir com os dados.
* **DAO (Data Access Object):** Camada de acesso aos dados. É a única parte do sistema que interage diretamente com o banco de dados, abstraindo a complexidade da persistência.
* **Models (Modelos):** Define a estrutura dos dados e o mapeamento objeto-relacional com o SQLAlchemy.

### Padrões e Conceitos Implementados
* **SOLID**:
    * **Princípio da Responsabilidade Única (SRP):** Aplicado diretamente na separação em camadas. Cada classe e módulo tem um, e somente um, motivo para mudar.
    * **Princípio da Inversão de Dependência (DIP):** A camada de Rotas não depende diretamente do DAO, mas sim da abstração fornecida pela camada de Serviços.
* **Padrão de Projeto DAO:** Utilizado para isolar completamente a lógica de acesso ao banco de dados, tornando o código mais limpo, testável e fácil de manter.
* **Fábrica de Aplicação (Application Factory):** O app Flask é criado e configurado dentro de uma função, uma prática recomendada para facilitar testes e a configuração de múltiplos ambientes.

## Instruções de Instalação

1.  Clone este repositório.
2.  Navegue até a pasta do projeto: `cd backend-tarefas`
3.  Crie e ative um ambiente virtual:
    ```bash
    py -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```
4.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Comandos de Inicialização

Para iniciar o servidor da API, execute o seguinte comando:

```bash
py run.py
```

## Observação:
O banco de dados (tarefas.db) e suas tabelas serão criados automaticamente na primeira vez que o servidor for iniciado.

## <img align="center" alt="Postman" height="40" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postman/postman-original.svg" /> POSTMAN:
Caso queira testar os endpoints no Postman, aqui na pasta do projeto consta o arquivo <b>PUC-MVP1.postman_collection.json</b> com as Collections que podem ser importadas no Postman.