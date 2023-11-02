# 导入user包中的models模块
from user import models

# 使用user/models模块得到User类
admin = models.User('admin', '123456')
# 使用user.models模块中的show方法
admin.show()

from article import models
xx = models.Article('个人总结', 'XX')
xx.show()

