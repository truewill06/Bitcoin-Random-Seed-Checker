from distutils.core import setup
setup(
  name = 'check-random-wallet',         
  packages = ['check-random-wallet'],   
  version = '0.1',     
  license='MIT',       
  description = 'CHECKS RANDOM WALLETS USING SEED.',   
  author = 'PETER POPE',                   
  author_email = 'truewill06@gmail.com',      
  url = 'https://github.com/truewill06/check-random-wallet',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/truewill06/check-random-wallet/archive/refs/tags/0.1.tar.gz',    
  keywords = ['BITCOIN', 'SEED'],   
  install_requires=[            
          
          'binascii',
	  'bip32utils',
	  'bs4',
          'pprint',
	  'time',
          'os',
	
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.10',
  ],
)
