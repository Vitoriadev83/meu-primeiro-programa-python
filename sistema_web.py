import streamlit as st
import datetime

st.title("Cadastro de Clientes")

nome = st.text_input("Digite o nome do cliente")
endereco = st.text_input("Digite o endereço")
dt_nasc = st.date_input("Escolha a data de nascimento",
             min_value= datetime.date(1900, 1, 1),
             max_value= datetime.date.today(), 
             format= "DD/MM/YYYY")
tipo_cliente = st.selectbox("Tipo de cliente",
                            ["Pessoa física", "Pessoa jurídica"])

cadastrar = st.button("Cadastrar cliente")

if cadastrar:
  with open("clientes.csv", "a", encoding="utf8") as arquivo:
    arquivo.write(f"{nome}, {endereco} {dt_nasc}, {tipo_cliente} \n")
    st.success("Cliente cadastrado com sucesso!")
                  

                     