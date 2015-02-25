import array

__author__ = 'grk'
from flask.ext.restful import reqparse, fields


quiz_fields = {
    "title": fields.String,
    "comments": fields.String,
    "language": fields.String,
    "createdBy": fields.String
}

creation_parser = reqparse.RequestParser()
creation_parser.add_argument('title', dest='title', type=str, location='json', required=True, help='title is missing', )
creation_parser.add_argument('comments', dest='comments', type=str, location='json', required=True,
                             help='comments is missing', )
creation_parser.add_argument('language', dest='language', type=str, location='json', required=True,
                             help='language is missing', )
creation_parser.add_argument('questions', dest='questions', type=list, location='json', required=False, )
#creation_parser.add_argument('questions.number', dest='questions.number', type=int, location='json', required=True, help="Question number must be an integer", )
#creation_parser.add_argument('questions.type', dest='questions.type', type=str, location='json', required=True, help="Question type is missing", )
#creation_parser.add_argument('questions.title', dest='questions.title', type=str, location='json', required=True, help="Question title is missing", )
creation_parser.add_argument('questions.answersTemplate', dest='questions.answersTemplate', type=list, location='json', )
#creation_parser.add_argument('questions.answersTemplate.number', dest='questions.answersTemplate.number', type=int, location='json', )
#creation_parser.add_argument('questions.answersTemplate.value', dest='questions.answersTemplate.value', type=str, location='json', )


class Quiz:
    def __init__(self):
        self.title = ""
        self.comments = ""
        self.language = ""
        self.createdBy = ""
        self.questions = []
        self.creationDate = None
        self.deleteDate = None
        self._id = ""

    @staticmethod
    def quiz_from_dict(quizDict):
        q = Quiz()
        q._id = quizDict.get('_id')
        q.title = quizDict.get('title')
        q.comments = quizDict.get('comments')
        q.language = quizDict.get('language')
        q.createdBy = quizDict.get('createdBy')
        q.creationDate = quizDict.get('creationDate')
        for questionDict in quizDict.get('questions'):
            print "\n", questionDict.get('title')
            q.questions.append(Question.question_from_dict(questionDict))

        return q

    def format(self):
        return {
            "_id": self._id,
            "title": self.title,
            "comments": self.comments,
            "language": self.language,
            "createdBy": self.createdBy,
            "creationDate": str(self.creationDate)
        }

    def format_for_update(self):
        return {

        }

    def format_for_delete(self):
        return {
        }


class Question:
    def __init__(self):
        self._id = ""
        self.number = 0
        self.type = ""
        self.rule = ""
        self.title = ""
        self.launchedBy = ""
        self.creationDate = ""
        self.answersTemplate = []

    @staticmethod
    def question_from_dict(questionDict):
        q = Question()
        q.title = questionDict.get('title')
        q.number = questionDict.get('number')
        q.type = questionDict.get('type')
        q.rule = questionDict.get('rule')
        q.launchedBy = questionDict.get('launchedBy')
        answersTemplate = questionDict.get('answersTemplate')
        print answersTemplate
        if not (answersTemplate is None):
            for answerTemplate_dict in questionDict.get('answersTemplate'):
                q.answersTemplate.append(AnswerTemplate.answer_from_dict(answerTemplate_dict))

        return q

    def format(self):
        return {
            "_id": self._id,
            "number": self.number,
            "type": self.type,
            "rule": self.rule,
            "title": self.title,
            "creationDate": str(self.creationDate),
            "launchedBy": self.launchedBy,
            "answersTemplate": self.answersTemplate
        }


class AnswerTemplate:
    def __init__(self):
        self._id = ""
        self.number = ""
        self.creationDate = ""
        self.value = ""

    @staticmethod
    def answer_from_dict(answerTemplateDict):
        a = AnswerTemplate()
        a.number = answerTemplateDict.get('number')
        a.value = answerTemplateDict.get('value')
        return a

    def format(self):
        return {
            "_id": self._id,
            "number": self.number,
            "value": self.value,
            "creationDate": str(self.creationDate)
        }
