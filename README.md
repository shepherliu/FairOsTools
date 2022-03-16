# FairOsTools
a python lib and tool for FairOs

How to Run it On Local?

1. make sure that your system has installed git, docker and python3. Linux or macos is recommend.

2. run the fairos server.
	
	download the fairos server docker-compose.yml
	
		wget https://github.com/fairDataSociety/fairOS-dfs/raw/master/docker/testnet-new/docker-compose.yml
	
	modify the docker-compose.yml
		
		change "--postageBlockId" to you postage stamp
	
		change --cookieDomain "fairos1.fairdatasociety.org" to your domain, add CORS domains to --cors-origins
		
		change BEE_SWAP_ENDPOINT to your own infura swap-endpoint
	
	start it in background: 
		
		docker-compose up -d
	
	You can see logs with command:
	
		docker logs fairstack_fairos_1 -f
		docker logs fairstack_bee-1_1 -f
	
	get you ethereum address from the bee logs and facuet your address with little gBzz and gETH.

3. clone the project the the local.

    	git clone https://github.com/shepherliu/FairOsTools.git

4. change to the project dir

    	cd FairOsTools

5. install FairOsTools libs
    
    	python3 setup.py install
    
6. use the libs like this:
  
	    from fairos.fairos import Fairos
	    from fairos.fairos import test

	    #run the default test case
	    test()

	    fs = Fairos('http://localhost:9090')

		  fs.signup_user('test', 'test')

		  fs.login_user('test', 'test')

		  res = fs.user_stat()
		  print(res)

		  res = fs.new_pod('mypod')
		  print(res)
		  
7. for a quick start, you can use the offical fairos test server https://fairos.fairdatasociety.org/ if you have already registered an account at https://app.fairdrive.fairdatasociety.org/ (beause the offical fairos test server's register function is not avaiable now ).
	
	
	
How it Works?

  1. see the fairos api documents at: https://docs.fairos.fairdatasociety.org/
