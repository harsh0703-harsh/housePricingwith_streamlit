import numpy as np 
import pandas as pd 
import streamlit as st
import pickle
import sqlite3
import datetime



linear=pickle.load(open("l_regressio.pkl","rb"))
decision=pickle.load(open("dt.pkl","rb"))




def main():
    st.title('HOUSE PRICE PREDICTION')
    hrrml=""" 
   <style>
   body{
   background-color: rgb(13, 190, 196);
   
   } 
    """
    st.markdown(hrrml,unsafe_allow_html=True)
    options=["Decision Tree Regressor","Linear Regression"]
    choice=st.sidebar.radio("Select the algorithm",options)
    bedrooms=st.number_input('No of bedreeoms ')
    bathrooms=st.number_input('No of bathrooms')
    sqft_living=st.number_input("Living room Area ")
    sqft_lot=st.number_input("Area of lot ")
    floors=st.number_input("Number of floors")
    waterfront=st.selectbox("Water view ",["Yes","No"])
    if waterfront=="Yes":
        waterfront=1
    else:
        waterfront=0
    condition=st.selectbox(" Rating" , [1, 2,3,4,5])
    sqft_above=st.number_input('sqft_aboves')
    years=[]
    for x in range(1900,2021):
        years.append(x)
    yr_built=st.selectbox("Year",years)
    lat=st.number_input('lat')
    sqft_living15=st.number_input('living root square foot ')
    sqft_lot15=st.number_input('Lot Square Foot ')

    if st.button("Price"):
        prediction=predicting_price(choice,bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,condition,sqft_above,yr_built,lat,sqft_living15,sqft_lot15)
        st.success("The house prics is {}".format(np.round(prediction),2))
       
    if st.button("About"):
        st.write("Made By Harsh")
        st.write("Credit goes to Krish Sir ")
    try:
        if st.sidebar.checkbox("Database"):
            st.header("Try to do prediction First")
            st.write("Database Created")
            st.write(pd.DataFrame({"Algotithm":[choice],"Bedrooms":[bedrooms],"bathrooms":[bathrooms],"sqft_Living":[sqft_living],"sqft_lot":[sqft_lot],"Floors":[floors],"Waterfront":[waterfront],"Rank":[condition],"sqft_above":[sqft_above],"yr_built":[yr_built],"Lat":[lat],"sqft_living15":[sqft_living15],"sqft_lot15":[sqft_lot15]}))
    except:
        st.write("Some Problem Happend !. Try to do predictions first")
            
def predicting_price(choice,bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,condition,sqft_above,yr_built,lat,sqft_living15,sqft_lot15):
    if choice==" ":
        st.warning("Please Select the Algorithm")
    elif choice=="Decision Tree Regressor":
        house_price=decision.predict([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,condition,sqft_above,yr_built,lat,sqft_living15,sqft_lot15]])
        return house_price
    elif  choice=="Linear Regression":
        house_price=house_price=linear.predict([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,condition,sqft_above,yr_built,lat,sqft_living15,sqft_lot15]])
        return house_price

    
if __name__=="__main__":
    main()



 