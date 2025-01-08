'''
HTTP协议简介
'''

'''
HTTP协议
- 在Web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让浏览器显示出来。
- 浏览器和服务器之间的传输协议是HTTP
- 注意
    - HTML是一种用来定义网页的文本，会HTML，就可以编写网页
    - HTML是在网络上传输的HTML协议，用于浏览器和服务器的通信
'''

'''
打开浏览器测试
Request Headers显示 GET / HTTP/1.1
- GET表示一个读取请求，将从服务器获得网页数据
- / 表示URL的路径，URL总是以 / 开头
- HTTP/1.1表示采用HTTP协议的版本为1.1
    - 注意：1.1版本的HTTP允许多个HTTP请求复用一个TCP连接，以加快传输速度
    
Content-Type: text/html
- Content-Type表示响应的内容，这里是text/html表示HTML网页
- 注意：浏览器就是依靠Content-Type来判断响应的内容是网页还是图片，是视频还是音乐
- 浏览器并不靠URL来判断响应的内容；
'''

'''
HTTP请求
- 步骤一：浏览器首先向服务器发送HTTP请求，请求包括：
    - 1. 方法：GET/POST， GET表示仅请求资源，POST会附带用户数据
    - 2. 路径：/full/url/path
    - 3. 由Host头指定：Host: www.sina.com.cn
    - 4. 还有其他相关的Header
    - **如果是POST，那么请求还包括一个Body，包含用户数据**； 
- 步骤二：服务器向浏览器返回HTTP响应，响应包括：
    - 1. 响应代码；如200表示成功
    - 2. 响应类型：Content-Type指定
        - Content-Type: text/html;charset=utf-8表示响应类型是HTML文本，并且编码是UTF-8
        - Content-Type: image/jpeg表示响应类型是JPEG格式的图片；
    - 注意：通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。
- 步骤三：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。
    - Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发
    - 当我们编写一个页面时，我们只需要在HTTP响应中把HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个HTTP请求，
    因此，一个HTTP请求只处理一个资源。
- HTTP协议具有极强的扩展性
    - 访问的新浪主页里面插入了其他各种服务器资源，将请求压力分散到各个服务器上；
'''

'''
HTTP格式
- 每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。
'''
