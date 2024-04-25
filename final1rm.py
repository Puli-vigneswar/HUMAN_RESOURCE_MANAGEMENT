
import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os 

#extracting the dataframes
dist_total =pd.read_csv("D:/new_total_NIC_dist.csv")
retail=pd.read_csv("D:/retail.csv")
sales=pd.read_csv("D:/sales.csv")
manufactures=pd.read_csv("D:/manufactures.csv")
crops=pd.read_csv("D:/crops.csv")

alldfs=pd.concat([retail,sales,manufactures,crops],ignore_index=True)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Assuming 'dist_total' DataFrame is already defined and loaded with data
# If not, you need to load it from a CSV or other data source

# Load the 'statetocode.csv' file into a DataFrame
try:
    sttocode = pd.read_csv("D:/statetocode.csv")
except FileNotFoundError:
    print("Error: 'statetocode.csv' file not found. Please provide the correct path.")

# Function to get the DataFrame based on the State_Code
def get_df(selcode):
    df = dist_total[dist_total["State_Code"] == selcode]
    return df

# Function to plot the statistics
def plot_statistics(df):
    df1 = df[["district", "main_total_persons", "marginal_total_persons"]]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="district", y="main_total_persons", data=df1, color='blue', label="main_total_persons")
    sns.barplot(x='district', y="marginal_total_persons", data=df1, label="marginal_total_persons")
    plt.xlabel("Districts")
    plt.ylabel("Workers Statistics")
    plt.title("Main vs Marginal Total Fields Performance")
    plt.xticks(rotation=90) 
    st.pyplot(fig)

 # Function to plot the statistics
def lineplotmw(df):
        df1 = df[["district", "main_total_male", "main_total_female"]]
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.plot(df1["district"], df1["main_total_male"], label='main_total_male', marker='o')
        plt.plot(df1["district"], df1["main_total_female"], label='main_total_female', marker='*')
        plt.xlabel("Districts")
        plt.ylabel("Workers Statistics")
        plt.title("Men vs women Total fields statistics")
        plt.legend()
        plt.xticks(rotation=90) 
        st.pyplot(fig)

def lineplotmwurban(df):
        df1 = df[["district", "main_URBAN_male", "main_URBAN_female"]]
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.plot(df1["district"], df1["main_URBAN_male"], label='main_URBAN_male', marker='o')
        plt.plot(df1["district"], df1["main_URBAN_female"], label='main_URBAN_female', marker='*')
        plt.xlabel("Districts")
        plt.ylabel("Workers Statistics")
        plt.title("Men vs women Total urban statistics")
        plt.legend()
        plt.xticks(rotation=90) 
        st.pyplot(fig)
def lineplotmwrural(df):
        df1 = df[["district", "main_RURAL_male", "main_RURAL_female"]]
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.plot(df1["district"], df1["main_RURAL_male"], label='main_RURAL_male', marker='*')
        plt.plot(df1["district"], df1["main_RURAL_female"], label='main_RURAL_female', marker='+')
        plt.xlabel("Districts")
        plt.ylabel("Workers Statistics")
        plt.title("Men vs women Total urban statistics")
        plt.legend()
        plt.xticks(rotation=90) 
        st.pyplot(fig)

# Function to plot the statistics
def plot_statistics_rural(df):
    df1 = df[["district", "main_RURAL_persons", "marginal_rural_persons"]]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="district", y="main_RURAL_persons", data=df1, color='red', label="main_RURAL_persons")
    sns.barplot(x='district', y="marginal_rural_persons", data=df1,color='yellow', label="marginal_rural_persons")
    plt.xlabel("Districts")
    plt.ylabel("Workers Statistics")
    plt.title("Main vs Marginal Total  rural Fields Performance")
    plt.xticks(rotation=90) 
    st.pyplot(fig)
def plot_statistics_urban(df):
    df1 = df[["district", "main_URBAN_persons", "marginal_urban_persons"]]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="district", y="main_URBAN_persons", data=df1, color='orange', label="main_URBAN_persons")
    sns.barplot(x='district', y="marginal_urban_persons", data=df1,color='green', label="marginal_urban_persons")
    plt.xlabel("Districts")
    plt.ylabel("Workers Statistics")
    plt.title("Main vs Marginal Total  Urban Fields Performance")
    plt.xticks(rotation=90) 
    st.pyplot(fig)
def cluster1plotmw(df):
        df1 = df[["NIC_NAME", "main_total_persons", "marginal_total_persons"]]
        fig , ax = plt.subplots(figsize=(12, 8))
    
        # Set the figure size
        # Create line plots for males and females
        plt.plot(df['NIC_NAME'], df['main_total_persons'], marker='*', label='main_total_persons')
        plt.plot(df['NIC_NAME'], df['marginal_total_persons'], marker='o', label='marginal_total_persons')

        # Add labels and title
        plt.xlabel('OCCUPATION')
        plt.ylabel('workers')
        plt.title('marginal_total_persons')
        plt.legend()
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=90)
        st.pyplot(fig)
def cluster1plotrural(df):
        df1 = df[["NIC_NAME", "main_RURAL_persons", "marginal_rural_persons"]]
        fig , ax = plt.subplots(figsize=(12, 8))
    
        # Set the figure size
        # Create line plots for males and females
        plt.plot(df['NIC_NAME'], df['main_RURAL_persons'], marker='o', label='main_RURAL_persons')
        plt.plot(df['NIC_NAME'], df['marginal_rural_persons'], marker='.', label='marginal_rural_persons')

        # Add labels and title
        plt.xlabel('OCCUPATION')
        plt.ylabel('workers')
        plt.title('RURAL INFO of main and marginal workers')
        plt.legend()
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=90)
        st.pyplot(fig)
def clusterurban(df):
    df1 = df[["NIC_NAME", "main_URBAN_persons", "marginal_urban_persons"]]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="NIC_NAME", y="main_URBAN_persons", data=df1, color='orange', label="main_URBAN_persons")
    sns.barplot(x='NIC_NAME', y="marginal_urban_persons", data=df1,color='green', label="marginal_urban_persons")
    plt.xlabel("occupations")
    plt.ylabel("Workers Statistics")
    plt.title("Main vs Marginal Total  Urban Fields Performance")
    plt.xticks(rotation=90) 
    st.pyplot(fig) 
def clustergender(df):
    df1 = df[["NIC_NAME", "main_RURAL_male", "main_RURAL_female"]]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="NIC_NAME", y="main_RURAL_male", data=df1, color='orange', label="main_RURAL_male")
    sns.barplot(x='NIC_NAME', y="main_RURAL_female", data=df1,color='green', label="main_RURAL_female")
    plt.xlabel("occupations")
    plt.ylabel("Workers Statistics")
    plt.title("RURAL AREA GENDER BASED PLOT")
    plt.xticks(rotation=90) 
    st.pyplot(fig) 

def clustergenderurb(df):
    df1 = df[["NIC_NAME", "main_URBAN_male", "main_URBAN_female"]]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="NIC_NAME", y="main_URBAN_male", data=df1, color='blue', label="main_URBAN_male")
    sns.barplot(x='NIC_NAME', y="main_URBAN_female", data=df1,color='green', label="main_URBAN_female")
    plt.xlabel("occupations")
    plt.ylabel("Workers Statistics")
    plt.title("URBAN AREA GENDER BASED PLOT")
    plt.xticks(rotation=90) 
    st.pyplot(fig) 
    
def que1():
    max_rows = alldfs[alldfs['main_total_persons'] == alldfs['main_total_persons'].max()]
    m=max_rows
    st.dataframe(m[["State_Code","district_name","Division","NIC_NAME","main_total_persons","main_total_male","main_total_female"]])
        
def que2():
    maxmar=alldfs[alldfs["marginal_total_persons"]==alldfs["marginal_total_persons"].max()]
    mar=maxmar 
    st.dataframe(mar[["State_Code","district_name","Division","marginal_total_persons","marginal_total_male","marginal_total_female","NIC_NAME"]])
        
def que3():
    maxmar=alldfs[alldfs["main_RURAL_persons"]==alldfs["main_RURAL_persons"].max()]
    mar=maxmar 
    st.dataframe(mar[["State_Code","district_name","Division","main_RURAL_persons","main_RURAL_male","main_RURAL_female","NIC_NAME"]])

def que4():
    maxwm=alldfs[alldfs["main_total_female"]==alldfs["main_total_female"].max()]
    mar=maxwm 
    st.dataframe(mar[["State_Code","district_name","Division","main_total_female","main_total_persons","main_total_male","NIC_NAME"]])

def que5():
    k=alldfs[["NIC_NAME","main_total_persons"]]
    o=k[k["main_total_persons"]==k["main_total_persons"].max()]
    
    st.write(o)
    
def que6():
    men=alldfs["main_total_persons"].mean()
    st.write(men)
    
def que7():
    men=alldfs["marginal_total_persons"].mean()
    st.write(men) 
def que8():
    m=alldfs.query('main_total_female > main_total_male')
    j=m.head(10)
    st.dataframe(j[["State_Code","district_name","Division","main_total_female","main_total_male"]])
def que9():
    m=alldfs.query('marginal_total_persons > main_total_persons')
    j=m.head(10)
    st.dataframe(j[["State_Code","district_name","Division","marginal_total_persons","main_total_persons"]])
    
    
def que10():
    maxwm=alldfs[alldfs["main_total_male"]==alldfs["main_total_male"].max()]
    mar=maxwm 
    st.dataframe(mar[["State_Code","district_name","Division","main_total_female","main_total_persons","main_total_male","NIC_NAME"]])
    

        
    
        
st.title(':rainbow[HUMAN RESOURCE MANAGEMENT]')

# CreatING tab titles
tab_titles = ['HOME', 'EXPLORE CHARTS', 'INDUSTRIES',"FACTS"]

# Create the tabs
tab1, tab2, tab3,tab4 = st.tabs(tab_titles)

# Add content to each tab
with tab1:
    st.header('OVERVIEW OF THE APPLICATION')
    st.markdown(':purple[This is a dashboard of exploring the human resource management regarding the various fiels ]')
    st.markdown("To explore the data in a convinient manner")
    st.markdown("Which helps to understand the trend of the occupations")
    st.markdown("In multiple areas also helps the officials to understand the data of 23 states and more")
    st.markdown("**********")
    st.markdown(":green[-----Skills take away-----]")
    
    st.markdown(":grey[NATURAL LANGUAGE PROCESSING]")
    st.write(":grey[EXPLORATORY DATA ANALYSIS]")
    st.write(":grey[OS]")
    st.write(":grey[PYTHON SCRIPTING]")
    st.write(":grey[STREAMLIT]")
    st.markdown("*******")
with tab2:
    st.subheader(":yellow[EXPLORE THE CHARTS RELATED TO SPECIFIED FIELDS]")
    states = sttocode["state_ut"].tolist()
    # select box 
    selstate = st.selectbox("Select district to view total occupations", states)
    try:
        selcode = sttocode.loc[sttocode["state_ut"] == selstate, 'State_Code'].values[0]
    except IndexError:
        print(f"Error: State code not found for '{selstate}'. Please check the data in 'statetocode.csv'.")

    if selcode is not None:
        df = get_df(selcode)
        plot_statistics(df) 
        
    st.write("explore the gender based data")
    states = sttocode["state_ut"].tolist()
    
    try:
        selcode = sttocode.loc[sttocode["state_ut"] == selstate, 'State_Code'].values[0]
    except IndexError:
        print(f"Error: State code not found for '{selstate}'. Please check the data in 'statetocode.csv'.")

        
    def get_df(selcode):
        df = dist_total[dist_total["State_Code"] == selcode]
        return df


    if selcode is not None:
        df1=get_df(selcode)
        lineplotmw(df1)
    
    st.write("this is the rural workers statistics")
    if selcode is not None:
        df=get_df(selcode) 
        plot_statistics_rural(df)
    st.write("urban workers statics main and marginal")
    if selcode is not None:
        df=get_df(selcode) 
        plot_statistics_urban(df)
    st.write("urban workers gender wise plot ")
    if selcode is not None:
        df=get_df(selcode)
        lineplotmwurban(df)
    st.write("rural workers gender based plot")
    if selcode is not None:
        df=get_df(selcode)
        lineplotmwrural(df)
    
    
    st.markdown("******")

with tab3:
    st.subheader("This is a Graphical representation of charts which  related to various fields and industries")
    optedind=st.radio("Select your fields:", ["AGRICULTURE","RETAIL", "MANUFACTURE", "POULTRY"])
    if optedind=="AGRICULTURE":
        st.write("this is the representation of data of various fields")
        statesg = sttocode["state_ut"].tolist()
        optstate = st.selectbox("Select a state ", statesg)
        
        try:
            optstcode = sttocode.loc[sttocode["state_ut"] == optstate, 'State_Code'].values[0]
        except IndexError:
            print(f"Error: State code not found for '{selstate}'. Please check the data in 'statetocode.csv'.")

        
        r=crops[crops["State_Code"]==optstcode]
        lst=r.district_name.unique()
        dist=st.selectbox("select district",lst)
        dre=r[r["district_name"]==dist]
        divl=dre.Division.unique()
        divr=st.selectbox("select division",divl)
        divref=dre[dre["Division"]==divr]
        cluster1plotmw(divref)
        if st.button("explore rural workers info"):
            cluster1plotrural(divref)
        if st.button("explore urban workers"):
            clusterurban(divref)
        if st.button("rural area wise gender plot"):
            clustergender(divref)
        if st.button("urban area wise gender plot"):
            clustergenderurb(divref)
            
    elif optedind=="MANUFACTURE":
        st.write("this is the representation of data of various fields")
        statesg = sttocode["state_ut"].tolist()
        optstate = st.selectbox("Select a state ", statesg)
        try:
            optstcode = sttocode.loc[sttocode["state_ut"] == optstate, 'State_Code'].values[0]
        except IndexError:
            print(f"Error: State code not found for '{selstate}'. Please check the data in 'statetocode.csv'.")
        optstcode
        r=manufactures[manufactures["State_Code"]==optstcode]
        lst=r.district_name.unique()
        dist=st.selectbox("select district",lst)
        dre=r[r["district_name"]==dist]
        divl=dre.Division.unique()
        divr=st.selectbox("select division",divl)
        divref=dre[dre["Division"]==divr]
        cluster1plotmw(divref)
        if st.button("explore rural workers info"):
            cluster1plotrural(divref)
        if st.button("explore urban workers"):
            clusterurban(divref)
        if st.button("rural area wise gender plot"):
            clustergender(divref)
        if st.button("urban area wise gender plot"):
            clustergenderurb(divref)
    elif optedind=="RETAIL":
        st.write("this is the representation of data of various fields")
        statesg = sttocode["state_ut"].tolist()
        optstate = st.selectbox("Select a state ", statesg)
        try:
            optstcode = sttocode.loc[sttocode["state_ut"] == optstate, 'State_Code'].values[0]
        except IndexError:
            print(f"Error: State code not found for '{selstate}'. Please check the data in 'statetocode.csv'.")
        optstcode
        retail
        r=retail[retail["State_Code"]==optstcode]
        lst=r.district_name.unique()
        dist=st.selectbox("select district",lst)
        dre=r[r["district_name"]==dist]
        divl=dre.Division.unique()
        divr=st.selectbox("select division",divl)
        divref=dre[dre["Division"]==divr]
        cluster1plotmw(divref)
        
        if st.button("explore rural workers info"):
            cluster1plotrural(divref)
        if st.button("explore urban workers"):
            clusterurban(divref)
        if st.button("rural area wise gender plot"):
            clustergender(divref)
        if st.button("urban area wise gender plot"):
            clustergenderurb(divref)
    elif optedind=="POULTRY":
        st.write("this is the representation of data of various fields")
        statesg = sttocode["state_ut"].tolist()
        optstate = st.selectbox("Select a state ", statesg)
        try:
            optstcode = sttocode.loc[sttocode["state_ut"] == optstate, 'State_Code'].values[0]
        except IndexError:
            print(f"Error: State code not found for '{selstate}'. Please check the data in 'statetocode.csv'.")
        
        
        r=sales[sales["State_Code"]==optstcode]
        lst=r.district_name.unique()
        dist=st.selectbox("select district",lst)
        dre=r[r["district_name"]==dist]
        divl=dre.Division.unique()
        divr=st.selectbox("select division",divl)
        divref=dre[dre["Division"]==divr]
        cluster1plotmw(divref)
        
        if st.button("explore rural workers info"):
            cluster1plotrural(divref)
        if st.button("explore urban workers"):
            clusterurban(divref)
        
        if st.button("rural area wise gender plot"):
            clustergender(divref)
            
        if st.button("urban area wise gender plot"):
            clustergenderurb(divref)
        
        st.markdown("******")
with tab4:
    st.header(':rainbow[some of the facts related to the datagiven below ]')
    boxed=st.selectbox("select a fact to check:",("1.maximum  main workers in statistics",
                       "2.maximum marginal workers",
                       "3.maximum main rural workers",
                       "4.maximum womens in total area wise",
                       "5.maximum workers in an occupation",
                       "6.avg workers count in main workers",
                       "7.avg workers count in marginal workers",
                       "8.women greater than men workers",
                       "9.marginal workers greater than the main workers",
                       "10.maximum men workers"))
    if boxed=="1.maximum  main workers in statistics":
        que1()
    if boxed=="2.maximum marginal workers":
        que2()
    if boxed=="3.maximum main rural workers":
        que3()
    if boxed=="4.maximum womens in total area wise":
        que4()
    if boxed=="5.maximum workers in an occupation":
        que5() 
    if boxed=="6.avg workers count in main workers":
        que6()
    if boxed=="7.avg workers count in marginal workers":
        que7()
    
    if boxed=="8.women greater than men workers":
        que8()
        
    if boxed=="9.marginal workers greater than the main workers":
        que9()
        
    if boxed=="10.maximum men workers":
        que10()
        
        
    st.markdown("*****")