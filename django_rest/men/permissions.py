from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    # ограничение прав доступа на уровне всего запроса
    def has_permission(self, request, view):
        # если запросы только на чтение, то разрешаем доступ
        print(request.method)
        if request.method in permissions.SAFE_METHODS:
            return True
        print(request.user.is_staff, request.user)

        # иначе только для админа(staff)
        return bool(request.user and request.user.is_staff)

    # ограничение прав доступа на уровне модели?
    # def has_object_permission(self, request, view, obj):
    #     pass


# если ты создал этого men, то только ты можешь его изменять, остальные только читать
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #  если чтение, то всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # изменение только владельцу(obj - это, кажется, конкретная запись из базы, которую мы выбрали)
        return obj.user == request.user
