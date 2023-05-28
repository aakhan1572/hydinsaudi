import os
from django.db.models.signals import post_save, pre_save,pre_delete,post_delete
from django.dispatch import receiver
from .models import User, UserProfile
#from expads.models import Expatad,ExpatImage

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the userprofile if not exist
            UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass
# post_save.connect(post_save_create_profile_receiver, sender=User)


"""

def _delete_file(path):
   if os.path.isfile(path):
       os.remove(path)

def delete_post_signal_expatimage(ExpatImage):
    @receiver(post_delete, sender=ExpatImage)
    def ExpatImage_delete_file(sender, instance, *args, **kwargs):
        if instance.images:
            _delete_file(instance.images.path)       


def delete_post_signal_expatad(Expatad):
    @receiver(post_delete, sender=Expatad)
    def ExpatImage_delete_file(sender, instance, *args, **kwargs):
        if instance.cover_photo:
            _delete_file(instance.cover_photo.path)       
 

"""