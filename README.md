# <p align = "center"> Features </p>

### <p align = "center">1. Upload Bulk Data </p>
![image](https://github.com/anshumannandan/Fastt/assets/93365821/0d53f5e4-be0f-4d11-9c9d-2d2a5379deeb)

### <p align = "center">2. Get all data from database </p>
![image](https://github.com/anshumannandan/Fastt/assets/93365821/7a3379d1-d7d3-4a71-96c0-20f9ddb368b9)

## How to setup the project on your local server?

1. Clone the repository:

```CMD
git clone https://github.com/anshumannandan/Fastt
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Navigate to the project directory: 

```CMD
cd Fastt
```

3. Install & Create a virtual environment:

```CMD
pip install virtualenv
virtualenv venv
```

4. Activate the virtual environment:
```CMD
venv/scripts/activate
```

5. Install the dependencies: 

```CMD
pip install -r requirements.txt
```

6. Navigate to main directory
```CMD
cd project
```

7. Run the backend server on localhost:

```CMD
uvicorn app.main:app --reload
```

You can access the endpoints from your web browser following this url:
```url
http://127.0.0.1:8000
```
