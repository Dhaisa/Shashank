import streamlit

st.code("""
 def goo(input):
    return a**2
 x = goo(2)""")

st.latex('x^2 + y^2 +2 = 0')

df = pd.DataFrame({
              'Name':['Rahul','Suresh','Mukesh'],
              'UnderGrad':['Amity','DTU','VIT'],
              'CGPA':[8.34,9.23,7.87]
                   })
st.dataframe(df)
st.metric('Increment','20k','15%')
st.json(({
              'Name':['Rahul','Suresh','Mukesh'],
              'UnderGrad':['Amity','DTU','VIT'],
              'CGPA':[8.34,9.23,7.87]
                   }))
st.image('k.jpeg')

st.video('AdChng1.mp4')
st.sidebar.title('Sidebar ka Title')
c1,c2 = st.columns(2)
with c1:
    st.image('k.jpeg')
with c2:
    st.image('rt.jpeg')
    st.image('nj.jpeg')
st.error('Login Failed')
st.success('Login Successful')
st.info('Information')
st.warning('Warning')

bar = st.progress(0)
for i in range(1,101):
    time.sleep(0.01)
    bar.progress(i)
em1 = st.text_input('Enter your email')
number = st.number_input('Enter your Age')
date = st.date_input('Enter your Date of birth')

streamlit.header('Here is my 2nd commit')
