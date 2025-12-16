# Relatório do Projeto Final – Desenvolvimento de Aplicação Mobile com Flutter

## 1. Identificação

* **Aluno:** Thiago de Sousa Santos
* **Disciplina:** Dispositivos Móveis
* **Trabalho:** Projeto Final
* **Tecnologia utilizada:** Flutter
* **Repositório GitHub:**
  [https://github.com/thiago21sousa21/IFPI/tree/main/dispositivos_moveis/otilio/prova/projeto_final](https://github.com/thiago21sousa21/IFPI/tree/main/dispositivos_moveis/otilio/prova/projeto_final)

---

## 2. Objetivo do Projeto

O objetivo deste projeto é desenvolver uma aplicação mobile utilizando **Flutter**, aplicando conceitos de **arquitetura MVC**, navegação entre telas, armazenamento de dados e integração com **Google Maps**. O sistema permite o cadastro de usuários, autenticação (login), gerenciamento de contatos e visualização geográfica desses contatos em um mapa.

---

## 3. Descrição Geral do Sistema

A aplicação foi desenvolvida individualmente e consiste em um fluxo simples e intuitivo. Após o cadastro e login do usuário, o sistema direciona para uma tela inicial (Home), onde é possível acessar as principais funcionalidades do aplicativo.

O sistema possui as seguintes telas principais:

* Tela de Login
* Tela de Cadastro
* Tela Home
* Tela de Contatos
* Tela de Adicionar/Editar Contato
* Tela de Mapas (Google Maps)

---

## 4. Funcionalidades Implementadas

### 4.1 Tela de Cadastro

Permite que o usuário crie uma conta informando seus dados básicos. Após o cadastro, o usuário pode realizar o login normalmente no sistema.

---

### 4.2 Tela de Login

Responsável pela autenticação do usuário. Após o login bem-sucedido, o usuário é redirecionado para a tela Home.

---

### 4.3 Tela Home

A tela Home contém dois botões principais:

* **Contatos:** direciona o usuário para a tela de gerenciamento de contatos.
* **Mapas:** direciona o usuário para a tela de mapas com os marcadores dos contatos cadastrados.

---

### 4.4 Tela de Contatos

Nesta tela, o usuário pode:

* Visualizar a lista de contatos cadastrados
* Adicionar novos contatos
* Selecionar um contato existente para edição

---

### 4.5 Tela de Adicionar / Editar Contato

Foi utilizada uma única tela tanto para adicionar quanto para editar contatos, reaproveitando a mesma estrutura. O formulário contém os seguintes campos:

* Nome
* Email
* Latitude
* Longitude

Após o preenchimento, os dados são armazenados e ficam disponíveis tanto na lista de contatos quanto na tela de mapas.

---

### 4.6 Tela de Mapas (Google Maps)

A tela de mapas exibe um mapa utilizando o **Google Maps**, contendo marcadores referentes aos contatos cadastrados.

Cada marcador:

* É posicionado exatamente conforme a latitude e longitude informadas
* Ao ser clicado, exibe o nome e o email do contato

Essa funcionalidade permite a visualização geográfica dos contatos de forma clara e interativa.

---

## 5. Armazenamento de Dados

Os dados dos usuários e dos contatos são armazenados localmente, permitindo que as informações persistam durante o uso da aplicação. O armazenamento possibilita recuperar os contatos tanto para edição quanto para exibição no mapa.

---

## 6. Arquitetura Utilizada

O projeto foi desenvolvido seguindo a arquitetura **MVC (Model–View–Controller)**:

* **Model:** responsável pela definição das estruturas de dados (usuários e contatos).
* **View:** responsável pelas telas e interface gráfica do aplicativo.
* **Controller:** responsável pela lógica de negócio, controle dos dados e comunicação entre Model e View.

Essa arquitetura facilita a organização do código, manutenção e escalabilidade do projeto.

---

## 7. Tecnologias e Ferramentas Utilizadas

* Flutter
* Dart
* Google Maps API
* Git e GitHub

---

## 8. Considerações Finais

O desenvolvimento deste projeto permitiu aplicar na prática os conceitos aprendidos em sala de aula, incluindo navegação entre telas, formulários, integração com mapas, arquitetura MVC e organização de código em Flutter.

A aplicação atende a todos os requisitos propostos no trabalho, apresentando um funcionamento correto, interface intuitiva e integração com serviços externos como o Google Maps.

---

**Autor:** Thiago de Sousa Santos
