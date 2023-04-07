# SQL Injection Project

## Proposal
Build three applications: `./vulnerable`,  `./secure` and `./enterprise` that implement a **vault** in which visitors can:
 - Register with a name, email and a password
 - Log in with that email and password
 - Upload an image and a secret phrase, when logged in
 - See their image and secret phrase, when logged in
 - Change (only) their image and secret phrase, when logged in
 - See other people's names, but not their image or secret phrase

The `./vulnerable` application has several security flaws, which will be exploited using the scripts in `./exploits`. It is built with **Tech Stack 1**.

The `./secure` application fixes the security flaws present in the previous application, keeping the tech stack and core logic. It is built with **Tech Stack 1**.

The `./enterprise` application uses external services for critical processes, such as authentication. It is built with **Tech Stack 2**.

---

**Tech Stack 1**
 - Flask: Web framework
 - SQLite: Relational database
 - Hosted on a Debian 10 virtual private server with Nginx

**Tech Stack 2**
 - Nuxt: JavaScript framework
 - Firebase: Google Cloud solutions for hosting, authentication, database and image storage

## Execution

To install the required modules run:
```bash
pip install -r requirements.txt
```

And you can execute each application by running `python main.py`.

[Black](https://github.com/python/black) is used for code formatting.

<details>
<summary>Proposal feedback from professor</summary>
Caro Nicholas e restantes elementos do grupo,

Obrigado pelo e-mail com a proposta de tema.

SQL injection (de entre as várias vulnerabilidades inerentes a validação de inputs imprópria/inexistente), é um tópico relativamente simples mas que pode dar um trabalho interessante.

Fazer o trabalho em três passos (construção de aplicação vulnerável, exploração das vulnerabilidades, e correção/mitigação) é uma abordagem comum e aceitável.

Se virem o SEED Labs focado em SQLi, p.ex, irão encontrar uma abordagem semelhante lá também.

Posso deixar algumas sugestões de tópicos que podem pesquisar e eventualmente acrescentar ao vosso trabalho:

 - Explorar Web Application Firewalls (WAFs), especialmente se tiverem em consideração TLS/HTTPS -- são ferramentas muito comuns, e são úteis p.ex. quando não temos acesso a corrigir o código vulnerável. Também são úteis para detetar utilizadores que estejam a tentar fazer SQLi.

 - Se mantiverem a escolha de tecnologias que mencionaram também podem fazer um trabalho mais abrangente, não focado apenas em SQLi mas também noutras vulnerabilidades comuns em aplicações Flask (code injection, SSTI, etc. -- p.ex. https://github.com/stephenbradshaw/breakableflask) e eventual mitigação.

 - Se quiserem testar diferentes técnicas de SQLi, podem também inspirar-se em algo tipo DVWA (https://github.com/digininja/DVWA) e eventualmente usar ferramentas de ataque automatizadas.

Claro que as sugestões também dependem do progresso que forem fazendo ao longo das semanas, e dos tópicos que mais despertarem o vosso interesse.
</details>

## References
 - [Sqlite3 Python documentation](https://docs.python.org/3/library/sqlite3.html)
 - [Flask documentation](https://flask.palletsprojects.com/en/2.2.x/)
 - [DigitalOcean article Flask + SQLite](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application)
 - [Blobs in SQLite](https://stackoverflow.com/questions/51301395/how-to-store-a-jpg-in-an-sqlite-database-with-python)
 - [Breakable Flask GitHub repo](https://github.com/stephenbradshaw/breakableflask)
 - [Firebase documentation](https://firebase.google.com/docs)
