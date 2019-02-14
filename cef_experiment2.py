"""
Communicate between Python and Javascript asynchronously using
inter-process messaging with the use of Javascript Bindings.
"""

from cefpython3 import cefpython as cef



def main(data):
    cef.Initialize()
    browser = cef.CreateBrowserSync(url='file:///index_no_read.html',
                                    window_title="Javascript Bindings")
    browser.SetClientHandler(LoadHandler(data))
    bindings = cef.JavascriptBindings()
    browser.SetJavascriptBindings(bindings)
    cef.MessageLoop()
    del browser
    cef.Shutdown()




class LoadHandler(object):

    def __init__(self, data):
        self.data = data
    def OnLoadEnd(self, browser, **_):
        browser.ExecuteFunction("js_function", self.data)


if __name__ == '__main__':
    data = {
    "0.00867999999999999": {
        "192": {
            "cluster": "15", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Nc", 
                    "value": 2.220179039646012
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 1.402599034299253
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 2.300632955006875
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 21.80564259131647
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 4.989404410200426
                }, 
                {
                    "source": "Nc", 
                    "target": "Nhc", 
                    "value": 2.224078070913066
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNHc", 
                    "value": 0.8007665607393193
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 2.281109735932893
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 1.530637906402655
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNc", 
                    "value": 2.965120456296594
                }, 
                {
                    "source": "Hc", 
                    "target": "Nz", 
                    "value": 0.7002073309663492
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNc", 
                    "value": 1.920051265099392
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 4.130554443206562
                }, 
                {
                    "source": "Nz", 
                    "target": "Hc", 
                    "value": 0.6953126554439963
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 4.233357825612092
                }, 
                {
                    "source": "Nz", 
                    "target": "NzHc", 
                    "value": 2.03431267917334
                }, 
                {
                    "source": "Nz", 
                    "target": "HzHc", 
                    "value": 1.325332453424464
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 1.398583004634848
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 5.111561104611662
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 1.781145071039786
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 5.51470507546718
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 2.303082255418849
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nc", 
                    "value": 0.8000962272370193
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 1.109126255306172
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzNc", 
                    "value": 2.820134005075329
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 1.815901359471665
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 21.80676254063222
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 2.28470750365781
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 5.108971644582462
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 1.111334867693483
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 8.401931169164445
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 1.52679698602959
                }, 
                {
                    "source": "NzNc", 
                    "target": "Hc", 
                    "value": 1.924060908884114
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 4.233917174760707
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzNHc", 
                    "value": 2.816063731099979
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzHc", 
                    "value": 0.4412817136962748
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nhc", 
                    "value": 4.986810807370565
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nc", 
                    "value": 2.963912582974738
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 1.778932237071879
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 1.816087318329967
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 8.403509220495021
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nz", 
                    "value": 2.034023789442619
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNc", 
                    "value": 0.4403499992609207
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 4.131442769723907
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nz", 
                    "value": 1.320993140965954
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 5.516575691353421
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 8, 
                    "num_source": 4, 
                    "num_target": 4
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 8, 
                    "num_source": 4, 
                    "num_target": 4
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "3", 
                    "id": "HzNHc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "6", 
                    "id": "NzNc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "3", 
                    "id": "HzHc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }
            ]
        }, 
        "329.5": {
            "cluster": "3", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Nc", 
                    "value": 1.630780085366486
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 2.350768365720148
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 2.947970314921625
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 20.76445016686006
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 1.784665326736085
                }, 
                {
                    "source": "Nc", 
                    "target": "Nhc", 
                    "value": 1.630408550853643
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNHc", 
                    "value": 0.5771611222468808
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 1.59499997945231
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 1.555426754212429
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNc", 
                    "value": 3.393340970502112
                }, 
                {
                    "source": "Hc", 
                    "target": "Nz", 
                    "value": 1.040799298091239
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 3.870691446384287
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNc", 
                    "value": 2.489083765728116
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 13.97512892445604
                }, 
                {
                    "source": "Nz", 
                    "target": "Hc", 
                    "value": 1.041487438828035
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNHc", 
                    "value": 2.464876931974477
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 8.767782063851543
                }, 
                {
                    "source": "Nz", 
                    "target": "NzHc", 
                    "value": 2.358549462070747
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 2.350119676856545
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 3.871189738615942
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 5.906209247166294
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 1.655832137763939
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 12.58698309554259
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 2.947091599656093
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nc", 
                    "value": 0.5769290703426132
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nz", 
                    "value": 2.463829108292762
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 0.9493919122559412
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzNc", 
                    "value": 9.273818199970924
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 1.207624834709983
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 0.6826670950052103
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 20.76492556110027
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 1.594937325249081
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 5.90684385200217
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 0.9488426582733227
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 5.993504438121047
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 1.555578261217892
                }, 
                {
                    "source": "NzNc", 
                    "target": "Hc", 
                    "value": 2.489465546254199
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 8.768267222598206
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzNHc", 
                    "value": 9.273846815197578
                }, 
                {
                    "source": "NzNc", 
                    "target": "HzNc", 
                    "value": 0.7085187190026011
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzHc", 
                    "value": 2.025743373165132
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nhc", 
                    "value": 1.784689483318771
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nc", 
                    "value": 3.393713043846921
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 1.655122268889061
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 1.208656420456298
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 5.993019328869694
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNc", 
                    "value": 0.7089505729834972
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nz", 
                    "value": 2.358964018235398
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 0.6827610391523874
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNc", 
                    "value": 2.025969495995069
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 13.97566093048912
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 12.58674522179055
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 8, 
                    "num_source": 4, 
                    "num_target": 4
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 8, 
                    "num_source": 4, 
                    "num_target": 4
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "4", 
                    "id": "NzNc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "1", 
                    "id": "HzNc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "6", 
                    "id": "NzHc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }, 
                {
                    "group": "3", 
                    "id": "HzHc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }
            ]
        }, 
        "63": {
            "cluster": "9", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Nc", 
                    "value": 1.370118164113068
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 2.142612437725882
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 2.515468337062852
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 21.16937152641029
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 3.608554404515918
                }, 
                {
                    "source": "Nc", 
                    "target": "Nhc", 
                    "value": 1.439863323658684
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNHc", 
                    "value": 1.076124475260673
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 1.088870406116679
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 1.696838923021468
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNc", 
                    "value": 2.8276741797298
                }, 
                {
                    "source": "Hc", 
                    "target": "Nz", 
                    "value": 0.7299435292194969
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 0.7738905610791034
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNc", 
                    "value": 1.604400517088009
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 6.139841758108272
                }, 
                {
                    "source": "Nz", 
                    "target": "Hc", 
                    "value": 0.7438085209751539
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNHc", 
                    "value": 1.584196668246723
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 5.694357276126594
                }, 
                {
                    "source": "Nz", 
                    "target": "NzHc", 
                    "value": 2.2104822813801
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 2.101731059602415
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 0.7885681768275288
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 5.071760471393503
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 1.431143690146387
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 6.302887952653297
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 2.55721610316253
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nc", 
                    "value": 1.044953153115548
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nz", 
                    "value": 1.58299158450435
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 1.356777765415528
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzNc", 
                    "value": 5.354542037473304
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 1.860295105895221
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 21.18199047553354
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 1.141933737297818
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 5.038323158902873
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 1.383573483356112
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 6.529011845057207
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 1.670071462886472
                }, 
                {
                    "source": "NzNc", 
                    "target": "Hc", 
                    "value": 1.621543482460158
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 5.699920652060425
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzNHc", 
                    "value": 5.356990608055308
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzHc", 
                    "value": 0.6419462216451312
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nhc", 
                    "value": 3.549861821660639
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nc", 
                    "value": 2.814969035906707
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 1.433898910055478
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 1.874643944761466
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 6.574195458751854
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nz", 
                    "value": 2.208029103819354
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNc", 
                    "value": 0.6402846162460967
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 6.129422246862328
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 6.302572039974335
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "2", 
                    "id": "Hc", 
                    "num_both": 8, 
                    "num_source": 4, 
                    "num_target": 4
                }, 
                {
                    "group": "3", 
                    "id": "Nz", 
                    "num_both": 8, 
                    "num_source": 4, 
                    "num_target": 4
                }, 
                {
                    "group": "4", 
                    "id": "Hz", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "3", 
                    "id": "NzNHc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "4", 
                    "id": "HzNHc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "1", 
                    "id": "NzNc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "4", 
                    "id": "HzNc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "4", 
                    "id": "NzHc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "2", 
                    "id": "HzHc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }
            ]
        }
    }, 
    "0.01891": {
        "192": {
            "cluster": "13", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Nc", 
                    "value": 12.77040458393809
                }, 
                {
                    "source": "Nhc", 
                    "target": "Nz", 
                    "value": 19.71080962239741
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 16.96013388791509
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 16.02881223635542
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 1.376792422004748
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNc", 
                    "value": 2.150836024667845
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzHc", 
                    "value": 10.33854965630171
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 13.73977213708595
                }, 
                {
                    "source": "Nc", 
                    "target": "Nhc", 
                    "value": 12.77647618644583
                }, 
                {
                    "source": "Nc", 
                    "target": "Hc", 
                    "value": 6.122563847186754
                }, 
                {
                    "source": "Nc", 
                    "target": "Nz", 
                    "value": 9.759382456957677
                }, 
                {
                    "source": "Nc", 
                    "target": "Hz", 
                    "value": 14.10049394640864
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNHc", 
                    "value": 11.83991232029269
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 1.1359195402393
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 17.74915078592498
                }, 
                {
                    "source": "Nc", 
                    "target": "NzHc", 
                    "value": 4.154100451435356
                }, 
                {
                    "source": "Nc", 
                    "target": "HzHc", 
                    "value": 5.09976785566771
                }, 
                {
                    "source": "Hc", 
                    "target": "Nc", 
                    "value": 5.982656939331353
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 6.34314492225751
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 6.681159548328096
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNc", 
                    "value": 1.124637925317639
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 1.554611212892714
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 5.71196970008261
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 1.387676773198869
                }, 
                {
                    "source": "Nz", 
                    "target": "Nhc", 
                    "value": 19.66605855454029
                }, 
                {
                    "source": "Nz", 
                    "target": "Nc", 
                    "value": 9.709060593853383
                }, 
                {
                    "source": "Nz", 
                    "target": "Hz", 
                    "value": 18.90058525962379
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNHc", 
                    "value": 15.76079824793977
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 1.6973545653786
                }, 
                {
                    "source": "Nz", 
                    "target": "HzHc", 
                    "value": 0.6868374940698728
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 17.02340310720914
                }, 
                {
                    "source": "Hz", 
                    "target": "Nc", 
                    "value": 14.15748546655117
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 6.255277128663056
                }, 
                {
                    "source": "Hz", 
                    "target": "Nz", 
                    "value": 18.79631413245792
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 12.84639108855309
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 17.15840448754889
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNc", 
                    "value": 11.8169879996551
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 1.207664689277446
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 11.77131029761101
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 15.44046232540952
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 16.02659087862584
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nc", 
                    "value": 11.83168126914381
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nz", 
                    "value": 15.80315506115338
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 12.78137898059713
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 0.2794146564384841
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzNc", 
                    "value": 14.87339286430376
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 2.563466411755751
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 0.09483347077774798
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 1.47056629621243
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 1.223459773465881
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 6.624405552962752
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 17.19027762141877
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 0.374635034072511
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNc", 
                    "value": 5.12065026640771
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 14.84995657139538
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 21.77997842061038
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 11.40278558821746
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nhc", 
                    "value": 2.162818024425149
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 17.75506498390853
                }, 
                {
                    "source": "NzNc", 
                    "target": "Hc", 
                    "value": 1.25718498660141
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 1.752588661939926
                }, 
                {
                    "source": "NzNc", 
                    "target": "Hz", 
                    "value": 11.76673667959825
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzNHc", 
                    "value": 14.88734143557675
                }, 
                {
                    "source": "NzNc", 
                    "target": "HzNHc", 
                    "value": 5.040163752646729
                }, 
                {
                    "source": "NzNc", 
                    "target": "HzNc", 
                    "value": 8.40060421983369
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzHc", 
                    "value": 15.48682194216412
                }, 
                {
                    "source": "NzNc", 
                    "target": "HzHc", 
                    "value": 14.92271106273584
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 1.563716488437878
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 1.11177187949947
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 14.91513521921067
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNc", 
                    "value": 8.26139383656267
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 22.39348028229149
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 7.268013791562639
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nhc", 
                    "value": 10.23281830967863
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nc", 
                    "value": 4.253655092775553
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 5.668434067090266
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 11.81612411007254
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 2.456445321627642
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 21.79314846616295
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNc", 
                    "value": 15.57925400255559
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 22.34139587893008
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 2.693927623102887
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 13.79496109256253
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nc", 
                    "value": 5.148796361421097
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 1.29455081218197
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nz", 
                    "value": 0.5908098138816354
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 15.43328711643231
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 0.06846679115460762
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 11.36431356519959
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNc", 
                    "value": 14.88032975432414
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 7.368866093220716
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 2.642793225124273
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 18, 
                    "num_source": 9, 
                    "num_target": 9
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 20, 
                    "num_source": 10, 
                    "num_target": 10
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "3", 
                    "id": "HzNHc", 
                    "num_both": 18, 
                    "num_source": 9, 
                    "num_target": 9
                }, 
                {
                    "group": "6", 
                    "id": "NzNc", 
                    "num_both": 20, 
                    "num_source": 10, 
                    "num_target": 10
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 18, 
                    "num_source": 9, 
                    "num_target": 9
                }, 
                {
                    "group": "3", 
                    "id": "HzHc", 
                    "num_both": 20, 
                    "num_source": 10, 
                    "num_target": 10
                }
            ]
        }, 
        "329.5": {
            "cluster": "1", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Nc", 
                    "value": 13.51786994905806
                }, 
                {
                    "source": "Nhc", 
                    "target": "Nz", 
                    "value": 27.16686082570526
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 14.28160656343139
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 24.51319931172749
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 7.828233646651883
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNc", 
                    "value": 6.566416377951168
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzHc", 
                    "value": 18.29251561905794
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 21.97152843865014
                }, 
                {
                    "source": "Nc", 
                    "target": "Nhc", 
                    "value": 13.5201549310801
                }, 
                {
                    "source": "Nc", 
                    "target": "Nz", 
                    "value": 23.74333753937658
                }, 
                {
                    "source": "Nc", 
                    "target": "Hz", 
                    "value": 12.69981601220573
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNHc", 
                    "value": 11.21069711334978
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 2.388484095781675
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 21.86519460186006
                }, 
                {
                    "source": "Nc", 
                    "target": "NzHc", 
                    "value": 1.717338567336135
                }, 
                {
                    "source": "Nc", 
                    "target": "HzHc", 
                    "value": 3.308807818982476
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 1.230353695077174
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 2.120950539506467
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 1.915211495607278
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 8.784032435933357
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 2.628814387687823
                }, 
                {
                    "source": "Nz", 
                    "target": "Nhc", 
                    "value": 27.16347263180065
                }, 
                {
                    "source": "Nz", 
                    "target": "Nc", 
                    "value": 23.73774081413213
                }, 
                {
                    "source": "Nz", 
                    "target": "Hz", 
                    "value": 21.49441601028747
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNHc", 
                    "value": 6.660109068855812
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 5.627043905699467
                }, 
                {
                    "source": "Nz", 
                    "target": "HzHc", 
                    "value": 0.9961571494810785
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 14.29330186041033
                }, 
                {
                    "source": "Hz", 
                    "target": "Nc", 
                    "value": 12.709219579478
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 1.22530452620355
                }, 
                {
                    "source": "Hz", 
                    "target": "Nz", 
                    "value": 21.47971321658767
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 9.91589284816571
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 19.93236899506407
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNc", 
                    "value": 9.035860916229094
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 1.505482307799484
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 21.32347031080509
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 26.87969028937464
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 24.51759920907774
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nc", 
                    "value": 11.21279918324097
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nz", 
                    "value": 6.667769421338697
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 9.908544253588259
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 6.090644273466546
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzNc", 
                    "value": 20.00256206295523
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 2.806494991453388
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 0.1541147131891671
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 7.813881700919711
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 2.376367896942718
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 2.118707639522403
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 19.93531906117491
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 6.100772068008229
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNc", 
                    "value": 9.673854969526705
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 12.41685264716927
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 32.10589877136569
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 16.31811757616424
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nhc", 
                    "value": 6.571910152388743
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 21.86840615272562
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 5.635737858973438
                }, 
                {
                    "source": "NzNc", 
                    "target": "Hz", 
                    "value": 9.029690034111967
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzNHc", 
                    "value": 20.00369227595708
                }, 
                {
                    "source": "NzNc", 
                    "target": "HzNHc", 
                    "value": 9.664895807656446
                }, 
                {
                    "source": "NzNc", 
                    "target": "HzNc", 
                    "value": 5.054004846566896
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzHc", 
                    "value": 17.27802370366799
                }, 
                {
                    "source": "NzNc", 
                    "target": "HzHc", 
                    "value": 24.40967215115419
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 1.910508361189968
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 1.515548923815019
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 12.42407309984795
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNc", 
                    "value": 5.038519997613067
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 15.55757442720619
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 6.322691761484099
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nhc", 
                    "value": 18.2764606098251
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nc", 
                    "value": 1.703495100648451
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 8.783509236130522
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 21.3282528423951
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 2.818382079779333
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 32.10771791694042
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNc", 
                    "value": 17.28874194113466
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 15.55207765532942
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 6.715324960004046
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 21.97959534779971
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nc", 
                    "value": 3.314609629104062
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 2.636993949658887
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nz", 
                    "value": 1.007324846489883
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 26.87619105857704
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 0.1578666394651366
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 16.31178790440003
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNc", 
                    "value": 24.4070607419146
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 6.335726235636053
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 6.70722109630241
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 20, 
                    "num_source": 10, 
                    "num_target": 10
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 18, 
                    "num_source": 9, 
                    "num_target": 9
                }, 
                {
                    "group": "4", 
                    "id": "NzNc", 
                    "num_both": 18, 
                    "num_source": 9, 
                    "num_target": 9
                }, 
                {
                    "group": "1", 
                    "id": "HzNc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "6", 
                    "id": "NzHc", 
                    "num_both": 18, 
                    "num_source": 9, 
                    "num_target": 9
                }, 
                {
                    "group": "3", 
                    "id": "HzHc", 
                    "num_both": 20, 
                    "num_source": 10, 
                    "num_target": 10
                }
            ]
        }, 
        "63": {
            "cluster": "7", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Nc", 
                    "value": 19.95832281700142
                }, 
                {
                    "source": "Nhc", 
                    "target": "Nz", 
                    "value": 31.4233914870755
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 8.125046426505195
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 13.19458908846526
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 11.79018516202555
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNc", 
                    "value": 8.470304604173823
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 10.35153776601532
                }, 
                {
                    "source": "Nc", 
                    "target": "Nhc", 
                    "value": 19.95867417220058
                }, 
                {
                    "source": "Nc", 
                    "target": "Nz", 
                    "value": 20.08216626616953
                }, 
                {
                    "source": "Nc", 
                    "target": "Hz", 
                    "value": 14.82317511988835
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNHc", 
                    "value": 14.52623330417672
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 1.209752336160106
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 20.87332849165254
                }, 
                {
                    "source": "Nc", 
                    "target": "NzHc", 
                    "value": 7.236720500032429
                }, 
                {
                    "source": "Nc", 
                    "target": "HzHc", 
                    "value": 5.676853810709923
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 1.865237180937091
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 3.721190663979
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 6.810815179159087
                }, 
                {
                    "source": "Nz", 
                    "target": "Nhc", 
                    "value": 31.42268721983355
                }, 
                {
                    "source": "Nz", 
                    "target": "Nc", 
                    "value": 20.08111144917661
                }, 
                {
                    "source": "Nz", 
                    "target": "Hz", 
                    "value": 18.85822520951724
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNHc", 
                    "value": 12.68686896937551
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 1.591850458526114
                }, 
                {
                    "source": "Nz", 
                    "target": "HzHc", 
                    "value": 1.333012576385009
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 8.127243825722351
                }, 
                {
                    "source": "Hz", 
                    "target": "Nc", 
                    "value": 14.82504054867865
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 1.866315160631214
                }, 
                {
                    "source": "Hz", 
                    "target": "Nz", 
                    "value": 18.85536677864116
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 13.05243639468291
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 25.91578696481859
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNc", 
                    "value": 14.58084297372645
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 4.047667644008235
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 24.79319202388748
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 16.14148080311205
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 13.19524540919105
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nc", 
                    "value": 14.5265414321379
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nz", 
                    "value": 12.6882218670732
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 13.05087860535946
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 5.18512818522474
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzNc", 
                    "value": 18.80729089686838
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 0.9206740819879394
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 3.308613570615284
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 11.78731971739966
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 1.207208952297675
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 3.720766373222276
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 25.91648398883541
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 5.187367974367991
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNc", 
                    "value": 6.985842469339813
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 4.279465877680414
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 37.69996772295978
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 9.990048098331512
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nhc", 
                    "value": 8.471368968145208
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 20.87405000297369
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 1.593599545563484
                }, 
                {
                    "source": "NzNc", 
                    "target": "Hz", 
                    "value": 14.57970459182641
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzNHc", 
                    "value": 18.80770548631226
                }, 
                {
                    "source": "NzNc", 
                    "target": "HzNHc", 
                    "value": 6.984019905839864
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzHc", 
                    "value": 7.817228952114482
                }, 
                {
                    "source": "NzNc", 
                    "target": "HzHc", 
                    "value": 13.01091013507725
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 4.046226148565061
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 4.28027010351353
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 6.091638239381844
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nc", 
                    "value": 7.234070985132584
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 6.810533666190324
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 24.79402530351017
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 0.9183236573561093
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 37.70011388611123
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNc", 
                    "value": 7.819168507384111
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 6.090978670228333
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 7.051630513764207
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 10.35334066512326
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nc", 
                    "value": 5.678326117719516
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nz", 
                    "value": 1.330549969121173
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 16.14111725042203
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 3.307444153960975
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 9.9890037064845
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNc", 
                    "value": 13.0101519826437
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 7.052802601678033
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "2", 
                    "id": "Hc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }, 
                {
                    "group": "3", 
                    "id": "Nz", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "4", 
                    "id": "Hz", 
                    "num_both": 20, 
                    "num_source": 10, 
                    "num_target": 10
                }, 
                {
                    "group": "3", 
                    "id": "NzNHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "5", 
                    "id": "HzNHc", 
                    "num_both": 18, 
                    "num_source": 9, 
                    "num_target": 9
                }, 
                {
                    "group": "6", 
                    "id": "NzNc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "4", 
                    "id": "HzNc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }, 
                {
                    "group": "5", 
                    "id": "NzHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "2", 
                    "id": "HzHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }
            ]
        }
    }, 
    "0.04929": {
        "192": {
            "cluster": "14", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 0.5214008467994471
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNc", 
                    "value": 1.50168875168738
                }, 
                {
                    "source": "Nc", 
                    "target": "Hc", 
                    "value": 4.039593427378651
                }, 
                {
                    "source": "Nc", 
                    "target": "Hz", 
                    "value": 12.59053561104946
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 4.701462380248151
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNc", 
                    "value": 8.33588053147089
                }, 
                {
                    "source": "Nc", 
                    "target": "NzHc", 
                    "value": 3.666575815364777
                }, 
                {
                    "source": "Nc", 
                    "target": "HzHc", 
                    "value": 11.37290180364571
                }, 
                {
                    "source": "Hc", 
                    "target": "Nc", 
                    "value": 4.052078915520425
                }, 
                {
                    "source": "Hc", 
                    "target": "Nz", 
                    "value": 28.98869930307225
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 28.68706750855356
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 10.8916920797021
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 3.206671101100369
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 23.6970835602572
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 12.48920039735516
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 37.26214282772501
                }, 
                {
                    "source": "Nz", 
                    "target": "Hc", 
                    "value": 28.98986034542752
                }, 
                {
                    "source": "Nz", 
                    "target": "Hz", 
                    "value": 3.367911271217884
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNHc", 
                    "value": 42.31561499504743
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 4.335587298257281
                }, 
                {
                    "source": "Nz", 
                    "target": "HzNc", 
                    "value": 11.74388868409834
                }, 
                {
                    "source": "Nz", 
                    "target": "HzHc", 
                    "value": 15.91423138576305
                }, 
                {
                    "source": "Hz", 
                    "target": "Nc", 
                    "value": 12.60811720267091
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 28.68891714183322
                }, 
                {
                    "source": "Hz", 
                    "target": "Nz", 
                    "value": 3.368056069327822
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 31.00692316444091
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 17.77752349774713
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 0.9350887012037908
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 19.89434399492873
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 0.5172313255706035
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 10.89404481273642
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nz", 
                    "value": 42.3122906041376
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzNc", 
                    "value": 7.190288695973004
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 1.039034322158866
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 4.679341090052827
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 3.202685227131179
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 31.00875514341128
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 12.26993515721447
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 9.294915234540657
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 16.3853141268318
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nhc", 
                    "value": 1.495539054378951
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 4.342179149547871
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzNHc", 
                    "value": 7.187105829538845
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nc", 
                    "value": 8.352946460705507
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 23.70205555540456
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nz", 
                    "value": 11.73789755881083
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 17.77818231913282
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 12.26588937963588
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 15.41034867809147
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 32.10245916384417
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nc", 
                    "value": 3.695045055780995
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 12.47230372100099
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 0.9467806232156926
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 9.300407401739424
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 15.42413576162998
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 4.030543779202777
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nc", 
                    "value": 11.35642150845136
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 37.26365660747604
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nz", 
                    "value": 15.91108602656127
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 19.89643479312036
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 1.041496500193154
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 16.38297042545995
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 32.1011190690472
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 4.01935211165707
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "NzNHc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "3", 
                    "id": "HzNHc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "5", 
                    "id": "NzNc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "HzHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }
            ]
        }, 
        "329.5": {
            "cluster": "2", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 1.375264189375179
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNc", 
                    "value": 0.3565394757828526
                }, 
                {
                    "source": "Nc", 
                    "target": "Hc", 
                    "value": 1.005580515876551
                }, 
                {
                    "source": "Nc", 
                    "target": "Hz", 
                    "value": 2.171977000199873
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 2.448275719173806
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNc", 
                    "value": 7.453066854785203
                }, 
                {
                    "source": "Nc", 
                    "target": "NzHc", 
                    "value": 1.797263309431005
                }, 
                {
                    "source": "Nc", 
                    "target": "HzHc", 
                    "value": 4.533847436656732
                }, 
                {
                    "source": "Hc", 
                    "target": "Nc", 
                    "value": 0.9994620896195007
                }, 
                {
                    "source": "Hc", 
                    "target": "Nz", 
                    "value": 14.47565607238795
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 32.20630813135924
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 4.064517983095129
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 1.397090960134765
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 22.54290834358326
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 14.03274042425809
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 39.25988459072617
                }, 
                {
                    "source": "Nz", 
                    "target": "Hc", 
                    "value": 14.46292534129054
                }, 
                {
                    "source": "Nz", 
                    "target": "Hz", 
                    "value": 2.442061425132954
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNHc", 
                    "value": 6.053035739524264
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 0.2411908721032632
                }, 
                {
                    "source": "Nz", 
                    "target": "HzNc", 
                    "value": 10.31127168086517
                }, 
                {
                    "source": "Nz", 
                    "target": "HzHc", 
                    "value": 4.77867199198115
                }, 
                {
                    "source": "Hz", 
                    "target": "Nc", 
                    "value": 2.183079334348284
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 32.20726198148083
                }, 
                {
                    "source": "Hz", 
                    "target": "Nz", 
                    "value": 2.428007668484555
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 40.17903739908303
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 5.543785475457023
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 1.368550886148341
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 15.22275656751857
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 1.375985112489829
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 4.074364818120259
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nz", 
                    "value": 6.055436823555338
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzNc", 
                    "value": 1.185156646711873
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 3.968144287340044
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 2.438857433928097
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 1.40212002585053
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 40.18298897516588
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 4.025936263974481
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 9.96228493340791
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 20.80314620266802
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nhc", 
                    "value": 0.360486320493259
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 0.2345501047971419
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzNHc", 
                    "value": 1.189506154716278
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nc", 
                    "value": 7.463143955771843
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 22.54224018832268
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nz", 
                    "value": 10.29828554781332
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 5.54235964139337
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 4.020782069375407
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 17.8037830382143
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 35.64694109726997
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nc", 
                    "value": 1.805849551315033
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 14.02934550613629
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 1.37159889970388
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 9.962121684390581
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 17.80797184149187
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 4.482183277066285
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nc", 
                    "value": 4.522179348683386
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 39.25638085910647
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nz", 
                    "value": 4.788686656122122
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 15.21824494920349
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 3.975479351364742
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 20.81151025015285
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 35.64392435114117
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 4.4753581832817
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "4", 
                    "id": "NzNc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }, 
                {
                    "group": "1", 
                    "id": "HzNc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "6", 
                    "id": "NzHc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "HzHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }
            ]
        }, 
        "63": {
            "cluster": "8", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 1.305062644210105
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNc", 
                    "value": 0.8460218317960229
                }, 
                {
                    "source": "Nc", 
                    "target": "Hc", 
                    "value": 4.248810310902259
                }, 
                {
                    "source": "Nc", 
                    "target": "Hz", 
                    "value": 1.815271649198803
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 0.8124071205485983
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNc", 
                    "value": 7.71615105938834
                }, 
                {
                    "source": "Nc", 
                    "target": "NzHc", 
                    "value": 0.1518322330178427
                }, 
                {
                    "source": "Nc", 
                    "target": "HzHc", 
                    "value": 6.853212147700931
                }, 
                {
                    "source": "Hc", 
                    "target": "Nc", 
                    "value": 4.257770005318243
                }, 
                {
                    "source": "Hc", 
                    "target": "Nz", 
                    "value": 26.44028716763932
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 27.55799456919416
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 11.75707953777586
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 0.4333136156259468
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 19.43804012445635
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 10.0623207729392
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 34.94974542312975
                }, 
                {
                    "source": "Nz", 
                    "target": "Hc", 
                    "value": 26.40816305854713
                }, 
                {
                    "source": "Nz", 
                    "target": "Hz", 
                    "value": 5.293316789888134
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNHc", 
                    "value": 30.23481862841451
                }, 
                {
                    "source": "Nz", 
                    "target": "HzNc", 
                    "value": 7.026895750110569
                }, 
                {
                    "source": "Nz", 
                    "target": "HzHc", 
                    "value": 11.00992886756516
                }, 
                {
                    "source": "Hz", 
                    "target": "Nc", 
                    "value": 1.845121799718105
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 27.57641262100536
                }, 
                {
                    "source": "Hz", 
                    "target": "Nz", 
                    "value": 5.218557061893321
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 35.55725006536343
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 6.550775197922618
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 0.5488092168902751
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 19.62513000775061
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 1.305062644214725
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 11.25008808226359
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nz", 
                    "value": 30.7000874034432
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzNc", 
                    "value": 2.075563998117638
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 0.7280697987329746
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 0.8614668995240453
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 0.4387097160738285
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 35.52337838756581
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 1.158418862031112
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 10.05422524357067
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 14.72629830146937
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nhc", 
                    "value": 0.8460218317974713
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzNHc", 
                    "value": 2.075563998114433
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nc", 
                    "value": 7.791955799868825
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 19.46386529407131
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nz", 
                    "value": 6.989737412172771
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 6.58023086798352
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 1.061132310946187
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 25.07801061005696
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 26.61555652399512
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nc", 
                    "value": 0.1909276661674044
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 10.06233126662721
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 0.5466923649348423
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 10.10472981594689
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 25.03138991453761
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 1.814894445846871
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nc", 
                    "value": 6.898876524911227
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 34.79386684191117
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nz", 
                    "value": 10.76991877924572
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 19.50306615188981
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 1.222843588661237
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 14.77913012000921
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 26.48980605291321
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 1.87067109832758
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "2", 
                    "id": "Hc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "3", 
                    "id": "Nz", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "2", 
                    "id": "Hz", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "3", 
                    "id": "NzNHc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "NzNc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "1", 
                    "id": "HzNc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "NzHc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "2", 
                    "id": "HzHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }
            ]
        }
    }, 
    "0.10447": {
        "192": {
            "cluster": "5", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Hc", 
                    "value": 42.47936636357809
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 39.13266716346823
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 36.40837949391997
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 28.13503217995088
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 22.79750042460974
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzHc", 
                    "value": 3.070804226321761
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 2.331762164362198
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 0.9599735823411883
                }, 
                {
                    "source": "Hc", 
                    "target": "Nhc", 
                    "value": 42.48052452581344
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 77.02328376440471
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 3.035031218133056
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 17.66379903351632
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 14.59107819276346
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 3.280475962029695
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 13.49467253288065
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 2.310684181861302
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 39.14710086595828
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 77.03641143077371
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 8.11047445597999
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 5.774814078964436
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 15.69777998507956
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 3.162272524751065
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 15.0564980986131
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 36.42235454119589
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 3.019279632478649
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 8.110678336732153
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 6.262337281227223
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 10.33573159645016
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 6.811870174227466
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 12.4490571496793
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 28.10148934558878
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 17.69138426796677
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 5.663888641495968
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 6.216215391065156
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 6.122462346189616
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 1.556335213127032
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 83.0831140473966
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 0.9599703215171579
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 2.310684181515018
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nhc", 
                    "value": 22.80258474570462
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 14.58484853834474
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 15.67814755929601
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 10.31697307901582
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 6.150599893078836
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 6.406333154402718
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 23.59350815997053
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nhc", 
                    "value": 3.041146349455107
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 3.309302176159453
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 3.179103283050216
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 6.827443065068459
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 1.496234660806447
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 6.440391453382528
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 3.032360756452399
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 2.348111565273324
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 13.47649130931623
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 15.02458569664672
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 12.47897491190132
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 83.0995825163042
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 23.58194049382039
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 3.076893733514212
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 2, 
                    "num_source": 1, 
                    "num_target": 1
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "Nz", 
                    "num_both": 2, 
                    "num_source": 1, 
                    "num_target": 1
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "NzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "NzNc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "3", 
                    "id": "HzHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }
            ]
        }, 
        "329.5": {
            "cluster": "11", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Hc", 
                    "value": 19.8281330517201
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 20.083447718626
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 20.21003219809337
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 17.67735331040218
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 15.85422507610702
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzHc", 
                    "value": 0.9426537249104395
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 7.782672019086164
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 1.417929677626282
                }, 
                {
                    "source": "Hc", 
                    "target": "Nhc", 
                    "value": 19.84188867185418
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 31.58361841799968
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 1.387288601437068e-05
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 4.066531758334252
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 5.124026103630255
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 3.366423580433696
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 13.97401684562951
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 2.256988391579299
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 20.09656256095982
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 31.5828862902004
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 0.8758120077058673
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 3.985205221405932
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 4.390658010519347
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 1.999460135609429
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 12.75060499162433
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 20.1565008058883
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 1.244176379733492e-05
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 0.8100953050203591
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 0.581867071515346
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 6.581617184728858
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 4.040708915854426
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 10.20890901757808
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 17.71425490786669
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 4.089098038305649
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 4.008688389026548
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 1.414106968574132e-05
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 5.626235699649405
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 1.087386753739276
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 35.84275604051408
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 1.417929677626282
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 2.256988391579299
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nhc", 
                    "value": 15.82954851876566
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 5.135009864304152
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 4.402376365188299
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 6.665828955929681
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 5.614515659564192
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 5.410910579885808
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 12.36780861086687
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nhc", 
                    "value": 0.9483972196000705
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 3.348496618180169
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 1.981798676797256
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 4.087025568738147
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 1.129006932797412
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 5.381556813419179
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 3.469487275933761
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 7.812654749684706
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 13.98982060170501
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 12.76729187018504
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 10.12670476607739
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 35.8362101464482
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 12.37275285271115
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 3.436806833134225
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 2, 
                    "num_source": 1, 
                    "num_target": 1
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 2, 
                    "num_source": 1, 
                    "num_target": 1
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "5", 
                    "id": "HzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "6", 
                    "id": "NzNc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "HzHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }
            ]
        }, 
        "63": {
            "cluster": "17", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Hc", 
                    "value": 38.05658198860726
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 32.46581917243881
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 12.51020824542888
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 27.41221097154324
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 8.53009153491216
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzHc", 
                    "value": 0.07737379400256089
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 8.738843377710042
                }, 
                {
                    "source": "Hc", 
                    "target": "Nhc", 
                    "value": 38.14487712767617
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 57.15852803872075
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 2.996631695784708
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 24.59236232089746
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 0.7037211087124364
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 14.86131100797546
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 2.513274585364549
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 32.55624326104083
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 57.16110261735367
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 1.847151560498496
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 0.9426572979782131
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 26.36396168472444
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 17.4769888060685
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 12.60782143314375
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 2.976654706077863
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 1.831182520278448
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 2.831281751881366
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 2.51375791847153
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 4.412991706566143
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 2.358879927300577
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 27.42314081947916
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 0.8653210128547407
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 2.745902647834195
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 11.65938543906018
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 0.8061438302662894
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 75.69692353077208
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 2.513274585364549
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 24.74744970780655
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 26.51483215603615
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 2.634547450835989
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 11.43707161124576
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 7.523012482466866
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 4.732740851464106
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nhc", 
                    "value": 0.1200406393388197
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 0.6809435232501366
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 4.357456237477991
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 0.8291347314176227
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 7.376741589466169
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 3.429137572571438
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 8.779596139404285
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 14.81449941125333
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 17.42854373587558
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 2.416278989599443
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 75.72531542628437
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 4.537940016872922
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 3.428480813937582
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 13, 
                    "num_source": 7, 
                    "num_target": 6
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 0, 
                    "num_source": 0, 
                    "num_target": 0
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 2, 
                    "num_source": 1, 
                    "num_target": 1
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "6", 
                    "id": "NzNc", 
                    "num_both": 2, 
                    "num_source": 1, 
                    "num_target": 1
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 13, 
                    "num_source": 6, 
                    "num_target": 7
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "1", 
                    "id": "HzHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }
            ]
        }
    }, 
    "0.18569": {
        "192": {
            "cluster": "6", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Hc", 
                    "value": 26.76686308068216
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 20.5365849693122
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 23.25375858028993
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 12.13935475358743
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 4.838406022809009
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzHc", 
                    "value": 0.1146073045618905
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 3.289788796159819
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 0.7442585697337368
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNc", 
                    "value": 0.454210498542694
                }, 
                {
                    "source": "Nc", 
                    "target": "NzHc", 
                    "value": 0.02276927372510424
                }, 
                {
                    "source": "Hc", 
                    "target": "Nhc", 
                    "value": 26.76671334957567
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 41.29274293307786
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 1.414413753280614
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 4.336940986962108
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 28.70267157808448
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 1.148386676530694
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 22.29347597907998
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 1.887244105095927
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 20.53652499231561
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 41.2928321369107
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 5.870273648259139
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 1.196713295264557
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 25.41254214559754
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 1.04129298669274
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 16.80437548900574
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 23.2539539806349
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 1.414459236603852
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 5.870526558094285
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 1.151650165920111
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 6.532524195709774
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 1.758326209730824
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 11.51816670674571
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 12.13925877047171
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 4.338601006393183
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 1.196677702509216
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 1.151215834510261
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 0.8739113957933276
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 1.2783865282558
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 58.16440085979872
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 0.7559552578139704
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 1.887244105431762
                }, 
                {
                    "source": "NzNc", 
                    "target": "NzHc", 
                    "value": 0.5503104998401391
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nhc", 
                    "value": 4.838432304958209
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nc", 
                    "value": 0.4835685762135883
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 28.70285022893108
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 25.41262674925165
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 6.532351086922679
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 0.8740366366329957
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 16.65625122620943
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 5.306849883386429
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nhc", 
                    "value": 0.1150612684691064
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nc", 
                    "value": 0.0562348551951627
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 1.148995133030197
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 1.04181057670871
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 1.758580309151308
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 1.278670173074328
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNc", 
                    "value": 0.5672525244599294
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 16.65669734503703
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 4.544690603334032
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 3.28998600507471
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 22.29337866788446
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 16.80419041382354
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 11.51859979418022
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 58.16425167707234
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 5.306574377059753
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 4.545388457448351
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "Nz", 
                    "num_both": 2, 
                    "num_source": 1, 
                    "num_target": 1
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "NzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "NzNc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 18, 
                    "num_source": 9, 
                    "num_target": 9
                }, 
                {
                    "group": "3", 
                    "id": "HzHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }
            ]
        }, 
        "329.5": {
            "cluster": "12", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Hc", 
                    "value": 15.54775011589514
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 19.90028937624464
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 9.156575736189586
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 18.7805811081292
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 4.627516601323196
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzHc", 
                    "value": 4.611932631044761
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 9.178853755825662
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 1.095529224383514
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNc", 
                    "value": 0.2785950890674631
                }, 
                {
                    "source": "Nc", 
                    "target": "NzHc", 
                    "value": 0.5308457880160256
                }, 
                {
                    "source": "Hc", 
                    "target": "Nhc", 
                    "value": 15.55308940753391
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 27.67848851034555
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 2.645063397409118
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 7.667489999462854
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 22.36120060460526
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 1.251324020445345
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 16.445217369761
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 2.138770898753492
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 19.90680207863402
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 27.67965136340202
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 0.8883121519030366
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 0.2224836440455478
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 29.11482432328476
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 0.09735618479598851
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 5.858443868046588
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 9.114965851121708
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 2.597678462908064
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 0.840031913685345
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 1.061090753070902
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 4.017415247465604
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 1.939952476799807
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 1.195837797519033
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 18.78279872570699
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 7.664641742463101
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 0.2183737722801249
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 1.017389672484907
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 3.39187881255166
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 0.1569451510228604
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 44.20520023172725
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 1.095529100451093
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 2.138770905587415
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nhc", 
                    "value": 4.639163175092893
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nc", 
                    "value": 0.3075447222447812
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 22.36747895018898
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 29.12001225854335
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 3.964287244628121
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 0.1858918545756753
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 7.956850600699391
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 3.809719903074682
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nhc", 
                    "value": 4.613161531769926
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nc", 
                    "value": 0.5542756005953876
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 1.247171857151174
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 0.08723381045900072
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 1.982077033362313
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 0.1545636327552051
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 7.946193922259432
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 2.633333981550184
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 9.156686895251902
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 16.44525247826437
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 5.857259136588818
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 1.149323419543199
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 44.20794107969127
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 3.803686035754964
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 2.629570723543166
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 2, 
                    "num_source": 1, 
                    "num_target": 1
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "6", 
                    "id": "NzNc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "1", 
                    "id": "HzHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }
            ]
        }, 
        "63": {
            "cluster": "18", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Hc", 
                    "value": 20.71607899044615
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 9.04484085923346
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 9.118197808982337
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 29.87097368991103
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 13.27876186709676
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzHc", 
                    "value": 1.729054649039752
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 17.13008084455483
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 0.9028945342354233
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNc", 
                    "value": 0.201604336811561
                }, 
                {
                    "source": "Nc", 
                    "target": "NzHc", 
                    "value": 0.6323235929160916
                }, 
                {
                    "source": "Hc", 
                    "target": "Nhc", 
                    "value": 20.71643583869837
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 35.65343878204897
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 1.932876726773078
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 2.782504250253201
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 17.61423849014292
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 1.287378958336271
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 17.78539890384983
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 2.245408104634617
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 9.045120202432065
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 35.65335964027967
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 3.777256429705779
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 0.9287859016533464
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 25.76406467881506
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 2.720790467514323
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 12.15841535551755
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 9.116563995299618
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 1.934827798592865
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 3.775367000924684
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 0.0157609435047957
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 2.977348033634931
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 2.192029203964019
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 1.357259597642116
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 29.87142395106147
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 2.782592424883879
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 0.9286173504456451
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 0.01781653105406474
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 0.3978117245252706
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 0.1511945066544536
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 50.19633453121067
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 0.902894534508891
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 2.245408104741387
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nhc", 
                    "value": 13.27903337524916
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nc", 
                    "value": 0.2018550918965526
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 17.61415329672161
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 25.76405815388323
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 2.975468687161138
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 0.3979886655703315
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 9.408834339169612
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 2.263608195819878
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nhc", 
                    "value": 1.728754026437481
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nc", 
                    "value": 0.6322041788880564
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 1.286747924506641
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 2.721350427361162
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 2.193296560610472
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 0.1516007864559616
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 9.408281951577742
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 0.5663277844859044
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 17.12946224585576
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 17.78566123392622
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 12.1587581296328
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 1.355072941073346
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 50.19651328273287
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 2.263264738309026
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 0.565445907609973
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 6, 
                    "num_source": 3, 
                    "num_target": 3
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 2, 
                    "num_source": 1, 
                    "num_target": 1
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "6", 
                    "id": "NzNc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "1", 
                    "id": "HzHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }
            ]
        }
    }, 
    "0.29109": {
        "192": {
            "cluster": "4", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Nc", 
                    "value": 2.75775606569637
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hc", 
                    "value": 2.535885039795394
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 3.890473893895602
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 28.46916235823172
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNc", 
                    "value": 0.2936060729192965
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 1.565870260258299
                }, 
                {
                    "source": "Nc", 
                    "target": "Nhc", 
                    "value": 2.733798489093554
                }, 
                {
                    "source": "Nc", 
                    "target": "Hc", 
                    "value": 1.078525809903716
                }, 
                {
                    "source": "Nc", 
                    "target": "Nz", 
                    "value": 0.1701299543913296
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 0.1594553740332727
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 1.57642300807071
                }, 
                {
                    "source": "Nc", 
                    "target": "HzHc", 
                    "value": 0.4873334993104914
                }, 
                {
                    "source": "Hc", 
                    "target": "Nhc", 
                    "value": 2.553008201309696
                }, 
                {
                    "source": "Hc", 
                    "target": "Nc", 
                    "value": 1.035362946754264
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 18.17720776052665
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 3.692764850605613
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 4.812861445889554
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 1.474176164207081
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 0.5259187381866182
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 18.14874342569583
                }, 
                {
                    "source": "Nz", 
                    "target": "Nc", 
                    "value": 0.1657273080318295
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 3.619692610545356
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 18.17600720535048
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 2.452402868309974
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 8.19082392642441
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 1.389000320195358
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 0.3960977970538744
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 17.48886473699434
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 3.896677460055018
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 3.681439714379248
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 2.444078604993725
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 0.9995016363343697
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 1.228379486079649
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 1.537995818770242
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 3.760950234633556
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 28.48379899512791
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 0.2576740620093232
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 4.810098952328352
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 8.190168284666175
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 0.9930197973867074
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNc", 
                    "value": 0.6747006653848455
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 2.506538875892733
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 9.69272902998254
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nhc", 
                    "value": 0.2911558042817912
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 1.580385095696227
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 3.619323824622717
                }, 
                {
                    "source": "NzNc", 
                    "target": "HzNHc", 
                    "value": 0.6656110516916345
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 1.479348557285197
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 1.394422232417937
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 1.237356311780953
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 2.501232523308565
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 1.532254391411279
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 1.451217231120755
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 0.5317475713429067
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 0.3948899783177613
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 1.539008067462102
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 1.529328298881517
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 0.2807394031944956
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nc", 
                    "value": 0.4399714813828994
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 18.15239668563234
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 17.4936046316408
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 3.745932124424413
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 9.69896502795955
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 1.448995365762859
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 0.272183377655605
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 11, 
                    "num_source": 6, 
                    "num_target": 5
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "2", 
                    "id": "Nz", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "1", 
                    "id": "NzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "2", 
                    "id": "NzNc", 
                    "num_both": 8, 
                    "num_source": 4, 
                    "num_target": 4
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "3", 
                    "id": "HzHc", 
                    "num_both": 15, 
                    "num_source": 7, 
                    "num_target": 8
                }
            ]
        }, 
        "329.5": {
            "cluster": "10", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Nc", 
                    "value": 4.309089777127832
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hc", 
                    "value": 6.78830415630926
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 9.526626249448702
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 5.122201160966378
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 20.31827438754128
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 6.032285165617567
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 5.742695722726237
                }, 
                {
                    "source": "Nc", 
                    "target": "Nhc", 
                    "value": 4.178376983799541
                }, 
                {
                    "source": "Nc", 
                    "target": "Hc", 
                    "value": 1.612397774501991
                }, 
                {
                    "source": "Nc", 
                    "target": "Nz", 
                    "value": 0.2268469721679815
                }, 
                {
                    "source": "Nc", 
                    "target": "Hz", 
                    "value": 2.286230300335566
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 2.435728619010272
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 1.999994441274055
                }, 
                {
                    "source": "Nc", 
                    "target": "HzHc", 
                    "value": 1.079471880460161
                }, 
                {
                    "source": "Hc", 
                    "target": "Nhc", 
                    "value": 6.821039617115105
                }, 
                {
                    "source": "Hc", 
                    "target": "Nc", 
                    "value": 1.457550347429233
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 13.34443711782478
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 2.726879718146539
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 9.391277124424326
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 2.774710157715381
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 0.3056658215907215
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 18.00441276012489
                }, 
                {
                    "source": "Nz", 
                    "target": "Nc", 
                    "value": 0.226846972167614
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 2.811611421587027
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 9.560604466940413
                }, 
                {
                    "source": "Hz", 
                    "target": "Nc", 
                    "value": 2.130779539662037
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 13.34575539739371
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 1.889172202217342
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 11.20909742056526
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 5.539275760745266
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 1.401734099450649
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 12.91731490191066
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 5.186619812866074
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 2.762117283282468
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 1.923143991504312
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 2.067786846369817
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 1.137579821923129
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 4.053182187261757
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 1.363338179418989
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 20.32492301844115
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 2.571108043910992
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 9.365262114051797
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 11.18182760788502
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 2.126126166618186
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 2.098351313278461
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 12.51495369972308
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 1.999994441274193
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 2.811611421586947
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nhc", 
                    "value": 5.919521943242172
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 2.860819337576118
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 5.624099284608377
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 1.186023675811718
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 1.9912873612212
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 2.04880268542367
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 2.832497107318888
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 0.2166855176111282
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 1.313926675851431
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 4.107908550236159
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 2.059788819027307
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 0.1964038880884169
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 5.771477581400379
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nc", 
                    "value": 0.9274768018160174
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 18.00044692006175
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 12.91204026388033
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 1.402129935005512
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 12.53702278491866
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 2.743143074317941
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 0.2882251069382173
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "5", 
                    "id": "HzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "6", 
                    "id": "NzNc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 10, 
                    "num_source": 5, 
                    "num_target": 5
                }, 
                {
                    "group": "1", 
                    "id": "HzHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }
            ]
        }, 
        "63": {
            "cluster": "16", 
            "links": [
                {
                    "source": "Nhc", 
                    "target": "Nc", 
                    "value": 2.060705888487842
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hc", 
                    "value": 3.812033472363536
                }, 
                {
                    "source": "Nhc", 
                    "target": "Hz", 
                    "value": 5.441838699594632
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzNHc", 
                    "value": 4.735920186416037
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNHc", 
                    "value": 38.56823146130397
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzNc", 
                    "value": 2.79681533729635
                }, 
                {
                    "source": "Nhc", 
                    "target": "NzHc", 
                    "value": 1.149042813762032
                }, 
                {
                    "source": "Nhc", 
                    "target": "HzHc", 
                    "value": 1.673329501105275
                }, 
                {
                    "source": "Nc", 
                    "target": "Nhc", 
                    "value": 2.060339417868576
                }, 
                {
                    "source": "Nc", 
                    "target": "Hc", 
                    "value": 0.7293856709552777
                }, 
                {
                    "source": "Nc", 
                    "target": "Hz", 
                    "value": 0.962221620755512
                }, 
                {
                    "source": "Nc", 
                    "target": "HzNHc", 
                    "value": 0.4303295870544767
                }, 
                {
                    "source": "Nc", 
                    "target": "NzNc", 
                    "value": 1.85235805410859
                }, 
                {
                    "source": "Nc", 
                    "target": "HzHc", 
                    "value": 0.8573285277247764
                }, 
                {
                    "source": "Hc", 
                    "target": "Nhc", 
                    "value": 3.811995980342391
                }, 
                {
                    "source": "Hc", 
                    "target": "Nc", 
                    "value": 0.729033294620709
                }, 
                {
                    "source": "Hc", 
                    "target": "Hz", 
                    "value": 22.4109686008168
                }, 
                {
                    "source": "Hc", 
                    "target": "NzNHc", 
                    "value": 0.2147054200613978
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNHc", 
                    "value": 3.112657196340111
                }, 
                {
                    "source": "Hc", 
                    "target": "HzNc", 
                    "value": 1.680417246804672
                }, 
                {
                    "source": "Hc", 
                    "target": "NzHc", 
                    "value": 0.008114989428580629
                }, 
                {
                    "source": "Hc", 
                    "target": "HzHc", 
                    "value": 27.5716034803158
                }, 
                {
                    "source": "Nz", 
                    "target": "NzNc", 
                    "value": 2.488336818910597
                }, 
                {
                    "source": "Hz", 
                    "target": "Nhc", 
                    "value": 5.441928984818706
                }, 
                {
                    "source": "Hz", 
                    "target": "Nc", 
                    "value": 0.9617660779081559
                }, 
                {
                    "source": "Hz", 
                    "target": "Hc", 
                    "value": 22.41109232425411
                }, 
                {
                    "source": "Hz", 
                    "target": "NzNHc", 
                    "value": 0.002362678688959287
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNHc", 
                    "value": 4.587076012189272
                }, 
                {
                    "source": "Hz", 
                    "target": "HzNc", 
                    "value": 2.982064175210595
                }, 
                {
                    "source": "Hz", 
                    "target": "NzHc", 
                    "value": 0.7580840721384036
                }, 
                {
                    "source": "Hz", 
                    "target": "HzHc", 
                    "value": 19.50550075593016
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Nhc", 
                    "value": 4.736415950276692
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hc", 
                    "value": 0.2121699080230569
                }, 
                {
                    "source": "NzNHc", 
                    "target": "Hz", 
                    "value": 0.002909238239712134
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNHc", 
                    "value": 1.415256239437367
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzNc", 
                    "value": 2.113810626225035
                }, 
                {
                    "source": "NzNHc", 
                    "target": "NzHc", 
                    "value": 3.002881776034145
                }, 
                {
                    "source": "NzNHc", 
                    "target": "HzHc", 
                    "value": 1.483932661731012
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nhc", 
                    "value": 38.56827263892465
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Nc", 
                    "value": 0.4307485929975286
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hc", 
                    "value": 3.112732383782634
                }, 
                {
                    "source": "HzNHc", 
                    "target": "Hz", 
                    "value": 4.58702129220005
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzNHc", 
                    "value": 1.414773051516766
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzNc", 
                    "value": 0.3507521366852679
                }, 
                {
                    "source": "HzNHc", 
                    "target": "NzHc", 
                    "value": 0.7030939640419741
                }, 
                {
                    "source": "HzNHc", 
                    "target": "HzHc", 
                    "value": 3.998729075446971
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nc", 
                    "value": 1.85235805375333
                }, 
                {
                    "source": "NzNc", 
                    "target": "Nz", 
                    "value": 2.488336818906412
                }, 
                {
                    "source": "HzNc", 
                    "target": "Nhc", 
                    "value": 2.79594616893109
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hc", 
                    "value": 1.681334145883971
                }, 
                {
                    "source": "HzNc", 
                    "target": "Hz", 
                    "value": 2.982892952114888
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzNHc", 
                    "value": 2.114219634745225
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzNHc", 
                    "value": 0.3516467389165377
                }, 
                {
                    "source": "HzNc", 
                    "target": "NzHc", 
                    "value": 1.383461016556307
                }, 
                {
                    "source": "HzNc", 
                    "target": "HzHc", 
                    "value": 0.6605799460561004
                }, 
                {
                    "source": "NzHc", 
                    "target": "Nhc", 
                    "value": 1.148331449838272
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hc", 
                    "value": 0.007292324782402727
                }, 
                {
                    "source": "NzHc", 
                    "target": "Hz", 
                    "value": 0.7587663505664146
                }, 
                {
                    "source": "NzHc", 
                    "target": "NzNHc", 
                    "value": 3.003217977823877
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNHc", 
                    "value": 0.702364739276456
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzNc", 
                    "value": 1.383465296169335
                }, 
                {
                    "source": "NzHc", 
                    "target": "HzHc", 
                    "value": 0.4141310702822653
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nhc", 
                    "value": 1.673383934329043
                }, 
                {
                    "source": "HzHc", 
                    "target": "Nc", 
                    "value": 0.8576457595145102
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hc", 
                    "value": 27.57159999880616
                }, 
                {
                    "source": "HzHc", 
                    "target": "Hz", 
                    "value": 19.50537519401023
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzNHc", 
                    "value": 1.48445717628622
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNHc", 
                    "value": 3.998643831444433
                }, 
                {
                    "source": "HzHc", 
                    "target": "HzNc", 
                    "value": 0.6614759787253377
                }, 
                {
                    "source": "HzHc", 
                    "target": "NzHc", 
                    "value": 0.4132057297150484
                }
            ], 
            "nodes": [
                {
                    "group": "1", 
                    "id": "Nhc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "2", 
                    "id": "Nc", 
                    "num_both": 12, 
                    "num_source": 6, 
                    "num_target": 6
                }, 
                {
                    "group": "3", 
                    "id": "Hc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "4", 
                    "id": "Nz", 
                    "num_both": 2, 
                    "num_source": 1, 
                    "num_target": 1
                }, 
                {
                    "group": "3", 
                    "id": "Hz", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "5", 
                    "id": "NzNHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "HzNHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }, 
                {
                    "group": "6", 
                    "id": "NzNc", 
                    "num_both": 4, 
                    "num_source": 2, 
                    "num_target": 2
                }, 
                {
                    "group": "3", 
                    "id": "HzNc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "3", 
                    "id": "NzHc", 
                    "num_both": 14, 
                    "num_source": 7, 
                    "num_target": 7
                }, 
                {
                    "group": "1", 
                    "id": "HzHc", 
                    "num_both": 16, 
                    "num_source": 8, 
                    "num_target": 8
                }
            ]
        }
    }
}
    main(data)