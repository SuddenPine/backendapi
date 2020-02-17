from rest_framework.permissions import AllowAny
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser

#other code
#in the end of class UserViewSet add the following

  def get_permissions(self):
    permission_classes = []
    if self.action == 'create':
      permission_classes = [AllowAny]
    elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
      permission_classes = [IsLoggedInUserOrAdmin]
    elif self.action == 'list' or self.action == 'destroy':
      permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]