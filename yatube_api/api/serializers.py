from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Group, Post, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    pub_date = serializers.DateTimeField(required=False, read_only=True)
    image = serializers.ImageField(required=False)

    # group = serializers.PrimaryKeyRelatedField(
    #     queryset=Group.objects.all(), required=False
    # )

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = Post
        read_only_fields = ('id',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment
        read_only_fields = ('id', 'created')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group
        read_only_fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )
    user = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True
    )

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError('Нельзя подписаться на себя')
        return data

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = (UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following')
        ),
        )
