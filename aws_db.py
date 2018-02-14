import boto
from boto.s3.key import Key
from boto.s3.connection import S3Connection
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class cl_aws():
    
    AWSID = None
    AWSKEY = None
    AWSBUCKET = None
    
    #rajawsdb
    
    def __init__(self):
        self.conn = boto.connect_s3(cl_aws.AWSID, cl_aws.AWSKEY)
        self.bucket = self.conn.get_bucket(cl_aws.AWSBUCKET)
        logging.debug('Successfully connected to AWS')

# Upload file on Amazon AWS S3 Storage
    def uploadFile(self,in_file):
        
        file_name = in_file.filename
        file_contents = in_file.stream.read()
        
        k = Key(self.bucket)
        k.key = file_name
        k.set_contents_from_string(file_contents)
        
        logging.debug('File Uploaded : %s' %file_name)


# List files in Amazon AWS on S3 Storage
    def getList(self):
    
        keys = self.bucket.get_all_keys()
        list_data = []
        
        for each in keys:
            temp = str(each).split(',')
            temp = temp[1]
            temp = temp.replace('>','')
            list_data.append(temp)
            
        return list_data

# Download file from Amazon AWS S3 Storage
    def downloadFile(self, in_file):
        
        for key in self.bucket:
            key.get_contents_to_filename(in_file)
            

# Delete a file on Amazon AWS S3 Storage
    def deleteFile(self,in_file):

        k = Key(self.bucket)
        k.key = in_file
        self.bucket.delete_key(k)



