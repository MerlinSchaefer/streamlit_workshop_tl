##imports
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

##read in data
## ATTENTION, you might have to specify your path first
diamonds = pd.read_csv("diamonds.csv", index_col=0)
housing = pd.read_csv("housing.csv", usecols=[0,1]) #we just want latitude and longitude from this dataset (the first two columns)

### Displaying text
##How to write things 
st.title("My first streamlit project")

st.write("this is a very long line of code and it becomes kinda unreadable at some point, let's try to avoid that and make our lives either with triple quotes")

##multiline writing/markdown

#TRY IT YOURSELF
#use the appropriate streamlit function and triple-quotes to write across multiple lines and in markdown style
#create a first order header and a second order header

st.write("**bold text ** *italics text*")


###Displaying data

##displaying a dataframe
st.dataframe(diamonds)

##add column selector
col_names = diamonds.columns.tolist()
col_select = st.multiselect("Columns",col_names, default = col_names)

#TRY IT YOURSELF
#display the dataframe again but with only the columns that the user selects through the Columns selector above.



###Plotting

##display figures
fig,ax = plt.subplots() #must create a subplot
ax = sns.barplot(x = diamonds["cut"].unique(), y = diamonds["cut"].value_counts())
st.pyplot(fig)

#TRY IT YOURSELF 
#display the two columns (latitude, longitude) from the housing dataframe as a scatterplot



##display map data
st.map(housing, zoom = 4.5)

###Machine Learning
ml_model = pickle.load(open("model.pkl", "rb")) #load model

##create the sidebar
st.sidebar.header("User Input Parameters")

##create function for user input
#Inputs:carat,x,y,z ; prediction price
def get_user_input():
    carat = st.sidebar.slider("carat",
                              diamonds["carat"].min(),
                              diamonds["carat"].max(),
                              diamonds["carat"].mean())
    x = st.sidebar.slider("x",
                          diamonds["x"].min(),
                          diamonds["x"].max(),
                          diamonds["x"].mean())
    y = st.sidebar.slider("y",
                          diamonds["y"].min(),
                          diamonds["y"].max(),
                          diamonds["y"].mean())
    z = st.sidebar.slider("z",
                          diamonds["z"].min(),
                          diamonds["z"].max(),
                          diamonds["z"].mean())
    features = pd.DataFrame({"carat":carat,
                             "x":x,"y":y,"z":z}, index = [0])
    return features

input_df = get_user_input() #get user input from sidebar

prediction = ml_model.predict(input_df)#get predicitions

st.subheader("Prediction")
st.write("Your diamond is worth: $",prediction[0], )

#image upload?

#image classification?