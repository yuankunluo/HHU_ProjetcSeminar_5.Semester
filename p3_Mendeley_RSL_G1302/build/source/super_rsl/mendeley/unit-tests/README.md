# Unit tests

These tests make sure that the client works as expected by making calls to the api.
To do so it resets the account used for testing to make sure that the tests run in the same conditions.


**Please do not use your real mendeley account when running these unit tests as you would lose your library.**
Please register a separate testing account for running these tests. If you use an email provider like gmail
you can register a new mendeley account using yournormalemail+mendeleytest@gmail.com for example, so you
don't have to have another email account.

### How to run the tests

Just run the different test scripts with python
```
python test-basics.py
```

The first time you run them, you will have to authenticate with oauth, again **DO NOT USE YOUR REAL ACCOUNT**. The tokens will be saved as a pkl file in this folder so you don't have to authenticate again. If you want to change the testing account, simply remove the pkl file.

The tests will ask you to confirm that you're ok with running them on your account. If you don't want to have to type yes everytime and know what you are doing `man yes` can be of use.