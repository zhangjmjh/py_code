



import time
import hashlib

def web_sign_no():
    t = time.time()
    timestamp = int(round(t * 1000))
    # print(timestamp)

    # sign = new_list + "&" + "timestamp={}".format(str("timestamp")) + "&" + "key=b0pDTrrfEn7zhnnLVRjmQG1pUzMrNt1M"
    sign = "timestamp={}".format(str("timestamp")) + "&" + "key=b0pDTrrfEn7zhnnLVRjmQG1pUzMrNt1M"
    # print(sign)

    app_sign = hashlib.sha1(sign.encode("utf-8")).hexdigest()
    # print(app_sign.upper())
    return app_sign.upper()

# if __name__ == '__main__':
#     get_sign()