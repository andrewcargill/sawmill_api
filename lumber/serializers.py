from rest_framework import serializers
from .models import Test, DropboxTest, Tree, Log, Plank, MoistureCheck, Post

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class DropBoxFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropboxTest
        fields = '__all__'

# class TreeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tree
#         fields = '__all__'

# class LogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Log
#         fields = '__all__'

# class PlankSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Plank
#         fields = '__all__'

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ('id', 'species', 'date', 'reason_for_felling', 'age', 'longitude', 'latitude', 'lumberjack', 'image')

class LogSerializer(serializers.ModelSerializer):
    tree = TreeSerializer(read_only=True)

    class Meta:
        model = Log
        fields = ('id', 'length', 'tree', 'date', 'diameter', 'buck')

class PlankSerializer(serializers.ModelSerializer):
    log = LogSerializer()

    class Meta:
        model = Plank
        fields = ('id', 'log', 'date', 'width', 'depth', 'wood_grade', 'live_edge', 'furniture', 'structural', 'general', 'info', 'operator', 'image1', 'image2')


class MoistureCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoistureCheck
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
