# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:51:51 2023

@author: GILAD, SHAHAR
"""

import pandas as pd
import numpy as np
import os


df=pd.read_csv('generated_with_buying_index.csv')
MAX_LISTS=49
def list_of_products():
    """
    


    Returns
    -------
    dict
        DICT WITH PRODUCTS AS KEY AND 0 AS VALUE
        AND METADTA OF DATE. DATE VALUE IS NUMBER OF DAYS PASSED SINCE LAST PURCHASE

    """
    my_dict=dict.fromkeys(df.iloc[:0,2:-1].columns.values.tolist())
    for key, value in my_dict.items():
        if value is None:
            my_dict[key] = 0
    return my_dict



def amount_of_lists(given_id):
    """
    

    Parameters
    ----------
    id : int
        COSTUMER'S SYSTEM IDENTEFIER.

    Returns
    -------
    int
        AMOUNT OF LISTS BELONG TO THIS COSTUMER.

    """
    return df[df.id==given_id].id.shape[0]



def add_list(given_id,given_dict):
        """
    

    Parameters
    ----------
    given_id : int
        costumer's id
    given_dict : dict. size= 168
        only list of products. and date as time from last purchase

    Raises
    ------
    ValueError
        ID must be smaller then 1000 and greater then 5000


    """
        if given_id>999 and given_id < 5001:
            raise ValueError ("id must be between 0 to 999 or 5001 to inf")
        buying_index=generate_byuing_index(given_id)
        
        #add given_list meta data
        given_dict['Buying_index']=buying_index
        given_dict['id']=given_id
        
        if(buying_index==MAX_LISTS):
            df.drop(df[(df.id==given_id) & (df.Buying_index==0)].index,inplace=True)
            df.loc[df["id"]==given_id,"Buying_index"]-=1
        
        given_df=pd.Series(given_dict)
        given_df.fillna(0,inplace=True)
        df.loc[len(df)+1]=given_df
        
        
        df.iloc[len(df)+1,1:]=given_df
            
            
                
def predict_list(given_id,time_from_last_buy):
        """
    

    Parameters
    ----------
    given_id : int
        costumers id
    time_from_last_buy : int
        days passed since last purchse of costumer

    Returns
    -------
    TYPE: dict
        dict like {index -> {column -> value}}

    """
        cur_df_trn_meta_data=df[df.date==time_from_last_buy].iloc[:,[2,-1]]

        # filter out the first buying of every costumer  in the df_trn_meta_data (buying index 0)
        cur_df_trn_meta_data=cur_df_trn_meta_data[cur_df_trn_meta_data.Buying_index>0]
      
        #changes all buying index to n-1
        cur_df_trn_meta_data.Buying_index=cur_df_trn_meta_data.Buying_index-1
      
        #cur_df_train will hold the n-1 shopping list of each costumer matched
        cur_df_trn=df.iloc[cur_df_trn_meta_data.index-1,:]
      
        # turn cur_df_rtn to matrix 
        cur_df_mat=df_to_mat(cur_df_trn,[3,170])
      
        #cur_vec= last list of the given_id costumer
        cur_vec=df[df.id==given_id].tail(2).head(1).to_numpy().squeeze()[3:170]
      
        #calc everage distance between examined shopping list to all the lists in cur_df_mat
        dist=np.mean(np.abs(cur_df_mat-cur_vec),axis=1)
      
        #find closest neigbour (knn= 1 nearest neighbour)
        minimal_dist_index=np.argmin(dist)
      
        #closest_subj= id,buying_index of the closest list
        closest_subject=cur_df_trn.iloc[minimal_dist_index,[1,-1]]
      
        #prediction= next purchase of the nearest nighbour found
        predicted_list=df[(df.id==closest_subject[0])&(df.Buying_index==closest_subject[1]+1)]
      
        return predicted_list.iloc[:,2:170].to_dict('index')





#####################  DOMESTIC FUNCTIONS #################

def generate_byuing_index(given_id):
    lists_exist=amount_of_lists(given_id)
    
    #dec by 1 to match it to the Buying_index column
    lists_exist-=1
    
    if lists_exist<49 and lists_exist>0:
        buying_index=df.Buying_index[df.id==given_id].max()+1
        
        # lists_exist=1 means there is 0 lists to that id
    elif lists_exist==-1:
        buying_index=0
        
        #lists_exist=49 means there is 50 lists. the new list will get buying_index 49
    elif lists_exist==49:
        buying_index=49
    return buying_index

def df_to_mat(df,col_index):
    #transfer to matrix
    mat=df.iloc[:,col_index[0]:col_index[1]].to_numpy()
    return mat


    
    
    
    
    
    