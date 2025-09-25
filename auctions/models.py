from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class active_lising(models.Model):
    title=models.CharField(max_length=64)
    description=models.TextField()
    starting_bid=models.IntegerField()
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name="creators_listing",default=1)
    image_url=models.URLField()


    def __str__(self):
        return f"all listings:{self.id}:title-{self.title} description- {self.description} starting bid:{self.starting_bid}  {self.image_url}"



class bids(models.Model):
    listing=models.ForeignKey(active_lising,on_delete=models.CASCADE,related_name="all_listings")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_bids")
    bid_amount=models.DecimalField(max_digits=12,decimal_places=4)

    def __str__(self):
        return f"{self.user} placed bid {self.bid_amount} on {self.listing}"



class comment(models.Model):
    user_comment=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_coments")
    commented_listing=models.ForeignKey(active_lising,on_delete=models.CASCADE,related_name="coments_on_listing")
    text_comm=models.TextField()

    def __str__(self):
        return f"{self.user_comment.username} commented on {self.commented_listing.title}"

    
    

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlists",default=1)
    watchlist = models.ManyToManyField(active_lising, related_name="watched_by")
