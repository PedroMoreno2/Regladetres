import streamlit as st
st.header("La vida en el mar")
listilla=["sardina","mero","tiburón ballena","pulpo"]
elec_animal=st.radio("Elige el animal que más te gusta:",listilla)
if elec_animal==listilla[0]:
    st.error("por el monte la sardina")
elif elec_animal==listilla[1]:
    st.warning("uno mero dos de febrero")
elif elec_animal==listilla[2]:
    st.success("por fin llegamos a lo que interesa")
elif elec_animal==listilla[3]:
    st.text("elige tiburón ballena por favor")
if(st.button("Click me for no reason")):
    st.markdown(":red[lo estás haciendo muy bien]")
elec_foto=st.selectbox("Fotos:",
                     ['F1', 'F2', 'F3'])
st.image("https://www.bekaretransfers.com/blog/wp-content/uploads/2017/05/whaleshark.jpeg")
st.image(F1)
fotoguay=Image.open(F1.jpg)
st.image(fotoguay,width=200)
fotillo=Image.open(elec_foto)
st.image(fotillo, width=200)