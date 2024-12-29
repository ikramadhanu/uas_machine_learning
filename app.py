import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd

with st.sidebar:
    selected = option_menu("Algorithm", 
        ["SUPPORT VECTOR MACHINE", "PERCEPTRON", "LOGISTIC REGRESSION"], 
        default_index=0)

# SUPPORT VECTOR MACHINE    
if (selected=="SUPPORT VECTOR MACHINE"):
    st.title("SUPPORT VECTOR MACHINE")
    st.divider()
    st.title('FISH CLASSIFICATION')
    length = st.number_input("Length")
    weight = st.number_input("Weight")
    w_l_ratio = st.number_input("w_l_ratio")
    fish = st.button("Predict Fish")
    if fish:
        st.success('PREDICTION : ')
    st.divider()

    st.title('PUMPKIN CLASSIFICATION')
    Area = st.number_input('Area')
    Perimeter = st.number_input('Perimeter')
    Major_Axis_Length = st.number_input('Major_Axis_Length')
    Minor_Axis_Length = st.number_input('Minor_Axis_Length')
    Convex_Area = st.number_input('Convex_Area') 
    Equiv_Diameter = st.number_input('Equiv_Diameter')
    Eccentricity = st.number_input('Eccentricity')
    Solidity = st.number_input('Solidity')
    Extent = st.number_input('Extent')
    Roundness = st.number_input('Roundness')
    Aspect_Ration = st.number_input('Aspect_Ration')
    Compactness = st.number_input('Compactness')
    pumpkin = st.button("Predict Pumpkin")
    if pumpkin:
        st.success('PREDICTION : ')
    st.divider()

    st.title('FRUIT CLASSIFICATION')
    diameter = st.number_input('diameter')
    weight = st.number_input('weight')
    red = st.slider('red', 0, 255)
    green = st.slider('green', 0, 255)
    blue = st.slider('blue', 0, 255)
    fruit = st.button("Predict Fruit")

    if fruit:
        with open('Model/svm_fruit.pickle', "rb") as r:
            svc = pickle.load(r)
        new_data = {
            'diameter' : [diameter],
            'weight' : [weight],
            'red' : [red],
            'green' : [green],
            'blue' : [blue]
        }
        new_data = pd.DataFrame(new_data)
        scaler = StandardScaler()
        scaled_new_data = scaler.fit_transform(new_data)
        new_prediction = svc.predict(new_data)

        if new_prediction[0] == 0 :
            hasil = 'grapefruit'
        else:
            hasil = 'orange'
        
        st.success('PREDICTION : {}'.format(hasil))
    st.divider()
    
# PERCEPTRON  
if (selected=="PERCEPTRON"):
    st.title("PERCEPTRON")
    st.divider()
    st.title('FISH CLASSIFICATION')
    length = st.number_input("Length")
    weight = st.number_input("Weight")
    w_l_ratio = st.number_input("w_l_ratio")
    fish = st.button("Predict Fish")
    if fish:
        st.success('PREDICTION : ')
    st.divider()

    st.title('PUMPKIN CLASSIFICATION')
    Area = st.number_input('Area')
    Perimeter = st.number_input('Perimeter')
    Major_Axis_Length = st.number_input('Major_Axis_Length')
    Minor_Axis_Length = st.number_input('Minor_Axis_Length')
    Convex_Area = st.number_input('Convex_Area') 
    Equiv_Diameter = st.number_input('Equiv_Diameter')
    Eccentricity = st.number_input('Eccentricity')
    Solidity = st.number_input('Solidity')
    Extent = st.number_input('Extent')
    Roundness = st.number_input('Roundness')
    Aspect_Ration = st.number_input('Aspect_Ration')
    Compactness = st.number_input('Compactness')
    pumpkin = st.button("Predict Pumpkin")
    if pumpkin:
        st.success('PREDICTION : ')
    st.divider()

    st.title('FRUIT CLASSIFICATION')
    diameter = st.number_input('diameter')
    weight = st.number_input('weight')
    red = st.slider('red', 0, 255)
    green = st.slider('green', 0, 255)
    blue = st.slider('blue', 0, 255)
    fruit = st.button("Predict Fruit")
    
    if fruit:
        with open('Model/perceptron_fruit.pickle', "rb") as r:
            perceptron = pickle.load(r)
        new_data = {
            'diameter' : [diameter],
            'weight' : [weight],
            'red' : [red],
            'green' : [green],
            'blue' : [blue]
        }
        new_data = pd.DataFrame(new_data)
        scaler = StandardScaler()
        scaled_new_data = scaler.fit_transform(new_data)
        new_prediction = perceptron.predict(new_data)

        if new_prediction[0] == 0 :
            hasil = 'grapefruit'
        else:
            hasil = 'orange'
        
        st.success('PREDICTION : {}'.format(hasil))
    st.divider()

# LOGISTIC REGRESSION  
if (selected=="LOGISTIC REGRESSION"):
    st.title("LOGISTIC REGRESSION")
    st.divider()
    st.title('FISH CLASSIFICATION')
    length = st.number_input("Length")
    weight = st.number_input("Weight")
    w_l_ratio = st.number_input("w_l_ratio")
    fish = st.button("Predict Fish")
    if fish:
        st.success('PREDICTION : ')
    st.divider()

    st.title('PUMPKIN CLASSIFICATION')
    Area = st.number_input('Area')
    Perimeter = st.number_input('Perimeter')
    Major_Axis_Length = st.number_input('Major_Axis_Length')
    Minor_Axis_Length = st.number_input('Minor_Axis_Length')
    Convex_Area = st.number_input('Convex_Area') 
    Equiv_Diameter = st.number_input('Equiv_Diameter')
    Eccentricity = st.number_input('Eccentricity')
    Solidity = st.number_input('Solidity')
    Extent = st.number_input('Extent')
    Roundness = st.number_input('Roundness')
    Aspect_Ration = st.number_input('Aspect_Ration')
    Compactness = st.number_input('Compactness')
    pumpkin = st.button("Predict Pumpkin")
    if pumpkin:
        st.success('PREDICTION : ')
    st.divider()

    st.title('FRUIT CLASSIFICATION')
    diameter = st.number_input('diameter')
    weight = st.number_input('weight')
    red = st.slider('red', 0, 255)
    green = st.slider('green', 0, 255)
    blue = st.slider('blue', 0, 255)
    fruit = st.button("Predict Fruit")
    if fruit:
        with open('Model/logistic_fruit.pickle', "rb") as r:
            log = pickle.load(r)
        new_data = {
            'diameter' : [diameter],
            'weight' : [weight],
            'red' : [red],
            'green' : [green],
            'blue' : [blue]
        }
        new_data = pd.DataFrame(new_data)
        scaler = StandardScaler()
        scaled_new_data = scaler.fit_transform(new_data)
        new_prediction = log.predict(new_data)

        if new_prediction[0] == 0 :
            hasil = 'grapefruit'
        else:
            hasil = 'orange'
        
        st.success('PREDICTION : {}'.format(hasil))
    st.divider()