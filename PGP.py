import sm2

import hashlib
def md5(a):
    data = a
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()

from datetime import datetime
time = datetime.today().strftime('%Y%m%d')

print("---------------------用户a，b的信息:-------------------------")
ID_a = input("ID_a:")
ID_b = input("ID_b:")
sk_a, pk_a = sm2.setKey()
sk_b, pk_b = sm2.setKey()
ka = sm2.init(sk_a, pk_a)
kb = sm2.init(sk_b, pk_b)
print("用户a:", "\n", "ID", ID_a, "\n", "sk", sk_a, "\n", "pk", pk_a)
print("用户b:", "\n", "ID", ID_b, "\n", "sk", sk_b, "\n", "pk", pk_b)

print("\n--------------[", ID_a, "]给[", ID_b, "]发送信息---------------")
msg = input("message:")
mddd=md5(msg)
msg= str(len(msg)) + msg
hmsg_ID_time= mddd + ID_a + time
print("hash(msg)||ID||time:", hmsg_ID_time)

print("\n-------[", ID_a, "]使用sk_a生成hash(msg)||ID||time的签名--------")
sm2_a = sm2.sm2Algorithm()
Sign_a_msg = sm2_a.encrypt(hmsg_ID_time, ka)
print("Sign_a_msg:", Sign_a_msg)

print("\n-------[", ID_a, "]使用pk_b加密len(msg)||msg||Sign_a_msg--------")
msg_b= msg + Sign_a_msg
sm2_b=sm2.sm2Algorithm()
Enc_b_msg=sm2_b.encrypt(msg_b, kb)
print("Enc_b_msg:", Enc_b_msg)

print("\n-------[", ID_b, "]使用sk_b解密得到len(msg)||msg||Sign_a_msg--------")
Dec_b_msg = sm2_b.decrypt(Enc_b_msg, kb)
print("Dec_b_msg:",Dec_b_msg)
len_msg=len(msg)
lenth=int(len_msg)
res= Dec_b_msg[lenth:]
ll=len(str(len_msg))
msg_true= Dec_b_msg[ll:lenth]
print("消息的内容为:", msg_true)
print("签名为:", res)

print("\n-----------------------用pk_a验证签名,得到hash(msg)||ID||time--------------------")
jiea=sm2.decrypt(res, ka)
print(jiea)

print("\n--------------------------[", ID_b, "] 使用MD5生成hash(msg)---------------------")
md55=md5(msg_true)
print(md55)
if(md55+ID_a+time==jiea):
	print("通过验证")
else:
	print("未通过验证")
