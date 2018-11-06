
def newmethod808():
    import requests
    request = requests.get("https://drive.google.com/uc?export=download&id=0B6ZlG_Eygdj-c1kzcmUxN05VUXM")
    with open("developer_survey_2017.zip","wb") as file:
        file.write(request.content)

    import zipfile
    with zipfile.ZipFile('developer_survey_2017.zip') as zip:
        zip.extractall('temp')

    import shutil, os
    shutil.move('temp/survey_results_public.csv', 'myExtract.csv')
    shutil.rmtree('temp')
    os.remove('developer_survey_2017.zip')   

newmethod808()   
# TODO November 07, 2018 