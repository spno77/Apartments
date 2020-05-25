from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj == request.user or request.user.is_superuser


class IsOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.owner == request.user 


class IsAvailable(permissions.BasePermission):
	def has_object_permission(self,request,view,obj): 
		return obj.apartment.owner == request.user

