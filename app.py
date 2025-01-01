import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd

# Sidebar
with st.sidebar:
    selected = option_menu("Algorithm", 
        ["SUPPORT VECTOR MACHINE", "PERCEPTRON", "LOGISTIC REGRESSION"], 
        default_index=0)

# SUPPORT VECTOR MACHINE    
if (selected=="SUPPORT VECTOR MACHINE"):
    st.title("SUPPORT VECTOR MACHINE")
    st.divider()

    # SVM Fish
    st.title('FISH CLASSIFICATION')
    length = st.number_input("Length")
    weight = st.number_input("Weight")
    w_l_ratio = st.number_input("w_l_ratio")
    fish = st.button("Predict Fish")

    if fish:
        with open('Model/svm_fish.pickle', "rb") as r:      # Load model
            svc = pickle.load(r)
        new_data = {
            'length' : [length],
            'weight' : [weight],
            'w_l_ratio' : [w_l_ratio],
        }
        new_data = pd.DataFrame(new_data)
        scaler = StandardScaler()
        scaled_new_data = scaler.fit_transform(new_data)
        new_prediction = svc.predict(new_data)

        if new_prediction[0] == 0 :
            hasil = 'Anabas testudineus'
        elif new_prediction[0] == 1 :
            hasil = 'Coilia dussumieri'
        elif new_prediction[0] == 2 :
            hasil = 'Otolithoides biauritus'
        elif new_prediction[0] == 3 :
            hasil = 'Otolithoides pama'
        elif new_prediction[0] == 4 :
            hasil = 'Pethia conchonius'
        elif new_prediction[0] == 5 :
            hasil = 'Polynemus paradiseus'
        elif new_prediction[0] == 6 :
            hasil = 'Puntius lateristriga'
        elif new_prediction[0] == 7 :
            hasil = 'Setipinna taty'
        elif new_prediction[0] == 8 :
            hasil = 'Sillaginopsis panijus'
        
        st.success('PREDICTION : {}'.format(hasil))
    st.divider()

    # SVM Pumpkin
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
        with open('Model/svm_pumpkin.pickle', "rb") as r:   # Load Model
            svc = pickle.load(r)
        new_data = {											
            'Area' : [Area],
            'Perimeter' : [Perimeter],
            'Major_Axis_Length' : [Major_Axis_Length],
            'Minor_Axis_Length' : [Minor_Axis_Length],
            'Convex_Area' : [Convex_Area],
            'Equiv_Diameter' : [Equiv_Diameter],
            'Eccentricity' : [Eccentricity],
            'Solidity' : [Solidity],
            'Extent' : [Extent],
            'Roundness' : [Roundness],
            'Aspect_Ration' : [Aspect_Ration],
            'Compactness' : [Compactness],
        }
        new_data = pd.DataFrame(new_data)
        scaler = StandardScaler()
        scaled_new_data = scaler.fit_transform(new_data)
        new_prediction = svc.predict(new_data)
        
        if new_prediction[0] == 0 :
            hasil = 'Çerçevelik'
        else:
            hasil = 'Ürgüp Sivrisi'

        st.success('PREDICTION : {}'.format(hasil))
    st.divider()

    # SVM Fruit
    st.title('FRUIT CLASSIFICATION')
    diameter = st.number_input('diameter')
    weight = st.number_input('weight')
    red = st.slider('red', 0, 255)
    green = st.slider('green', 0, 255)
    blue = st.slider('blue', 0, 255)
    fruit = st.button("Predict Fruit")

    if fruit:
        with open('Model/svm_fruit.pickle', "rb") as r: # Load Model
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

    # Perceptron Fish
    st.title('FISH CLASSIFICATION')
    length = st.number_input("Length")
    weight = st.number_input("Weight")
    w_l_ratio = st.number_input("w_l_ratio")
    fish = st.button("Predict Fish")

    if fish:
        with open('Model/perceptron_fish.pickle', "rb") as r:   # Load Model
            perceptron = pickle.load(r)
        new_data = {
            'length' : [length],
            'weight' : [weight],
            'w_l_ratio' : [w_l_ratio],
        }
        new_data = pd.DataFrame(new_data)
        scaler = StandardScaler()
        scaled_new_data = scaler.fit_transform(new_data)
        new_prediction = perceptron.predict(new_data)

        if new_prediction[0] == 0 :
            hasil = 'Anabas testudineus'
        elif new_prediction[0] == 1 :
            hasil = 'Coilia dussumieri'
        elif new_prediction[0] == 2 :
            hasil = 'Otolithoides biauritus'
        elif new_prediction[0] == 3 :
            hasil = 'Otolithoides pama'
        elif new_prediction[0] == 4 :
            hasil = 'Pethia conchonius'
        elif new_prediction[0] == 5 :
            hasil = 'Polynemus paradiseus'
        elif new_prediction[0] == 6 :
            hasil = 'Puntius lateristriga'
        elif new_prediction[0] == 7 :
            hasil = 'Setipinna taty'
        elif new_prediction[0] == 8 :
            hasil = 'Sillaginopsis panijus'
        
        st.success('PREDICTION : {}'.format(hasil))
    st.divider()

    # Perceptron Pumpkin
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
        with open('Model/perceptron_pumpkin.pickle', "rb") as r:    # Load Model
            perceptron = pickle.load(r)
        new_data = {											
            'Area' : [Area],
            'Perimeter' : [Perimeter],
            'Major_Axis_Length' : [Major_Axis_Length],
            'Minor_Axis_Length' : [Minor_Axis_Length],
            'Convex_Area' : [Convex_Area],
            'Equiv_Diameter' : [Equiv_Diameter],
            'Eccentricity' : [Eccentricity],
            'Solidity' : [Solidity],
            'Extent' : [Extent],
            'Roundness' : [Roundness],
            'Aspect_Ration' : [Aspect_Ration],
            'Compactness' : [Compactness],
        }
        new_data = pd.DataFrame(new_data)
        scaler = StandardScaler()
        scaled_new_data = scaler.fit_transform(new_data)
        new_prediction = perceptron.predict(new_data)
        
        if new_prediction[0] == 0 :
            hasil = 'Çerçevelik'
        else:
            hasil = 'Ürgüp Sivrisi'

        st.success('PREDICTION : {}'.format(hasil))
    st.divider()

    # Perceptron Fruit
    st.title('FRUIT CLASSIFICATION')
    diameter = st.number_input('diameter')
    weight = st.number_input('weight')
    red = st.slider('red', 0, 255)
    green = st.slider('green', 0, 255)
    blue = st.slider('blue', 0, 255)
    fruit = st.button("Predict Fruit")
    
    if fruit:
        with open('Model/perceptron_fruit.pickle', "rb") as r:  # Load Model
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

    # Logistic Fish
    st.title('FISH CLASSIFICATION')
    length = st.number_input("Length")
    weight = st.number_input("Weight")
    w_l_ratio = st.number_input("w_l_ratio")
    fish = st.button("Predict Fish")

    if fish:
        with open('Model/logistic_fish.pickle', "rb") as r: # Load Model
            log = pickle.load(r)
        new_data = {
            'length' : [length],
            'weight' : [weight],
            'w_l_ratio' : [w_l_ratio],
        }
        new_data = pd.DataFrame(new_data)
        scaler = StandardScaler()
        scaled_new_data = scaler.fit_transform(new_data)
        new_prediction = log.predict(new_data)

        if new_prediction[0] == 0 :
            hasil = 'Anabas testudineus'
        elif new_prediction[0] == 1 :
            hasil = 'Coilia dussumieri'
        elif new_prediction[0] == 2 :
            hasil = 'Otolithoides biauritus'
        elif new_prediction[0] == 3 :
            hasil = 'Otolithoides pama'
        elif new_prediction[0] == 4 :
            hasil = 'Pethia conchonius'
        elif new_prediction[0] == 5 :
            hasil = 'Polynemus paradiseus'
        elif new_prediction[0] == 6 :
            hasil = 'Puntius lateristriga'
        elif new_prediction[0] == 7 :
            hasil = 'Setipinna taty'
        elif new_prediction[0] == 8 :
            hasil = 'Sillaginopsis panijus'
        
        st.success('PREDICTION : {}'.format(hasil))
    st.divider()

    # Logistic Pumpkin
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
        with open('Model/logistic_pumpkin.pickle', "rb") as r:  # Load Model
            log = pickle.load(r)
        new_data = {											
            'Area' : [Area],
            'Perimeter' : [Perimeter],
            'Major_Axis_Length' : [Major_Axis_Length],
            'Minor_Axis_Length' : [Minor_Axis_Length],
            'Convex_Area' : [Convex_Area],
            'Equiv_Diameter' : [Equiv_Diameter],
            'Eccentricity' : [Eccentricity],
            'Solidity' : [Solidity],
            'Extent' : [Extent],
            'Roundness' : [Roundness],
            'Aspect_Ration' : [Aspect_Ration],
            'Compactness' : [Compactness],
        }
        new_data = pd.DataFrame(new_data)
        scaler = StandardScaler()
        scaled_new_data = scaler.fit_transform(new_data)
        new_prediction = log.predict(new_data)
        
        if new_prediction[0] == 0 :
            hasil = 'Çerçevelik'
        else:
            hasil = 'Ürgüp Sivrisi'

        st.success('PREDICTION : {}'.format(hasil))
    st.divider()

    # Logistic Fruit
    st.title('FRUIT CLASSIFICATION')
    diameter = st.number_input('diameter')
    weight = st.number_input('weight')
    red = st.slider('red', 0, 255)
    green = st.slider('green', 0, 255)
    blue = st.slider('blue', 0, 255)
    fruit = st.button("Predict Fruit")

    if fruit:
        with open('Model/logistic_fruit.pickle', "rb") as r: # Load Model
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

st.write("© 2025 - Ilham Khefi Ramadhanu")
