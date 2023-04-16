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
st.image(https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.bekaretransfers.com%2Fblog%2Fwp-content%2Fuploads%2F2017%2F05%2Fwhaleshark.jpeg&f=1&nofb=1&ipt=968b7797e170594c622da1f04f2fca3cc7de1aea4d0b823b37a3836f67433291&ipo=images)
st.image(F1)
fotoguay=Image.open(F1.jpg)
st.image(fotoguay,width=200)
fotillo=Image.open(elec_foto)
st.image(fotillo, width=200)