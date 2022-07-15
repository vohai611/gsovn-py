Hai Ngoc Vo

<!-- README.md is generated from README.Rmd. Please edit that file -->

# gsovn

<!-- badges: start -->
<!-- badges: end -->

The goal of gsovn is to scrape dataset from
[gso.gov.vn](https://gso.gov.vn) (Vietnam General statistic
organization)

## Installation

You can install the development version of gsovn from
[GitHub](https://github.com/vohai611/gsovn-py) with:

``` python
git clone https://github.com/vohai611/gsovn-py
cd gsovn-py
python setup.py install
```

## Usage

To view list of all dataset that available

``` python
import gsovn 
#> /usr/lib/python3/dist-packages/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.10) or chardet (3.0.4) doesn't match a supported version!
#>   warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
data = gsovn.gso_avail()
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/my-files/python-learning/gsovn/gsovn/gsovn.py:10: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
#> 
#> The code that caused this warning is on line 10 of the file /home/haivo/my-files/python-learning/gsovn/gsovn/gsovn.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.
#> 
#>   soup = bs4.BeautifulSoup(res.text)
```

To search for term

``` python
data.search("y te")
#>                                              content                                               link
#> 0  Bảo hiểm xã hội, bảo hiểm y tế và bảo hiểm thấ...  https://www.gso.gov.vn/px-web-2?pxid=V0316&the...
#> 1  Số cơ sở khám, chữa bệnh trực thuộc sở Y tế ph...  https://www.gso.gov.vn/px-web-2?pxid=V1105&the...
#> 2  Số giường bệnh trực thuộc sở Y tế phân theo đị...  https://www.gso.gov.vn/px-web-2?pxid=V1110&the...
#> 3                                Số nhân lực y tế(*)  https://www.gso.gov.vn/px-web-2?pxid=V1111&the...
#> 4          Số nhân lực y tế phân theo cấp quản lý(*)  https://www.gso.gov.vn/px-web-2?pxid=V1112&the...
#> 5  Số nhân lực ngành Y trực thuộc sở Y tế phân th...  https://www.gso.gov.vn/px-web-2?pxid=V1113&the...
#> 6  Số nhân lực ngành dược trực thuộc sở Y tế phân...  https://www.gso.gov.vn/px-web-2?pxid=V1115&the...
```

To download selected dataset

``` python
rs = data.search('thu nhap').head(1).get()
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/my-files/python-learning/gsovn/gsovn/gsovn.py:86: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
#> 
#> The code that caused this warning is on line 86 of the file /home/haivo/my-files/python-learning/gsovn/gsovn/gsovn.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.
#> 
#>   soup = bs4.BeautifulSoup(content.text)
#> /home/haivo/my-files/python-learning/gsovn/gsovn/gsovn.py:90: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
#> 
#> The code that caused this warning is on line 90 of the file /home/haivo/my-files/python-learning/gsovn/gsovn/gsovn.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.
#> 
#>   page_content  = bs4.BeautifulSoup(page.text)
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'pxweb.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'pxweb.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
rs[0]
#> 'Tổng thu nhập quốc gia theo giá thực tế chia theo Năm và Giá trị'
rs[1]
#>    Unnamed: 0_level_1  ... Tỷ lệ tổng thu nhập quốc gia so với tổng sản phẩm trong nước (**) (%)
#> 0                1990  ...                                               9360                   
#> 1                1991  ...                                               9470                   
#> 2                1992  ...                                               9660                   
#> 3                1993  ...                                               9620                   
#> 4                1994  ...                                               9750                   
#> 5                1995  ...                                               9990                   
#> 6                1996  ...                                               9910                   
#> 7                1997  ...                                               9840                   
#> 8                1998  ...                                               9770                   
#> 9                1999  ...                                               9820                   
#> 10               2000  ...                                               9860                   
#> 11               2001  ...                                               9870                   
#> 12               2002  ...                                               9840                   
#> 13               2003  ...                                               9840                   
#> 14               2004  ...                                               9810                   
#> 15               2005  ...                                               9816                   
#> 16               2006  ...                                               9785                   
#> 17               2007  ...                                               9720                   
#> 18               2008  ...                                               9702                   
#> 19               2009  ...                                               9569                   
#> 20               2010  ...                                               9619                   
#> 21               2011  ...                                               9569                   
#> 22               2012  ...                                               9599                   
#> 23               2013  ...                                               9571                   
#> 24               2014  ...                                               9525                   
#> 25               2015  ...                                               9372                   
#> 26               2016  ...                                               9311                   
#> 27               2017  ...                                               9240                   
#> 28               2018  ...                                               9355                   
#> 29               2019  ...                                               9359                   
#> 30         Sơ bộ 2020  ...                                               9424                   
#> 
#> [31 rows x 5 columns]
```

To download multiple dataset

``` python
multi_df = data.search("kinh te").head(4).get(multi=True)
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/my-files/python-learning/gsovn/gsovn/gsovn.py:86: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
#> 
#> The code that caused this warning is on line 86 of the file /home/haivo/my-files/python-learning/gsovn/gsovn/gsovn.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.
#> 
#>   soup = bs4.BeautifulSoup(content.text)
#> /home/haivo/my-files/python-learning/gsovn/gsovn/gsovn.py:90: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
#> 
#> The code that caused this warning is on line 90 of the file /home/haivo/my-files/python-learning/gsovn/gsovn/gsovn.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.
#> 
#>   page_content  = bs4.BeautifulSoup(page.text)
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'pxweb.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'pxweb.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'pxweb.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'pxweb.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'pxweb.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'pxweb.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'pxweb.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
#> /home/haivo/.local/lib/python3.8/site-packages/urllib3/connectionpool.py:1045: InsecureRequestWarning: Unverified HTTPS request is being made to host 'pxweb.gso.gov.vn'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
#>   warnings.warn(
multi_df
#> [['Lao động từ 15 tuổi trở lên đang làm việc hàng năm phân theo loại hình kinh tế chia theo Cách tính, Năm và Thành phần kinh tế',        Unnamed: 0_level_1  ... Khu vực có vốn đầu tư nước ngoài
#> 0   Tổng số (Nghìn người)  ...                              NaN
#> 1                    2000  ...                            35850
#> 2                    2001  ...                            34910
#> 3                    2002  ...                            42590
#> 4                    2003  ...                            75330
#> 5                    2004  ...                            91480
#> 6                    2005  ...                         1.112,80
#> 7                    2006  ...                         1.322,00
#> 8                    2007  ...                         1.562,20
#> 9                    2008  ...                         1.694,40
#> 10                   2009  ...                         1.524,60
#> 11                   2010  ...                         1.729,20
#> 12                   2011  ...                         2.098,60
#> 13                   2012  ...                         2.249,80
#> 14                   2013  ...                         2.518,30
#> 15                   2014  ...                         2.868,10
#> 16                   2015  ...                         3.197,80
#> 17                   2016  ...                         3.591,00
#> 18                   2017  ...                         4.207,80
#> 19                   2018  ...                         4.541,20
#> 20                   2019  ...                         4.768,40
#> 21             Sơ bộ 2020  ...                         4.733,80
#> 22             Cơ cấu (%)  ...                              NaN
#> 23                   2000  ...                              100
#> 24                   2001  ...                              090
#> 25                   2002  ...                              110
#> 26                   2003  ...                              190
#> 27                   2004  ...                              220
#> 28                   2005  ...                              260
#> 29                   2006  ...                              300
#> 30                   2007  ...                              350
#> 31                   2008  ...                              360
#> 32                   2009  ...                              320
#> 33                   2010  ...                              350
#> 34                   2011  ...                              420
#> 35                   2012  ...                              440
#> 36                   2013  ...                              480
#> 37                   2014  ...                              540
#> 38                   2015  ...                              600
#> 39                   2016  ...                              670
#> 40                   2017  ...                              780
#> 41                   2018  ...                              840
#> 42                   2019  ...                              870
#> 43             Sơ bộ 2020  ...                              883
#> 
#> [44 rows x 5 columns]], ['Lao động và cơ cấu lao động từ 15 tuổi trở lên đang làm việc hàng năm phân theo ngành kinh tế chia theo Ngành, Phân tổ và Năm',                                    Unnamed: 0_level_1  ... Cơ cấu (%)
#> 0                                             TỔNG SỐ  ...      10000
#> 1                 Nông nghiệp, lâm nghiệp và thủy sản  ...       3306
#> 2                                         Khai khoáng  ...         32
#> 3                       Công nghiệp chế biến, chế tạo  ...       2108
#> 4   Sản xuất và phân phối điện, khí đốt, nước nóng...  ...         32
#> 5   Cung cấp nước; hoạt động quản lý và xử lý rác ...  ...         31
#> 6                                            Xây dựng  ...        876
#> 7   Bán buôn và bán lẻ; sửa chữa ô tô, mô tô, xe m...  ...       1360
#> 8                                    Vận tải, kho bãi  ...        367
#> 9                          Dịch vụ lưu trú và ăn uống  ...        511
#> 10                          Thông tin và truyền thông  ...         63
#> 11         Hoạt động tài chính, ngân hàng và bảo hiểm  ...         85
#> 12                  Hoạt động kinh doanh bất động sản  ...         60
#> 13        Hoạt động chuyên môn, khoa học và công nghệ  ...         65
#> 14             Hoạt động hành chính và dịch vụ hỗ trợ  ...         67
#> 15  Hoạt động của Đảng Cộng sản, tổ chức chính trị...  ...        270
#> 16                                Giáo dục và đào tạo  ...        374
#> 17                  Y tế và hoạt động trợ giúp xã hội  ...        113
#> 18                   Nghệ thuật, vui chơi và giải trí  ...         49
#> 19                             Hoạt động dịch vụ khác  ...        190
#> 20  Hoạt động làm thuê các công việc trong các hộ ...  ...         40
#> 21       Hoạt động của các tổ chức và cơ quan quốc tế  ...          1
#> 
#> [22 rows x 31 columns]], ['Tỷ lệ lao động từ 15 tuổi trở lên đang làm việc trong nền kinh tế đã qua đào tạo phân theo nhóm tuổi (*) chia theo Nhóm tuổi và Năm',   Unnamed: 0_level_1  2009  2010  2011  ...  2017  2018  2019  Sơ bộ 2020
#> 0            TỔNG SỐ  1480  1470  1560  ...  2160  2200  2280        2405
#> 1              15-19   220   150   170  ...   140   180   130         115
#> 2              20-24  1670  1590  1820  ...  2780  2600  2500        2353
#> 3              25-29  2330  2410  2530  ...  3700  3830  3700        3791
#> 4              30-34  1800  2000  2080  ...  3190  3330  3480        3631
#> 5              35-39  1330  1400  1500  ...  2640  2760  3070        3241
#> 6              40-44  1220  1210  1290  ...  1910  1970  2170        2457
#> 7              45-49  1420  1310  1360  ...  1560  1550  1560        1802
#> 8                50+  1160  1180  1220  ...  1290  1310  1170        1222
#> 
#> [9 rows x 13 columns]], ['Tỷ lệ lao động từ 15 tuổi trở lên đang làm việc trong nền kinh tế đã qua đào tạo phân theo trình độ chuyên môn kỹ thuật (*) chia theo Chuyên môn kỹ thuật và Năm',         Unnamed: 0_level_1  2009  2010  2011  ...  2017  2018  2019  Sơ bộ 2020
#> 0                  TỔNG SỐ  1480  1470  1560  ...  2160  2200  2280        2405
#> 1                 Dạy nghề   480   190   210  ...   350   360   370         471
#> 2  Trung cấp chuyên nghiệp   270    ..    ..  ...   530   520   470         440
#> 3                 Cao đẳng   150   200   210  ...   330   370   380         382
#> 4          Đại học trở lên   550   560   610  ...   950   950  1060        1112
#> 
#> [5 rows x 13 columns]]]
```
