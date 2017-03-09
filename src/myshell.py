from blog.models import PostModel
qs = PostModel.objects.all()

for obj in qs:
	print(obj.age)

new_obj = PostModel.objects.create(title='Shell Post')
new_obj.save()
qs.count()

qs2 = PostModel.objects.filter(title__icontains='post')
PostModel.objects.all().count()
PostModel.other.all().count()

qs = PostModel.objects.filter(id__gt=0)
qs = PostModel.objects.filter(id__lt=0)
qs = PostModel.objects.filter(publish_date__year=2017)
import datetime
from datetime import datetime
new_date = datetime(2015, 1, 1)
new_date
PostModel.objects.filter(publish_date__gte=new_date)
PostModel.objects.filter(publish_date__lte=new_date)

from datetime import datetime
date1 = datetime(2015, 1, 1)
date2 = datetime(2015, 12, 31)
PostModel.objects.get_timeframe(date1, date2)