from django.db import models

# Create your models here.
class db_status(models.Model):   
    name = models.CharField(primary_key=True, max_length=20)   
    status = models.DateTimeField(max_length=50)
    score = models.IntegerField()
    
    def __unicode__(self):
        return self.name + ': ' + self.status.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:     
        db_table = 'status' 

class db_commentdb(models.Model):
    cid = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=50)
    postDate = models.DateTimeField(max_length=50)
    sortDate = models.DateTimeField(max_length=50)
    contents = models.CharField(max_length=10000)
    
    class Meta:     
        db_table = 'commentdb' 
    
class db_comment2db(models.Model):
    id = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    userName = models.CharField(max_length=50)
    postDate = models.DateTimeField(max_length=50)
    contents = models.CharField(max_length=10000)
    
    class Meta:     
        db_table = 'comment2db' 

class db_ac_contents_info(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=1000)
    up = models.CharField(max_length=1000)
    postTime = models.DateTimeField(max_length=50)
    url = models.CharField(max_length=50)
    
    class Meta:     
        db_table = 'accommentsinfo' 
             
class db_ac_contents_delete(models.Model):
    cid = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=100000)
    userName = models.CharField(max_length=50)
    quoteCid = models.IntegerField()
    layer = models.IntegerField()
    acid = models.IntegerField()
    height = models.IntegerField()
    isDelete = models.IntegerField()
    siji = models.IntegerField()
    zuipao = models.IntegerField()
    checkTime = models.DateTimeField(max_length=50)
    
    class Meta:     
        db_table = 'accomments_delete' 
        
class db_ac_contents_siji(models.Model):
    cid = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=100000)
    userName = models.CharField(max_length=50)
    quoteCid = models.IntegerField()
    layer = models.IntegerField()
    acid = models.IntegerField()
    height = models.IntegerField()
    isDelete = models.IntegerField()
    siji = models.IntegerField()
    zuipao = models.IntegerField()
    checkTime = models.DateTimeField(max_length=50)
    
    class Meta:     
        db_table = 'accomments_siji' 
        
class db_ac_refresh(models.Model):
    id = models.IntegerField(primary_key=True)
    createTime = models.DateTimeField(max_length=50)
    status = models.IntegerField()
    
    def __unicode__(self):
        return str(self.id) + '(' + str(self.status) + '): ' + self.createTime.strftime("%Y-%m-%d %H:%M:%S")
    
    class Meta:     
        db_table = 'acrefresh' 