from convertDataFormat import *
import unittest

def converttest(img):
    img_path = '/Users/spaceman/PycharmProjects/DataPreprocessing/'
    global image_name
    try:
        for _ in img['labels']:
            image_name = img['name'].replace('/', '_')
    except:
        pass
    img = cv2.imread(img_path + image_name)
    h, w = img.shape[:2]
    length = getLength(img)
    labels, points = convert_vertices_to_points(img)
    data = convert_scalabel_to_dataturks(img)
    dtturk = json.dumps(data, separators=(',', ':'))
    return dtturk
exampledata = {"content":"https://s3.amazonaws.com/mc-imt/vehicle/2019X8248/detail_damage2/16609/medium/7B95777D-BDAB-44B2-9F46-196C74C40EF7.jpeg","annotation":[{"label":["headlight"],"shape":"polygon","points":[[0.12635135135135134,0.0],[0.06689189189189189,0.08168168168168169],[0.06509009009009009,0.16576576576576577],[0.11193693693693695,0.2066066066066066],[0.21824324324324326,0.22342342342342345],[0.3822072072072072,0.22582582582582583],[0.5515765765765765,0.22582582582582583],[0.7443693693693695,0.22582582582582583],[0.747972972972973,0.0]],"notes":"","imageWidth":600,"imageHeight":800},{"label":["crack"],"shape":"polygon","points":[[0.34797297297297297,0.014414414414414415],[0.4092342342342342,0.1057057057057057],[0.49752252252252255,0.17297297297297298],[0.5768018018018019,0.1753753753753754],[0.6813063063063063,0.14654654654654653],[0.7371621621621622,0.11051051051051052],[0.7371621621621622,0.014414414414414415]],"notes":"","imageWidth":600,"imageHeight":800},{"label":["crack"],"shape":"polygon","points":[[0.5087365591397849,0.6935483870967741],[0.5275537634408601,0.7222222222222222],[0.5369623655913979,0.7508960573476702],[0.530241935483871,0.7777777777777777],[0.5396505376344085,0.7813620071684588],[0.5598118279569892,0.7491039426523297],[0.5745967741935484,0.7526881720430106],[0.551747311827957,0.7956989247311828],[0.5369623655913979,0.8189964157706093],[0.5168010752688172,0.8548387096774193],[0.49663978494623656,0.8566308243727598],[0.49395161290322576,0.8351254480286738],[0.512768817204301,0.8297491039426522],[0.5208333333333333,0.8118279569892473],[0.5221774193548386,0.7974910394265232],[0.5114247311827956,0.7831541218637993],[0.5194892473118279,0.7652329749103942],[0.5181451612903225,0.7455197132616488],[0.5060483870967741,0.7168458781362006]],"notes":"","imageWidth":600,"imageHeight":800}],"extras":None,"metadata":{"first_done_at":"","last_updated_at":"","sec_taken":0,"last_updated_by":"","status":"","evaluation":"CORRECT"}}
class TestDataFormat(unittest.TestCase):
    def TestFormat(self):
        self.assertDictequal(converttest('https://s3.amazonaws.com/mc-imt/vehicle/2019X8248/detail_damage2/16609/medium/7B95777D-BDAB-44B2-9F46-196C74C40EF7.jpeg'),exampledata)
        # I change value of "extras" from "null" to "None" for test
if __name__ == '__main__':
    unittest.main()