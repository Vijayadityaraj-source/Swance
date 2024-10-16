# Swance
- Used inswapper and gfpgan models to swap and enhance faces in the images.
- These models need to be downloaded by the user when running this repo and added to data/models folder in the Backend

  #### Models

  1. [GFPGANv1.4](https://huggingface.co/hacksider/deep-live-cam/resolve/main/GFPGANv1.4.pth)
  2. [inswapper_128_fp16.onnx](https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128.onnx) (Note: Use this [replacement version](https://github.com/facefusion/facefusion-assets/releases/download/models/inswapper_128.onnx) if you encounter issues)

  Place these files in the "data/models" folder.

### Example : 
  
  Source : 

  <img src="https://github.com/user-attachments/assets/25fdd411-1723-42d3-a4e3-7615da92fe79" alt="leo" width="300">

  Target : 

  <img src="https://github.com/user-attachments/assets/950d0d18-61f3-45e9-896e-ca1603fcab45" alt="leo" width="300">

  Output : 
  
  <img src="https://github.com/user-attachments/assets/90eabed8-f016-4f8c-9555-18acfceb1da3" alt="leo" width="300">

UI :

  <img src="https://github.com/user-attachments/assets/1aa2caab-0556-45f2-9ac7-188e2b82df6a" alt="UI" width="1000">

## How to run locally : 
### Backend
- Clone the repo : `git clone https://github.com/Vijayadityaraj-source/Swance.git`
- Go to backend : `cd BackEnd`
- Create a virtual enviornment : `python -m venv myenv`
- Activate the venv :
  
  Windows : `myenv\Scripts\activate`
  
  Mac/Linux : `source myenv/bin/activate`

- Install packages : `pip install -r requirements.txt`

  Note : You might need to install c++ dev tools as it is required for the insightface package to run.

- Run Backend : `python app\main.py`

  Backend will start running on  `127.0.0.1:8080`

### Frontend
-  Just run the html bruh.
