from flask import Flask,render_template,redirect,request,session
from web3 import Web3,HTTPProvider
import json

register_contract_address='0x5bd3b7dedf32DE6F36EAC432E81bF38352B41A1a'
rooms_contract_address='0x8a50a1eE77A9984eEeE21FC2B0c4c55715C296Ff'

def connect_with_register(acc):#connecting to the register contract
    blockchain='http://127.0.0.1:7545'
    web3=Web3(HTTPProvider(blockchain))
    if acc==0:
        acc=web3.eth.accounts[0]
    web3.eth.defaultAccount=acc
    artifact_path='../build/contracts/register.json'#loading artifact
    contract_address=register_contract_address
    with open(artifact_path) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']#extracting abi
    contract=web3.eth.contract(address=contract_address,abi=contract_abi)#passing contract address,abi
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

@app.route('/registeruser',methods=['post','get'])#html form sending data to here
def registeruser():
    walletaddr=request.form['walletaddr']
    name=request.form['name']
    email=request.form['email']
    mobile=request.form['mobile']
    password1=request.form['password']
    print(walletaddr,name,email,mobile,password1)
    contract,web3=connect_with_register(0)#connect to blockchain
    hash=contract.functions.registeruser(walletaddr,name,email,mobile,int(password1)).transact()#store details in a block
    web3.eth.waitForTransactionReceipt(hash)#append block to blockchain
    return render_template('Login.html')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)