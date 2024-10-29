import diarizationUtils as d
import sys
import torch
import whisper
import os.path
from pyannote.audio import Pipeline

# model이 저장된 위치
MODEL_PATH = "./model.npy"

# 학습할 wav 파일들이 저장된 절대위치, 같은 이름의 json 파일도 필요하다
FILES_FOR_LEARNING_PATH = "./*.wav"

FILES_FOR_PREDICT_PATH = "./test.wav"


# 첫 실행시 실행하여 model.npy 만들기
def modelInitialization():
    d.modelInitialization()
    
        

# 학습용
def training():
    """
    training()
    모델을 불러와 FILES_FOR_LEARNING_GLOBAL_PATH 에 저장된 파일로 training 한다.
    return none
    """
    d.dataPreprocessing(FILES_FOR_LEARNING_PATH)
    d.modelLoadAndFit(MODEL_PATH)


def predict():
    
    # predict 하는 용도
    model, margs, targs, iargs = d.modelLoad(MODEL_PATH)
    #msqs = d.dataPreprocessingForPredict(FILES_FOR_LEARNING_GLOBAL_PATH)
    msqs= d.dataPreprocessingForPredict(FILES_FOR_PREDICT_PATH)

    predictedClusterId = 0
    with torch.no_grad():
        predictedClusterId = d.predict(model,msqs,iargs)
        #predictedClusterId = d.predictWithLabel(model,msqs, mcid, margs, targs, iargs)

        with open ("cluster_id.txt", "w") as output:
            output.write(str(predictedClusterId))

    clusterIdArray = predictedClusterId

    # Whisper
    model = whisper.load_model("large")



    # hop time :0.01s
    # window 크기 0.02s
    result = model.transcribe(FILES_FOR_PREDICT_PATH)

    #매핑용
    clusterMappingDict = {}
    clusterMappingDictIndex = 0

    whisperDiarizationOutput = []

    for seg in result['segments']:

        # start 부터 end 까지 시간을 재서
        # cluster id 의 index 자르기
        # 자르기 해서 clustering

        start = seg['start'] * 100

        #hop time = 0.01s
        # start 초 *100 하면 index -> floor
        end = seg['end'] * 100

        _clusterIdDict = {}

        # dictionary 에 나온 횟수 기록
        for i in clusterIdArray[int(start):int(end)]:
            if i in _clusterIdDict:
                _clusterIdDict[i] += 1
            else:
                _clusterIdDict[i] = 1


        # 가장 많이 나온 id 선택
        selectedClusterId = max(_clusterIdDict, key=_clusterIdDict.get)

        if selectedClusterId not in clusterMappingDict:
            clusterMappingDict[selectedClusterId] = clusterMappingDictIndex
            clusterMappingDictIndex += 1
        
        s = f"{seg['start']: .1f}${seg['end']: .1f}$ {clusterMappingDict[selectedClusterId]} ${seg['text']}"
        whisperDiarizationOutput.append(s)
        print(s)

    with open("./whisperDiarizationOutput.txt", 'w') as f:
        f.write('\n'.join(whisperDiarizationOutput))

    pass



def main():

    # model이 없으면 initialization을 실행, train안된 model을 만든다.
    if os.path.isfile(MODEL_PATH) == False:
        modelInitialization()

    # 학습용 - 학습시 주석 해제
    # training()


    # 예측용 - 예측시 주석 해제
    predict()




    return None

if __name__ == "__main__":
    main()
