from rest_framework import permissions


class GlobalPermissionClass(permissions.BasePermission):

    def __get_model_permission_codename(self, method, view):
        model_name = view.queryset.model._meta.model_name
        action = self.__get_action_sufix(method)
        app_name = view.queryset.model._meta.app_label
        return f'{app_name}.{action}_{model_name}'
    
    def __get_action_sufix(self, method):

        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view'
        }
        return method_actions.get(method)

    def has_permission(self, request, view):

        model_permission_codename = self.__get_model_permission_codename(request.method, view)
        print(model_permission_codename)
        if request.user.is_superuser:
            return True
        elif request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm(model_permission_codename)
        elif request.method == 'POST':
            return request.user.has_perm(model_permission_codename)
        elif request.method in ['PUT',  'PATCH']:
            return request.user.has_perm(model_permission_codename)
        elif request.method == 'DELETE':
            return request.user.has_perm(model_permission_codename)
        return False