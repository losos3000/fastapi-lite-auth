# FastAPI Simple Auth
This is a login/password authentication module that can be quickly and easily integrated into your project.
It is recommended to use the module in small projects and pet projects.

To add the module to your project, you need to:

1. Install the module
2. Override the `get_user` method in `auth_manager`
3. Override the user schema and model in `auth_manager` if they differ from yours
4. Specify which fields in the user model represent the login and password 

More detailed installation and configuration instructions can be found in the `Installation` section.

Based on [AuthX](https://github.com/yezz123/authx)

## Installation


## Requirements
```shell
pip install -r requirements.txt
```
or
```shell
pip install "fastapi[standard]"
pip install authx 
```

## Start Example
### API
```shell
python3 -m example.api.main
```