from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import ChatRoom, Message
from .forms import ChatRoomForm, AddParticipantForm
from django.conf import settings
from django.views.decorators.http import require_POST

@login_required
def chat_room(request, room_id):
    try:
        chat_room = request.user.chat_rooms.get(id=room_id)
    except ChatRoom.DoesNotExist:
        return HttpResponseForbidden()
    
    messages = chat_room.messages.order_by('timestamp')
    return render(request, 'chat/room.html', {'chat_room': chat_room, 'messages': messages})


from django.http import JsonResponse

@login_required
@require_POST
def send_message(request, room_id):
    chat_room = get_object_or_404(ChatRoom, id=room_id)
    if chat_room not in request.user.chat_rooms.all():
        return HttpResponseForbidden()

    message = request.POST.get('message')
    if message:
        msg = Message.objects.create(chat_room=chat_room, user=request.user, content=message)
        return JsonResponse({
            'user': msg.user.username,
            'message': msg.content,
            'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })
    return JsonResponse({'error': 'Message not sent'})


@login_required
def create_room(request):
    if request.method == "POST":
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            chat_room = form.save()
            chat_room.participants.add(request.user)
            return redirect('chat_room', room_id=chat_room.id)
    else:
        form = ChatRoomForm()
    return render(request, 'chat/create_room.html', {'form': form})

@login_required
def add_participant(request, room_id):
    chat_room = get_object_or_404(ChatRoom, id=room_id)
    if request.user not in chat_room.participants.all():
        return HttpResponseForbidden()

    if request.method == "POST":
        form = AddParticipantForm(request.POST)
        if form.is_valid():
            participant_username = form.cleaned_data['username']
            try:
                participant = get_object_or_404(settings.AUTH_USER_MODEL, username=participant_username)
                chat_room.participants.add(participant)
                return redirect('chat_room', room_id=room_id)
            except:
                pass  # Обработка случая, когда пользователь не найден
    else:
        form = AddParticipantForm()
    return render(request, 'chat/add_participant.html', {'chat_room': chat_room, 'form': form})
