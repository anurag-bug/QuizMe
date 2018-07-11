from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from quiz.forms import *
from quiz.models import *
def signup(request):

    if request.method =='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/quiz/login/')
        else:
            args = {'form': form}
            return render(request, 'quiz/signup.html', args)
    else:
        form =signupForm()
        args={'form':form}
        return render(request,'quiz/signup.html',args)
def apiResponse(request,id):
    countA = len(list((ResultLive.objects.filter(response='A',quizId=id))))
    countB = len(list(ResultLive.objects.filter(response='B',quizId=id)))
    countC = len(list(ResultLive.objects.filter(response='C',quizId=id)))
    countD = len(list(ResultLive.objects.filter(response='D',quizId=id)))
    mydict={'A':countA,'B':countB,'C':countC,'D':countD}
    return JsonResponse(mydict)
def showResponse(request,id):
    quizInstance=QuizDetails.objects.get(pk=id)
    args={'quiz_id':id,'quizObject':quizInstance}
    return render(request,"quiz/barChart.html",args);

def recordResponse(request,quiz_id):
    quizDetailsInstance = QuizDetails.objects.get(pk=quiz_id)
    if request.method =='POST':
        form=ResponseForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)

            res.quizId=quizDetailsInstance
            res.save()
            return HttpResponse("You response recorded Successfully")
        else:
            args = {'form': form}
            return render(request, 'quiz/submit_response.html', args)
    else:
        question=quizDetailsInstance.question
        optionA=quizDetailsInstance.optionA
        optionB = quizDetailsInstance.optionB
        optionC = quizDetailsInstance.optionC
        optionD = quizDetailsInstance.optionD
        date=quizDetailsInstance.creationTime
        form =ResponseForm()
        args={'form':form,'question':question,'optionA':optionA,'optionB':optionB,'optionC':optionC,'optionD':optionD}
        return render(request,'quiz/submit_response.html',args)

def createQuiz(request):
    if request.method == 'POST':
        form = QuizCreationForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.user = request.user
            quiz.save()
            return HttpResponse("You quiz with id %d is Successfully created."%(quiz.pk))
        else:
            args = {'form': form}
            return render(request, 'quiz/create_quiz.html', args)
    else:
        form = QuizCreationForm()
        args = {'form': form}
        return render(request, 'quiz/create_quiz.html', args)

