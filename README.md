# 42-GRUT
42 Generalized Rambo Unit-Tester. Making unit-testing less of a hassle.


## Install & Use

#### 1)  Download `GRUT` in your Project's Root Directory
```bash
  git clone https://github.com/akharrou/42-GRUT.git ~/42-GRUT
```
----
#### 2) Build your Project Specific Unit-Tester
```bash
  python3 ~/42-GRUT/build.py <name of your 42 project>
```
Example:
```
   python3 42-GRUT/build.py fillit
```
----
#### 3) Run
```bash
  python3 grut-<project>.py <project's input> ...
```
Example:
```
   python3 grut-fillit.py sample_tetrominos_1 sample_tetrominos_2 sample_tetrominos_3
```
----


## Supported Projects

Currently only supports the following projects, although more are on their way !

  * fillit
  * ft_ls
  * ft_ssl_md5
