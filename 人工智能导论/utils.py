
#用于修改图片格式，将该图片设置成符合该网络的格式。
import tensorflow as tf
import settings

# 我们准备使用经典网络在imagenet数据集上的与训练权重，所以归一化时也要使用imagenet的平均值和标准差
image_mean = tf.constant([0.485, 0.456, 0.406])
image_std = tf.constant([0.299, 0.224, 0.225])


def normalization(x):
    """
    对输入图片x进行归一化，返回归一化的值
    """
    return (x - image_mean) / image_std


def load_images(image_path, width=settings.WIDTH, height=settings.HEIGHT):
    """
    加载并处理图片
    :param image_path:　图片路径
    :param width: 图片宽度
    :param height: 图片长度
    :return:　一个张量
    """
    # 加载文件
    x = tf.io.read_file(image_path)
    # 解码图片
    x = tf.image.decode_jpeg(x, channels=3)
    # 修改图片大小
    x = tf.image.resize(x, [height, width])
    x = x / 255.
    # 归一化
    x = normalization(x)
    x = tf.reshape(x, [1, height, width, 3]) #在处理图像数据的时候总会遇到输入图像的维数不符合的情况，此时tensorflow中reshape()就很好的解决了这个问题。
    # 返回结果
    return x


def save_image(image, filename):
    x = tf.reshape(image, image.shape[1:])
    x = x * image_std + image_mean
    x = x * 255.
    x = tf.cast(x, tf.int32)  #tf.cast()函数的作用是执行 tensorflow 中张量数据类型转换，比如读入的图片如果是int8类型的，一般在要在训练前把图像的数据格式转换为float32。
    x = tf.clip_by_value(x, 0, 255)#可以将一个张量中的数值限制在一个范围之内。（可以避免一些运算错误:可以保证在进行log运算时，不会出现log0这样的错误或者大于1的概率）
    x = tf.cast(x, tf.uint8)
    x = tf.image.encode_jpeg(x) #重新编码
    tf.io.write_file(filename, x)  #写入
