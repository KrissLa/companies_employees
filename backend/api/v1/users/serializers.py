"""
Модуль сериализации данных приложения users
"""
from rest_framework import serializers

from backend.apps.companies.models import Company
from backend.apps.users.models import User, Position, Skill, Language


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для создания и обновления
    записей о пользователи
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'patronymic',
                  'age', 'email', 'password', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }

    def create(self, validated_data: dict) -> User:
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class UserListSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для вывода списка пользоваетелей
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'patronymic',
                  'age', 'email', 'is_staff', 'is_active', 'date_joined',
                  'created_at', 'updated_at']


class UserRetrieveCompanySerializer(serializers.ModelSerializer):
    """
    Сериализация информации о компании для вывода в детальной информации
    о пользователе
    """

    class Meta:
        model = Company
        fields = ['id', 'name', ]


class UserRetrievePositionSerializer(serializers.ModelSerializer):
    """
    Сериализация информации о должности для вывода в детальной информации
    о пользователе
    """
    company = UserRetrieveCompanySerializer(read_only=True)

    class Meta:
        model = Position
        fields = ['position', 'company']


class UserRetrieveSkillSerializer(serializers.ModelSerializer):
    """
    Сериализация информации о навыках для вывода в детальной информации
    о пользователе
    """

    class Meta:
        model = Skill
        fields = ['skill', 'level']


class UserRetrieveLanguageSerializer(serializers.ModelSerializer):
    """
    Сериализация информации о языках для вывода в детальной информации
    о пользователе
    """

    class Meta:
        model = Language
        fields = ['language', 'level']


class UserRetrieveSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для вывода польной
    информации о пользователе
    """
    user_companies = UserRetrievePositionSerializer(many=True, read_only=True)
    skills = UserRetrieveSkillSerializer(many=True, read_only=True)
    languages = UserRetrieveLanguageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        exclude = ['password', 'companies']


class PositionUserSerializer(serializers.ModelSerializer):
    """
    Сериализация информации о пользователе
    """

    class Meta:
        model = User
        fields = ['id', 'username', ]


class PositionSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для должностей в компаниях
    """
    company = UserRetrieveCompanySerializer(read_only=True)
    user = PositionUserSerializer(read_only=True)

    class Meta:
        model = Position
        fields = ['id', 'position', 'user', 'company', 'is_active', 'created_at',
                  'updated_at']


class PositionCreateSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для добавления должностей
    """

    class Meta:
        model = Position
        fields = ['id', 'user', 'position', 'company', 'is_active']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class PositionUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для обновления должностей
    """

    class Meta:
        model = Position
        fields = ['id', 'user', 'position', 'company', 'is_active']
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
            'company': {'read_only': True},
        }


class SkillSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для навыков
    """
    user = PositionUserSerializer(read_only=True)

    class Meta:
        model = Skill
        fields = ['id', 'user', 'skill', 'level', 'is_active', 'created_at',
                  'updated_at']


class SkillCreateSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для навыков
    """

    class Meta:
        model = Skill
        fields = ['id', 'user', 'skill', 'level', 'is_active']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class SkillUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для навыков
    """

    class Meta:
        model = Skill
        fields = ['id', 'user', 'skill', 'level', 'is_active']
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
        }


class LanguageSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для языков
    """
    user = PositionUserSerializer(read_only=True)

    class Meta:
        model = Language
        fields = ['id', 'user', 'language', 'level', 'is_active', 'created_at',
                  'updated_at']


class LanguageCreateSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для языков
    """

    class Meta:
        model = Language
        fields = ['id', 'user', 'language', 'level', 'is_active']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class LanguageUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для языков
    """

    class Meta:
        model = Language
        fields = ['id', 'user', 'language', 'level', 'is_active']
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
        }
