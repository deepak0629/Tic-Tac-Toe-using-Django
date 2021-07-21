from django.shortcuts import render
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from gameplay.forms import MoveForm
# Create your views here.
@login_required()
def game_detail(request,id):
    game=get_object_or_404(Game,pk=id)
    context={"game":game}
    if game.is_users_move(request.user):
        context['form']=MoveForm()
    print(context['form'])
    return render(request,"gameplay/game_detail.html",context)