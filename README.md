# 42-GRUT
42 Generalized Rambo Unit-Tester. Making unit-testing less of a hassle.


## Install & Use

#### 1)  Download `42-GRUT` in your Home Directory
```bash
  git clone https://github.com/akharrou/42-GRUT.git ~/42-GRUT
  
  PS: downloading the directory anywhere other than home and with any other name than '42-GRUT' will cause it to fail.
```
----
#### 2) Build your Project Specific Unit-Tester
```bash
  python3 ~/42-GRUT/build.py <name of your 42 project>
```
Example:
```
   python3 ~/42-GRUT/build.py fillit
   
                 or
   
   python3 ~/42-GRUT/build.py ft_ls
```
----
#### 3) Run
```bash
  python3 ~/42-GRUT/<project>_unittester.py ...
```
Example:
```
   python3 ~/42-GRUT/fillit_unittester.py ./fillit_A ./fillit_B testfile1 testfile2 testfile3
```
----

## Having Issues ?

 1) Did you change the name of the directory ? from `~/42-GRUT` to anything else ?
 2) DM: @AKharrou or @kmira on Slack

----
## Supported Projects

Currently only supports the following projects, although more are on their way ! & Contributions are WELCOME :D !

  * fillit
  * ft_ls
  * ft_ssl_md5
