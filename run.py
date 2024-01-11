import os

if __name__ == '__main__':
    os.system('pytest -vs --alluredir=./temps --clean-alluredir')
    os.system('allure generate ./temps -o ./reports --clean')