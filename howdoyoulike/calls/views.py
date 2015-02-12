from django.core.exceptions import ObjectDoesNotExist
from django_twilio.decorators import twilio_view
from twilio.twiml import Response, Reject

from .models import Caller, Question


@twilio_view
def call(request):
    fromNumber = request.POST.get('From', '')[-10:]

    try:
        caller = Caller.objects.get(phone_number=fromNumber)
        if caller.start_fresh:
            textToSay = caller.intro_text
            caller.start_fresh = False
            caller.question_num = caller.start_num
            caller.save()
            r = Response()
            r.gather(timeout=120, finishOnKey='#').say(textToSay, voice='man')
            return r
        elif caller.question_num > caller.end_num:
            textToSay = caller.outro_text
            r = Response()
            r.say(textToSay, voice='man')
            return r
        else:
            textToSay = ''

        thisQuestion = Question.objects.get(num=caller.question_num)

        textToSay += thisQuestion.question_text + ' . . . '
        for choice in thisQuestion.choices.all():
            thisChoiceText = ''
            if not choice.num == 0:
                thisChoiceText += str(choice.num) + ' . . . '
            thisChoiceText += choice.choice_text + ' . . . . '
            textToSay += thisChoiceText

        caller.question_num += 1
        caller.save()
        r = Response()
        r.gather(timeout=120, finishOnKey='#').say(textToSay, voice='man')
        return r

    except ObjectDoesNotExist:
        return Reject()