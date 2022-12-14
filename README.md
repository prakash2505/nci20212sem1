## Prerequisites ##
1. Create an account on MetaMask
<img width="1440" alt="METAMASK" src="https://user-images.githubusercontent.com/114516555/207664244-190dbbae-513f-4b22-9e93-b403723c2912.png">

2. Create a contract on Remix IDE

<img width="1440" alt="compiler" src="https://user-images.githubusercontent.com/114516555/207664297-373e43b8-dce5-455d-a484-382455700a76.png">

3. Get the contract address from Etherscan website

<img width="1440" alt="Screenshot 2022-12-13 at 9 59 50 PM" src="https://user-images.githubusercontent.com/114516555/207664494-a0a8bf4b-e221-4bc4-a54c-b77926602b5c.png">


## Install python on your system via packager or from the web ##

## Install pip3 ##
``` sudo apt install python3-pip```

## Install Web3 ##
``` pip3 install web3 ```

For mac users

``` python3 -m pip install web3 ```


## Install decouple ##
``` pip3 install python-decouple ```

## Create an .env file and import items to it  ##

<img width="1440" alt="ENV" src="https://user-images.githubusercontent.com/114516555/207664675-d9d7dde7-f318-4053-8022-a7cb5e6dfcba.png">
INFURA_URL is the URL we will use to gain access to Infura’s ethereum nodesCONTRACT_ADDRESS is the address of your deployed token smart contractOWNER_ADDRESS is the address you used to deploy the contractSUPER_SECRET_PRIVATE_KEY is your OWNER_ADDRESS private key (from metamask)


## Imports ##


Import web3 and config from decouple and config gives us he .env functionality.

## Set up envronment variables ##


Setup the variables . abi can be found on the etherscan website. refer the following diagram.


## Run the eth_transfer.py file ##

``` python3 eth_transfer.py ```

## Build an Image ##

```docker build --tag [repositoryName]/[imageName]:tagName .```


## Run an image ##

```docker run --name [repositoryName] -p 8090:8080 [imageName]```

## Run the curl command ##

This transfers ETH:

```curl --header "Content-Type: application/json" --request POST --data '{"address":"0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C", "amount":"0.05"}' http://localhost:8090/eth```

This transfers token:

```curl --header "Content-Type: application/json" --request POST --data '{"address":"0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C"}' http://localhost:8090/token```

