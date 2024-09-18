from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Tree
from .serializers import TreeSerializer
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tree_list(request):
    trees = Tree.objects.all()
    serializer = TreeSerializer(trees, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tree_detail(request, common_name):
    try:
        tree = Tree.objects.get(common_name=common_name)
    except Tree.DoesNotExist:
        return Response({'status': "error", 'message': "No tree found with the provided common name"}, status=status.HTTP_404_NOT_FOUND)
    is_bookmarked = request.user.bookmarks.filter(common_name=common_name).exists()
    serializer = TreeSerializer(tree)
    return Response({'status': "success", 'message': serializer.data,'bookmarked': is_bookmarked},status=status.HTTP_200_OK)
