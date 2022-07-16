# impl-PGP-scheme-with-sm2
# PGP
![image](https://user-images.githubusercontent.com/104118101/179347214-89c8594f-2058-4321-a9fc-ad94a8863b8c.png)
* 实现思路： *<br>
Sender加密：<br>
1.Sender 和 Receiver 分别生成sm2的公钥和私钥(pk_s,sk_s),(pk_r,sk_r)<br>
2.生成临时会话密钥 Session Key(SK),这里的对称加密使用sm4<br>
3.加密sk：$ encryptKey=Ecn_{pk_r}(Sk) $<br>
4.加密data：$ encrypt=Ecn_{Sk}(data) $<br>
5.签名:$ Sign=Enc_{sk_s}(Sk)<br>
Receiver解密：<br>
1.用sk_r解密encryptKey得到SK<br>
2.验证签名<br>
3.用sk解密得到data<ne>
# 运行结果
![image](https://user-images.githubusercontent.com/104118101/179347199-219ad6d6-a2c9-4453-99bc-73eeeca84554.png)

