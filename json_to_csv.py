import json 
import pandas  as pd 
import glob
import os
path_to_json = 'data/test.json'
#path_to_folder = 'data/'
path_to_folder = 'data/ecp/labels/train/'

path_to_objectdection = '../object_detection/data/ECP/day/labels/val/'




# f = open(path)
# data = json.load(f)
# height, width = data['imageheight'], data['imagewidth']
# value = []
# for i in data['children']:
    
#     name = i["identity"]
#     x0 = i["x0"]
#     y0 = i["y0"]
#     x1 = i["x1"]
#     y1 = i["y1"]
    
#     # print(f"{height},{width},{name},{x0},{y0},{x1},{y1}: {tags}")
#     value.append([height, width, name, x0, y0, x1, y1])
    
# column_name = ['height', 'width', 'class', 'x0', 'y0', 'x1', 'y1']
# json_df = pd.DataFrame(value, columns=column_name)
# print(json_df)





def json_to_df(path):  
    f = open(path)
    data = json.load(f)
    height, width = data['imageheight'], data['imagewidth']
    value = []
    for i in data['children']:  
        name = i["identity"]
        x0 = i["x0"]
        y0 = i["y0"]
        x1 = i["x1"]
        y1 = i["y1"]
        value.append([path, height, width, name, x0, y0, x1, y1])
    column_name = ['filename','height', 'width', 'class', 'x0', 'y0', 'x1', 'y1']
    return pd.DataFrame(value, columns=column_name)
# df1 = json_to_df(path_to_json)
# print(df1.shape)


def df_to_csv(path):  
    # sourcery skip: for-append-to-extend, identity-comprehension, list-comprehension, simplify-generator
    #  get file list 
    file_list = []
    final_df = pd.DataFrame()
    for files in glob.glob(path + '*.json'):
        file_list.append(files)
        # print(files)
        #final_df = final_df.append(json_to_df(files), ignore_index=True)
        final_df = pd.concat([final_df, json_to_df(files)], ignore_index=True)
    # print(file_list)
    print(final_df)
 
#df_to_csv(path_to_folder)   



class JasonToCsv:
    def __init__(self):
        pass
    
    def json_to_df(self,path):
        f = open(path)
        data = json.load(f)
        height, width = data['imageheight'], data['imagewidth']
        value = []
        for i in data['children']:
            name = i["identity"]
            x0 = i["x0"]
            y0 = i["y0"]
            x1 = i["x1"]
            y1 = i["y1"]
            value.append([path, height, width, name, x0, y0, x1, y1])
        column_name = ['filename','height', 'width', 'class', 'x0', 'y0', 'x1', 'y1']
        json_df = pd.DataFrame(value, columns=column_name)
        print(json_df.shape)
        return json_df
    
    def mutiple_json_to_df(self, path):
        file_list = []
        final_df = pd.DataFrame()
        for files in glob.glob(path + '*.json', recursive=True):
            file_list.append(files)
            final_df = pd.concat([final_df, self.json_to_df(files)], ignore_index=True)
        print(final_df.shape)
        return final_df
    
    def edit_filename_column(self, dataframe):
        dataframe['filename'] = dataframe['filename'].str.replace('.json', '.png', regex=True)
        dataframe['filename'] = dataframe['filename'].str.split('/').str[-1]
        return dataframe
    
    def change_dtype_of_columns(self, dataframe):
        # dataframe['class'] = dataframe['class'].astype('str')
        dataframe['height'] = dataframe['height'].astype('int')
        dataframe['width'] = dataframe['width'].astype('int')
        dataframe['xmin'] = dataframe['x0'].astype('int')
        dataframe['ymin'] = dataframe['y0'].astype('int')
        dataframe['xmax'] = dataframe['x1'].astype('int')
        dataframe['ymax'] = dataframe['y1'].astype('int')
        return dataframe
    
    def save_to_csv(self, in_json, out_csv):
        df = self.mutiple_json_to_df(in_json)
        df = self.edit_filename_column(df)
        print(df.head())
        #print(df.dtypes)
        df = self.change_dtype_of_columns(df)
        final_columns = ['filename', 'height', 'width', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
        final_df = df[final_columns]
        print(final_df.dtypes)
        final_df.to_csv(out_csv, index=False)
        print('saved')

cv = JasonToCsv()
df = cv.mutiple_json_to_df(path_to_folder)
cv.save_to_csv(path_to_folder, 'data/train.csv')

# print(df)
# print(df.dtypes)