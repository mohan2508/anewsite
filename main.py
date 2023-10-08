import streamlit as st

from streamlit_option_menu import option_menu

st.write('<style>div.row-widget.stRadio>div{flex-direction:row;}</style>',unsafe_allow_html=True)  
    
btn = st.radio('',('HOME','ABOUT US','VISION','TUTORIALS','ONLINE','CONTACT'))  


st.markdown('''<div class="card mb-4 shadow-sm">
        <img src="https://source.unsplash.com/900x200/?nature,nature" ice="d-block w-100" alt="...">''',unsafe_allow_html=True)



st.sidebar.title('Welcome to Mohan Classes')
st.sidebar.markdown('''<div class="card mb-4 shadow-sm">
        <img src="https://source.unsplash.com/300x1100/?nature,nature" nature="d-block w-100" alt="...">''',unsafe_allow_html=True)

if btn == 'HOME':
        column1,column2,column3 = st.columns(3)
        with column1:
                st.title('Welcome to MohanClasses')
        with column3:
                st.write('''<div class="card mb-4 shadow-sm">
                <img src="https://source.unsplash.com/415x500/?nature,students" class="d-block w-100" alt="...">''',unsafe_allow_html=True)

elif btn == 'ABOUT US':
        
        column1,column2 = st.columns(2)

        with column1:
                st.title('Welcome to MohanClasses')
                st.markdown("[Watch Videos..........](https://www.youtube.com/channel/UCth-wWcoRoR-1wx4YO0O_Bw)")
        with column2:
                st.write('''
                MohanClasses is the coaching centre for CBSE,STATE and METRICULATION board students in 
                the areas of Kelambakkam,our commitment to providing a good academic education to our students. 
            
                MohanClasses give a more individualised experience with knowledgeable instructors who can explain concepts in more detail,
                answer questions,and provide new perspectives. Students benefit from this since they are better able to understand the material and use it correctly on 
                tests.
              
                Never force students to learn under pressure, and provides a planned way of 
                studying, along with quick tips and smart-study advice.Math tutoring gives your child exactly what they need to help supplement
                in-class learning.
             
                If you are looking for the best Maths coaching classes in Kelambakkam,MohanClasses is the top choice.  
                Customized study plans, and personalized attention, MohanClasseshelps students improve their Math skills quickly and effectively.''')    

    
elif btn == 'VISION':
        column1,column2 = st.columns(2)
        with column1:
                st.title('A Commitment to Excellence') 
        with column2:  
                st.write('''
                         At MohanClasses!!, we make great efforts to provide our students 
                         with having a wide scope that offers engaging and 
                         fulfilling experiences, preparing them for a rich social and cultural life. 


                         At MohanClasses, we take pride in offering personalized 
                         attention to each of our students, whether through our textbooks or 
                         hands-on training. Our goal is to help every student to expose in their 
                         subjects, achieve better scores.''') 
elif btn == 'TUTORIALS':
        st.write('<style>div.row-widget.stRadio>div{flex-direction:row;}</style>',unsafe_allow_html=True)  
    
        std = st.radio('Click the button below for your tutorials',('VIII STD','IX STD','X STD'))    

        if std == 'VIII STD':
                st.write("Tutorials for VIII STD")
                left_column,right_column = st.columns(2)
    
                with left_column:
                        st.markdown("[Square and Square Roots...............](https://www.youtube.com/watch?v=Ze2cRx39va0&t=54s)")
                        st.markdown("[comparing quantities_Part_I...........](https://www.youtube.com/watch?v=InDKtQ_9PZ0&t=6s)")
                        st.markdown("[comparing quantities_Part_II..........](https://www.youtube.com/watch?v=cedH0IFkEdE&t=15s)")
                        st.markdown("[Direct and Invers proportion .........](https://www.youtube.com/watch?v=ysMoG6HBSoc&t=130s)")
                        st.markdown("[Playing with Numbers .................](https://www.youtube.com/watch?v=Y6P0K08dHEc&t=1s)")
                        st.markdown("[Profit,Loss and Discount .............](https://www.youtube.com/watch?v=9rw8rtStT_U&t=95s)")
                with right_column:    
                        st.markdown("[Simple Interest and CI ...............](https://www.youtube.com/watch?v=838w989Rx7A&t=521s)")

        elif std == 'IX STD':
                st.write("Tutorials for IX STD")
                left_column,right_column = st.columns(2)
    
                with left_column:
                        st.markdown("[Number Systems...............](https://www.youtube.com/watch?v=TjZwzHqtU1A&t=502s)")
                        st.markdown("[Law of Exponents...........](https://www.youtube.com/watch?v=ACe55Y7KaKM&t=4s)")
                        st.markdown("[Polynomials _Part_I..........](https://www.youtube.com/watch?v=NwYli_8F3yE&t=36s)")
                        st.markdown("[Polynomials _Part_II .........](https://www.youtube.com/watch?v=9jJnwXu4Ats&t=215s)")
                        st.markdown("[Polynomials _Part_III .................](https://www.youtube.com/watch?v=6Uzgg_d6fGA&t=154s)")
                        st.markdown("[Coordinate Geometry .............](https://www.youtube.com/watch?v=6AWLXDU80e4&t=292s)")
                        st.markdown("[Circles_Part_I ...............](https://www.youtube.com/watch?v=GQ2Uh1ARRDc&t=34s)")
                        st.markdown("[Circles_Part_II ...............](https://www.youtube.com/watch?v=9x0-bn6eGcY&t=147s)")
                with right_column:    
                        st.markdown("[Heron's Formula ...............](https://www.youtube.com/watch?v=KLuMtELAM5k&t=9s)")
                        st.markdown("[Linear Equations in two variables ...............](https://www.youtube.com/watch?v=wbPJDiHJ3Kw&t=22s)")
                        st.markdown("[Lines and Angles_Part_I ...............](https://www.youtube.com/watch?v=Ty7iKh7_gDg&t=967s)")
                        st.markdown("[Lines and Angles_Part_II...............](https://www.youtube.com/watch?v=isk5okItLL8)")
                        st.markdown("[Quadrilaterals ...............](https://www.youtube.com/watch?v=G7srkaP4Dqc&t=219s)")
                        st.markdown("[Triangles_Part_I ...............](https://www.youtube.com/watch?v=1EGMxAmSGzI&t=592s)")
                        st.markdown("[Triangles_Part_II ...............](https://www.youtube.com/watch?v=vcrStIT-GBw&t=428s)")

        else:
                st.write("Tutorials for X STD")
                left_column,right_column = st.columns(2)
    
                with left_column:
                        st.markdown("[Real Numbers Part_I...............](https://www.youtube.com/watch?v=w6ikrQxSFYM&t=9s)")
                        st.markdown("[Real Numbers Part_II...........](https://www.youtube.com/watch?v=M5i04l-F5FI&t=3s)")
                        st.markdown("[Real Numbers Part_III..........](https://www.youtube.com/watch?v=aVFoxdqlp60&t=38s)")
                        st.markdown("[Pair of Linear Equations Part_I .........](https://www.youtube.com/watch?v=SvbGEaYxWsI&t=28s)")
                        st.markdown("[Pair of Linear Equations Part_II .................](https://www.youtube.com/watch?v=vZZ7RzjX-wk&t=32s)")
                        st.markdown("[Pair of Linear Equations Part_III .............](https://www.youtube.com/watch?v=9jJnwXu4Ats&t=3s)")
                        st.markdown("[Quadratic Equations Part_I...............](https://www.youtube.com/watch?v=lMTWPCTeNVA&t=2s)")
                        st.markdown("[Quadratic Equations Part_II...............](https://www.youtube.com/watch?v=GZIR_CVYEKk&t=117s)")
                        st.markdown("[Arithmetic Progression Part_I...............](https://www.youtube.com/watch?v=Q4IrOuG5PVA)")
                        st.markdown("[Arithmetic Progression Part_II...............](https://www.youtube.com/watch?v=vMjAGr8ap34&t=10s)")
                with right_column:    
                        st.markdown("[Trigonometry Part_I ...............](https://www.youtube.com/watch?v=ikypRqXi3G4&t=144s)")
                        st.markdown("[Trigonometry Part_II...............](https://www.youtube.com/watch?v=ikypRqXi3G4&t=144s)")
                        st.markdown("[Trigonometry Applications Part_I...............](https://www.youtube.com/watch?v=Xi3Y0sPxb2U&t=140s)")
                        st.markdown("[Trigonometry Applications Part_II...............](https://www.youtube.com/watch?v=G3SRYjQZ94Q&t=137s)")
                        st.markdown("[Circles Part_I...............](https://www.youtube.com/watch?v=PZjnNOccfac&t=591s)")
                        st.markdown("[Circles Part_II...............](https://www.youtube.com/watch?v=3n8W4bJUy-U&t=291s)")
                        st.markdown("[Probability Part_I...............](https://www.youtube.com/watch?v=1gSAdx9GYXY&t=10s)")
                        st.markdown("[Probability Part_II...............](https://www.youtube.com/watch?v=FIJns01KDKA)")

elif btn == 'ONLINE': 
        column1,column2,column3 =st.columns(3)
      
        with column1:
                st.title("There will be two sessions ")
        
        with column3:
                st.title('Morning')
                st.write('6.00 am  -  7.00 am')
                st.title('Evening')
                st.write('7.30 pm  -  8.30pm') 
                st.write('8.40 pm -   9.40pm')  
    
        st.write('Interested students can contact over phone or in whatsapp') 

else:
        st.write('______________________________________________________________________________________') 
    
        st.title("E-Mail: MohanClasses100@gmail.com")
        st.title("Mobile: 73581 12054")
        st.title("Whatsapp No. : 73581 12054") 
    
        st.write('______________________________________________________________________________________') 
        
hide_streamlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
Manage app{visibility:hidden}
deploy{visibility:hidden}
Header{visibility:hidden}
footer{visibility:hidden}

</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)                    
              
                     








