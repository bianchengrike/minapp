# django项目+微信小程序学习
### django作为后端处理创建 
  1. 创建项目文件夹：django-amdin startpeoject minapp 
  2. 进入项目文件夹后，创建应用文件夹：python manage.py startapp myapp
  3. 启动项目：python manage.py runserver  

#### 微信小程序学习视频太少且调试复杂，先学习django+vue创建前后端分离项目，最后对应到微信小程序
### vue项目环境搭建
  1. 安装node.js
  2. 设置node_global和node_cache（目录中没有手动创建再配置），接下来的所有操作要用管理员身份运行终端！！！
  3. 设置缓存文件夹：npm config set cache "E:\NodeJs\node_cache"
  4. 设置通过npm安装的包的存放路径：npm config set prefix "E:\NodeJs\node_global"
  5. 淘宝国内镜像安装：npm install -g cnpm --registry=https://registry.npm.taobao.org （同python清华镜像源），安装后可使用cnpm代替npm
  6. 将E:\NodeJs\node_global加入环境变量，cnpm就可以用了
  7. 安装vue： cnpm install vue -g
  8. 安装脚手架： cnpm install @vue/cli -g

### vue项目创建
  - 到要创建的目录下创建项目：vue init webpack 名称,因为看不懂，判断题一路回车（倒数三个选项选no，好像默认回车就是no）
    - 如遇如下（这个是要安装一个全局插件，直接 cnpm i -g @vue/cli-init）：
  ~~~ 
  Command vue init requires a global addon to be installed.
  Please run npm i -g @vue/cli-init and try again.
  ~~~  
  - 我安装了 element-ui  和 vue-resource ，直接 cnpm install 就可以了，然后src/main.js里面插入
  ~~~
  import Vue from 'vue'
  import App from './App'
  import router from './router'
  import ElementUI from 'element-ui'
  import VueResource from 'vue-resource'
  import 'element-ui/lib/theme-chalk/index.css'

  Vue.config.productionTip = false
  Vue.use(ElementUI)
  Vue.use(VueResource)
  /* eslint-disable no-new */
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })
  ~~~
### 配置好以后测试是否打通django
  1. 打包vue：myvue目录下 cnpm run build ,目录下获得dist文件夹
  2. 添加django settings 如下：
~~~python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['myvue/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


STATICFILES_DIRS = [os.path.join(BASE_DIR,'myvue/dist/static')]
~~~
  3. django urls 如下：
~~~python
from django.contrib import admin
from django.urls import path,include,re_path
from myapp import urls
from django.views.generic.base import TemplateView


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('myapp.urls')),
    path('',TemplateView.as_view(template_name='index.html')),
]
~~~
  4. django运行一手 ：python manage.py runserver ,出现vue欢迎界面就ok！