from rest_framework import serializers
from database.models.question import Question, Answer, AnswerText
from django.contrib.auth.models import User

class BaseAnswerTextSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    def create(self, validated_data):
        text = AnswerText(text=validated_data.get('text'))
        text.save()

        question = validated_data.get('question')
        question.answer_text.add(text)
        return text

class BaseAnswerSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    right = serializers.BooleanField(default=False)
    candidate = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    def create(self, validated_data):
        answer = Answer(name=validated_data.get('name'),right=validated_data.get('right'))
        answer.save()
        # answer.candidate.add(validated_data.get('candidate'))

        question = validated_data.get('question')
        question.answer.add(answer)
        return question

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class BaseQuestionSerializer(serializers.Serializer):
    quest = serializers.CharField(required=True)

    def create(self, validated_data):
        question = Question(**validated_data)
        question.save()
        return question

    def update(self, instance, validated_data):
        instance.quest = validated_data.get('quest', instance.quest)
        instance.save()
        return instance

class AnswerTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerText
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(read_only=True, many=True)
    answer_text = AnswerTextSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = "__all__"