from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from trees.models import Tree


# User registration karega
@api_view(['POST'])
def user_create(request):
    print(request.body)
    serializer = CustomUserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'status': "success",'messege':"user created successfully"}, status=status.HTTP_201_CREATED)
    return Response({'status':"error",'messege':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# user ka details
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    serializer = CustomUserSerializer(request.user)
    return Response({'status': "success",'messege':serializer.data}, status=status.HTTP_200_OK)


#list of common_name of tree user ne bookmark kiya hai
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_bookmarks(request):
    user = request.user
    bookmarked_trees = user.bookmarks.all() 
    common_names = [tree.common_name for tree in bookmarked_trees]
    return Response({'status': "success", 'bookmarked_trees': common_names}, status=status.HTTP_200_OK)


#creating bookmark tree ke common_name se
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_bookmark(request, common_name):
    try:
        tree = Tree.objects.get(common_name=common_name)
        user = request.user
        if tree not in user.bookmarks.all():
            user.bookmarks.add(tree)
            user.save()
            return Response({'status': 'success', 'message': str(common_name)+'bookmarked successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'info', 'message':str(common_name)+'is already bookmarked.'}, status=status.HTTP_200_OK)
        
    except Tree.DoesNotExist:
        return Response({'status': 'error', 'message': 'Tree not found.'}, status=status.HTTP_404_NOT_FOUND)


#delete bookmark tree ke common_name se
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_bookmark(request, common_name):
    try:
        tree = Tree.objects.get(common_name=common_name)
        user = request.user
        if tree  in user.bookmarks.all():
            user.bookmarks.remove(tree)
            user.save()
            return Response({'status': 'success', 'message': str(common_name)+' bookmarked tree deleted successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'info', 'message':str(common_name)+' is not bookmarked by user'}, status=status.HTTP_404_NOT_FOUND)
        
    except Tree.DoesNotExist:
        return Response({'status': 'error', 'message': 'No such tree exists'}, status=status.HTTP_404_NOT_FOUND)
