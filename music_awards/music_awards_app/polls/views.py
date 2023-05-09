from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("You are in the web page of music awards app")

def detail(request, questions_id):
    return HttpResponse(f"You are seeing the question number {questions_id}")

def results(request, questions_id):
    return HttpResponse(f"You are seeing the results of question number {questions_id}")

def vote(request, questions_id):
    return HttpResponse(f"You are voting to the question number {questions_id}")
