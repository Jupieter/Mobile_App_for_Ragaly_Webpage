

def start_service():
    from jnius import autoclass, cast

    print("1 - start_service")
    service = autoclass("org.jupieter.ragaly_news.ServiceRagaly")
    mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
    service.start(mActivity, "")
    try:
        msg_service = autoclass("org.jupieter.ragaly_news.RagalyBroadcastService")
        print("service",service)
    except:
        print("NO   RagalyBroadcastService")
    try:
        msg_service.start(mActivity)
    except:
        print("NO   msg_service.start")
    return service


if __name__ == '__main__':
    start_service()
    


