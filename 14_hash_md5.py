import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    if user not in db:
        return False  # 用户不存在，直接返回 False

    # 每次都新创建一个 md5 实例
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    
    return db[user] == md5.hexdigest()
        

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
