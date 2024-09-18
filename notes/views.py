from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from trees.models import Tree

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_note(request, common_name):
    try:
        tree = Tree.objects.get(common_name=common_name)
    except Tree.DoesNotExist:
        return Response({'status': "error", 'message': "Tree not found"}, status=status.HTTP_404_NOT_FOUND)
    
    existing_note = Note.objects.filter(user=request.user, tree=tree).first()
    if existing_note:
        return Response({'status': "error", 'message': "You have already created a note for this tree"}, status=status.HTTP_400_BAD_REQUEST)

    data = request.data.copy()
    data['user'] = request.user.id
    data['tree'] = tree.id 

    serializer = NoteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': "success", 'message': "Note created", 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'status': "error", 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_note(request, common_name):
    try:
        tree = Tree.objects.get(common_name=common_name)
        note = Note.objects.get(tree=tree, user=request.user)
    except Tree.DoesNotExist:
        return Response({'status': "error", 'message': "Tree not found"}, status=status.HTTP_404_NOT_FOUND)
    except Note.DoesNotExist:
        return Response({'status': "error", 'message': "Note not found or you're not the owner"}, status=status.HTTP_404_NOT_FOUND)

    serializer = NoteSerializer(note, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': "success", 'message': "Note updated", 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response({'status': "error", 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_note(request, common_name):
    try:
        tree = Tree.objects.get(common_name=common_name)
        note = Note.objects.get(tree=tree, user=request.user)
    except Tree.DoesNotExist:
        return Response({'status': "error", 'message': "Tree not found"}, status=status.HTTP_404_NOT_FOUND)
    except Note.DoesNotExist:
        return Response({'status': "error", 'message': "Note not found or you're not the owner"}, status=status.HTTP_404_NOT_FOUND)
    note.delete()
    return Response({'status': "success", 'message': "Note deleted"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_note(request, common_name):
    try:
        tree = Tree.objects.get(common_name=common_name)
        note = Note.objects.get(user=request.user, tree=tree)
    except Tree.DoesNotExist:
        return Response({'status': "error", 'message': "Tree not found"}, status=status.HTTP_404_NOT_FOUND)
    except Note.DoesNotExist:
        return Response({'status': "error", 'message': "Note not found for this tree and user"}, status=status.HTTP_404_NOT_FOUND)
    serializer = NoteSerializer(note)
    return Response({'status': "success", 'note': serializer.data}, status=status.HTTP_200_OK)
