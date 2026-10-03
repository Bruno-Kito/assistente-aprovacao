# Assistente de Aprovação

O **Assistente de Aprovação** é um módulo simples e funcional desenvolvido em Python para auxiliar professores no cálculo da situação final de estudantes em uma disciplina.

A ferramenta considera duas notas (**N1** e **N2**) e a **frequência (%)**, aplicando regras específicas para determinar se o aluno está:

- **Aprovado**
- **Em Recuperação**
- **Reprovado**

---

## 🎯 Objetivo

Automatizar o processo de avaliação final, garantindo:

- Rapidez  
- Padronização  
- Redução de erros ao analisar notas e frequência  

---

## 📋 Regras de Avaliação

- **Aprovado:** média ≥ 7 **e** frequência ≥ 75%  
- **Recuperação:** média entre 5 e 6.99 **e** frequência ≥ 75%  
- **Reprovado:** média < 5 **ou** frequência < 75%

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- VS Code  
- Ambiente virtual (venv)  
- Git & GitHub  

---

## 📁 Estrutura do Projeto

```
assistente-aprovacao/
├── venv/              # Ambiente virtual
├── main.py            # Código principal do assistente
├── README.md          # Documentação do projeto
└── .gitignore         # Arquivos ignorados pelo Git
```

---

## ▶️ Como Executar

### 1. Ative o ambiente virtual

**Windows:**
```
venv\Scripts\activate
```

**Mac/Linux:**
```
source venv/bin/activate
```

### 2. Execute o programa
```
python main.py
```

---

## 💾 Como Clonar o Repositório
```
git clone https://github.com/Bruno-Kito/assistente-aprovacao.git
```

---

## ⭐ Observações

- O programa valida entradas para evitar erros do usuário.  
- Pode ser facilmente expandido para incluir novas regras ou relatórios.  
- Ideal para uso educacional ou como projeto de estudo em Python.  