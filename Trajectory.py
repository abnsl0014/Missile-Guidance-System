from keras.models import model_from_json
from sklearn.externals import joblib
from collections import deque
class Trajectory:
    def __init__(self,modelPath='architecture.json',weightsPath='weights.h5',scalerPath = "scaler.pkl"):
        '''
            modelPath to be like = 'architecture.json'
            weightsPath to be like = 'weights.h5'
        '''
        json_file = open(modelPath, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.model = model_from_json(loaded_model_json)
        self.model.load_weights(weightsPath)
        self._look_back = 5
        self.scaler = joblib.load(scalerPath)
    def predictValues(self,x,lenPred):
        '''
        x is the small sequence
        shape should be (no. of rows,5,3)
        Look back is fixed to be 5 and
        3 is the params in each sequence
        
        lenPred Should be how many further points you want
        '''
        pred = []
        x = np.array(x)
        x = self.scaler.transform(x)
        x.reshape(-1,5,3)
        x = deque(x)
        assert(len(x) == self._look_back)
        for i in range(lenPred):
            x_prime = self.model.predict(np.array(x).reshape((1,self._look_back,3)))
            x.append(x_prime)
            x.popleft()
            x.append(x_prime)
        x = np.array(x)
        return x