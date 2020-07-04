


def track_list(request):



    context = {
        'core_topics': core_topic_serializer.data,
        'topic_dynamic': topic_dynamic,
        'topic_static': topic_static,
        'track_quiz_taken_check': track_quiz_taken_check
    }
    return Response(context)


