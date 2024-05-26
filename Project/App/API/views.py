from rest_framework.decorators import api_view
from App.models import Project,Client
from .serializers import  ClientSerializer, ProjectSerializer, MyClientSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
#-------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def clients(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)         
        return Response(serializer.data)

    if request.method == 'POST':
        clients = Client.objects.all()
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
#------------------------------------------------------------------------------------------------

@api_view(['GET', 'PUT', 'DELETE'])                                                 
def clientsdetail(request, pk):
    
    if request.method == 'GET':
        client = Client.objects.get(pk=pk)
        #projects = Project.objects.get(pk=pk)
        serializer = MyClientSerializer(client)
        return Response(serializer.data)

    if request.method == 'PUT':
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        client = Client.objects.get(pk=pk)
        client.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


#----------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def allproject(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)         
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
    
#-----------------------------------------------------------------------------------------------------

@api_view(['GET', 'PUT', 'DELETE'])                                                 
def projectdetails(request, pk):
    if request.method == 'GET':
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        project = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        project = Project.objects.get(pk=pk)
        project.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


#--------------------------------------------------------------------------------------------------

@api_view(['GET'])
def gotproject(request):
    allot = Project.objects.filter(users=request.user)
    serializer = ProjectSerializer(allot, many=True)
    return Response(serializer.data)


#--------------------------------------------------------------------------------------------------