# skynet

* roadmap
 - hadoop 
 - kuberneter 
 - openstack
 - ceph
 - glusterfs
 - docker-machine

* rrdtool ubuntu install
   - http://martybugs.net/linux/rrdtool/
   - apt-get install librrds-perl rrdtool

# Python Dev

Phthon 虚拟环境(Virtual Environment)

虚拟环境工具(virturalenv)通过为不同项目创建专属的Python虚拟环境，以实现其依赖的库独立保存在不同的路径。 这解决了“项目X依赖包版本1.x，但项目Y依赖包版本为4.x”的难题，并且维持全局的site-packages目录干净、易管理。

举个例子，通过这个工具可以实现依赖Django 1.3的项目与依赖Django 1.0的项目共存。

进一步了解与使用请参考文档 [Virtual Environments](http://github.com/kennethreitz/python-guide/blob/master/docs/dev/virtualenvs.rst)。

[Python编辑器](http://python.freelycode.com/contribution/list/2)
[虚拟环境工具(virturalenv)构建](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)

```
pip install virtualenv

git clone git@github.com:skyneteye/skynet.git

cd skynet/

virtualenv --no-site-packages venv  # 创建一个独立的Python运行环境，参数--no-site-packages，得到一个不带任何第三方的“干净”的python运行环境。

source venv/bin/activate        # 进入venv这个独立环境

pip install -r path/requirements.txt
```

在venv环境下，用pip安装的包都被安装到venv这个环境下，系统Python环境不受任何影响。也就是说，venv环境是专门针对skynet这个应用创建的，符合我们的初衷。

退出当前venv环境，此时就回到了正常的环境，现在pip或python均是在系统Python环境下执行。

```
deactivate
```

完全可以针对每个应用创建独立的Python运行环境，这样就可以对每个应用的Python环境进行隔离。

virtualenv是如何创建“独立”的Python运行环境的呢？原理很简单，就是把系统Python复制一份到virtualenv的环境，用命令source venv/bin/activate进入一个virtualenv环境时，virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。

小结: virtualenv为应用提供了隔离的Python运行环境，解决了不同应用间多版本的冲突问题。

