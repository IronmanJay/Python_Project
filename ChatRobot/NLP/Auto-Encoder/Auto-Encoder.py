from keras.layers import Input, Dense
from keras.models import Model
from sklearn.cluster import KMeans

class ASCIIAutoencoder():
    """基于字符的Autoencoder."""
    def __init__(self, sen_len=512, encoding_dim=32, epoch=50, val_ratio=0.3):
        """
        Init.
        :param sen_len:把sentences pad成相同的⻓度
        :param encoding_dim:压缩后的维度dim
        :param epoch:要跑多少epoch
        :param kmeanmodel:简单的KNN clustering模型
        """
        self.sen_len = sen_len
        self.encoding_dim = encoding_dim
        self.autoencoder = None
        self.encoder = None
        self.kmeanmodel =KMeans(n_clusters=2)
        self.epoch = epoch

    def fit(self, x):
        """
        模型构建。
        :param x: input text
        """
        # 把所有的trainset都搞成同⼀个size，并把每⼀个字符都换成ascii码
        x_train = self.preprocess(x, length=self.sen_len)
        # 然后给input预留好位置
        input_text = Input(shape=(self.sen_len,))
        # "encoded"每⼀经过⼀层，都被刷新成⼩⼀点的“压缩后表达式”
        encoded = Dense(1024, activation='tanh')(input_text)
        encoded = Dense(512, activation='tanh')(encoded)
        encoded = Dense(128, activation='tanh')(encoded)
        encoded = Dense(self.encoding_dim, activation='tanh')(encoded)
        # "decoded"就是把刚刚压缩完的东⻄，给反过来还原成input_text
        decoded = Dense(128, activation='tanh')(encoded)
        decoded = Dense(512, activation='tanh')(decoded)
        decoded = Dense(1024, activation='tanh')(decoded)
        decoded = Dense(self.sen_len, activation='sigmoid')(decoded)
        # 整个从⼤到⼩再到⼤的model，叫autoencoder
        self.autoencoder = Model(input=input_text, output=decoded)
        # 那么只从⼤到⼩（也就是⼀半的model）就叫encoder
        self.encoder = Model(input=input_text, output=encoded)
        
        #同理，我们接下来搞⼀个decoder出来，也就是从⼩到⼤的model
        #来，⾸先encoded的input size给预留好
        encoded_input =Input(shape=(1024,))
        # autoencoder的最后⼀层，就应该是decoder的第⼀层
        decoder_layer = self.autoencoder.layers[-1]
        #然后我们从头到尾连起来，就是⼀个decoder了！
        decoder =Model(input=encoded_input, output=decoder_layer(encoded_input))
        # compile
        self.autoencoder.compile(optimizer='adam', loss='mse')
        #跑起来
        self.autoencoder.fit(x_train, x_train,nb_epoch=self.epoch,batch_size=1000,shuffle=True,)
        #这⼀部分是⾃⼰拿⾃⼰train⼀下KNN，⼀件简单的基于距离的分类器
        x_train = self.encoder.predict(x_train)
        self.kmeanmodel.fit(x_train)

def predict(self, x):
    """
    做预测。
    :param x: input text
    :return: predictions
    """
    #同理，第⼀步把来的都给搞成ASCII化，并且⻓度相同
    x_test = self.preprocess(x, length=self.sen_len)
    #然后⽤encoder把test集给压缩
    x_test = self.encoder.predict(x_test)
    # KNN给分类出来
    preds = self.kmeanmodel.predict(x_test)
    return preds

def preprocess(self, s_list, length=256):
    ...