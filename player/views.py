from django.shortcuts import render,redirect,get_object_or_404
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
from player.forms import InvitationForm
from player.models import Invitation
from django.core.exceptions import PermissionDenied

# Create your views here.
@login_required
def home(request):
    # first_player=Game.objects.filter(
    # first_player__username=request.user,
    #     status="F"
    # )
    # second_player = Game.objects.filter(
    #     second_player__username=request.user,
    #     status="S"
    # )
    # print(first_player)
    # print(second_player)
    # totallist=list(first_player)+list(second_player)
    # my_games=Game.object.games_for_user(request.user)
    # active_games=my_games.active()
    print(request.user)
    my_games=Game.objects.games_for_user(request.user)
    invitations=request.user.invitations_received.all()
    active_games=my_games.active()
    return render(request,"player/home.html",{
        "ngames":Game.objects.count(),
        "totalgames":active_games,
        "invitations":invitations
    })


@login_required
def new_invitation(request):
    if request.method=="POST":
        # temp= request.POST.copy()
        # temp['from_user']=request.user
        # print(request.POST)
        invitation=Invitation(from_user=request.user)
        form=InvitationForm(data=request.POST,instance=invitation)
        if form.is_valid():
            form.save()
            return  redirect("player_home")
    else:
        form=InvitationForm()
    return render(request,'player/new_invitation_form.html',{"form":form})

@login_required()
def accept_invitation(request,id):
    invitation=get_object_or_404(Invitation,pk=id)
    if not request.user==invitation.to_user:
        raise PermissionDenied
    if request.method=="POST":
        if "accept" in request.POST:
            game=Game.objects.create(first_player=invitation.to_user,second_player=invitation.from_user)
        invitation.delete()
        return redirect(game)
    else:
        return render(request,"player/accept_invitation_form.html",{
            'invitation':invitation
        })
