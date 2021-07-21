from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
BOARD_SIZE=3
GAME_STATUS_CHOICES=(
    ('F','First Player To Move'),
    ('S','Second Player To Move'),
    ('W','First Player Wins'),
    ('L','Second Player Wins'),
    ('D','Draw')
)

# class statusclass(models.Model):
#     statuscode=models.CharField(max_length=1,primary_key=True)
#     statusmeaning=models.CharField(max_length=300,null=False,blank=False,default='First Player To Move')
#     def __str__(self):
#         return "{0}".format(self.statusmeaning)

#Custom Query set

class customquerysetforgameclass(models.QuerySet):
    # extending this imports all functions like filter,all, etc..
    # now we write custom functions
    def games_for_user(self,user):
        return self.filter(Q(first_player__username=user)|Q(second_player__username=user))
    def active(self):
        return self.filter(Q(status="F")|Q(status="S"))

class Game(models.Model):
    first_player=models.ForeignKey(User,related_name='games_first_player',on_delete=models.CASCADE)
    second_player = models.ForeignKey(User,related_name='games_second_player', on_delete=models.CASCADE)
    start_time=models.DateTimeField(auto_now_add=True)
    last_active=models.DateTimeField(auto_now=True)

    status=models.CharField(max_length=1,default="F",choices=GAME_STATUS_CHOICES)
    objects=customquerysetforgameclass.as_manager()
    # status=models.ForeignKey(statusclass,related_name='status_code',on_delete=models.CASCADE,null=False,blank=False)
    def get_absolute_url(self):
        return reverse("gameplay_detail",args=[self.id])
    def board(self):
        board=[[None for x in range(BOARD_SIZE)] for  y in range(BOARD_SIZE)]
        for move in self.move_set.all():
            board[move.y][move.x]=move
            return board
    def is_users_move(self,user):
        return (user==self.first_player and self.status=="F") or (user==self.second_player and self.status=="S")
    def __str__(self):
        return "{0} vs {1}".format(self.first_player,self.second_player)






class Move(models.Model):
    x=models.IntegerField()
    y=models.IntegerField()
    comment=models.CharField(max_length=300,blank=True,null=True,default="default added")
    is_first_player=models.BooleanField(editable=False)
    game=models.ForeignKey(Game,on_delete=models.CASCADE,null=True,editable=False)
    by_first_player=models.BooleanField(editable=False)
    def __str__(self):
        return "{0}:{1}:{2}:{3}:{4}".format(self.x,self.y,self.comment,self.is_first_player,self.game)