from django.shortcuts import render , HttpResponse
import openai

# Create your views here.
def index(request):

    #get question enterd by the user in index.html 
    ques = request.GET.get('question')

    # setting our openai api key 
    openai.api_key = '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'

    # getting answer of the question user entered  
    res = openai.Completion.create(engine = "text-davinci-002",prompt = ques,max_tokens = 1024,n = 1,stop = None,temperature = 0.5)

    answer = {'ans':res['choices'][0]['text']}    

    #rendering our answer to index.html
    
    return render(request,'index.html',answer)    


