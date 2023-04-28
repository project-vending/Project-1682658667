 
import os

# define project directory structure
model_dir = 'model'
data_dir = 'data'
output_dir = 'output'

# define model subdirectories
als_dir = os.path.join(model_dir, 'als_model')
als_output_dir = os.path.join(output_dir, 'als_recommendations')

# create directories
os.makedirs(model_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)
os.makedirs(als_dir, exist_ok=True)
os.makedirs(als_output_dir, exist_ok=True)

# create empty files
open(os.path.join(data_dir, 'product_data.csv'), 'a').close()
open(os.path.join(data_dir, 'user_data.csv'), 'a').close()
open(os.path.join(data_dir, 'purchase_data.csv'), 'a').close()
open(os.path.join(als_output_dir, 'recommendations.csv'), 'a').close()

print('File structure and empty files created successfully.')
