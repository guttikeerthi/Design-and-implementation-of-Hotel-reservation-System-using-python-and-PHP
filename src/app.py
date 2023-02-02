from flask import Flask,render_template,redirect,request,session
from web3 import Web3,HTTPProvider
import json

register_contract_address=''
rooms_contract_address=''

def connect_with_register(acc):
    blockchain='http://127.0.0.1:7545'
    web3=Web3(HTTPProvider(blockchain))
    if acc==0:
        acc=web3.eth.accounts[0]
    web3.eth.defaultAccount=acc
    artifact_path='../build/contracts/register.json'
    contract_address=register_contract_address
    with open(artifact_path) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']
    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
    return(contract,web3)


app=Flask(__name__)
app.secret_key='a15sacet'

@app.route('/')
def homepage():
    return render_template('Home.html')

@app.route('/Registration')
def registrationpage():
    return render_template('Registration.html')

@app.route('/Login')
def loginpage():
    return render_template('Login.html')

@app.route('/registeruser',methods=['post','get'])
def registeruser():
    walletaddr=request.form['walletaddr']
    name=request.form['name']
    email=request.form['email']
    mobile=request.form['mobile']
    password1=request.form['password']
    print(walletaddr,name,email,mobile,password1)
    contract,web3=connect_with_register(0)
    hash=contract.functions.registeruser(walletaddr,name,email,mobile,int(password1)).transact()
    web3.eth.waitForTransactionReceipt(hash)
    return render_template('Login.html')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)