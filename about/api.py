from .models import Branches , Partnerships
from .serializers import BranchesSerializers , PartnerShipsSerializers 
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def branchapi(request):
    br_data     = Branches.objects.all()
    branch_data = BranchesSerializers(br_data , many=True).data
    return Response({'branch_data': branch_data})


@api_view(['GET'])
def partnershipsapi(request):
    pr_data           = Partnerships.objects.all()
    partnerships_data = PartnerShipsSerializers(pr_data , many=True).data
    return Response({'partnerships_data': partnerships_data})

