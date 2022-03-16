# FairOsTools
a python lib and tool for FairOs

How to Run it On Local?

1. make sure that your system has installed git and python3. Linux or macos is recommend.

2. run the fairos server.

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

	
