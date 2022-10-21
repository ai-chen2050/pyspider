# OpenSea Crawler Instruction Document

<div align = right><b><i> <font color=purple>By Blake chen</font></i></b></div>    

<br />      

* @Time    :   2021/09/06 13:39:11    
* @Author  :   Blake chen          
* @Desc    :   Crawler Using For OpenSea


---    


## Installing (precondition）

develop python version : 3.8.3

```sh
pip install -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Using (Go For It)    

The two main methods for using supported. 
  - The Script Method: 
    - 1、Go to the file of settings.py, modify the value of ITERATOR_ROUND_NUM,SEARCH_THEME_WORDS to what you want.
    - 2、Remove code comments to startCrawling() in opensea/run.py:22  
    - 3、Just run `python opensea/run.py`

  - The Interface Method:
    - 1、run `python opensea/Qtmain.py`
    - 2、set value to 迭代轮数、搜索关键词
    - 3、and starting crawling ... 
     