# Q1 Host a static website using GCS bucket. 
---
> In the Cloud Console Home page go to the cloud storage service
---
> Create a new bucket and transfer the index.html file onto it
---
> Open cloud shell and use the below code to apply ACL settings to your index.html file to make it publicly accessible without making the whole bucket public
---
```
gsutil acl ch -u AllUsers:R gs://bucketname/index.html
```
![Image](https://github.com/Sri-krishna98/GCP/blob/master/Cloud%20Storage-SQL/Q1a.PNG?raw=true)
---
> Click on the index.html file which is now public and copy the Link URL to open the said static website from anywhere
---
![Image](https://github.com/Sri-krishna98/GCP/blob/master/Cloud%20Storage-SQL/Q1b.PNG?raw=true)

# Q2 Download the entire folder (folder1) on the local (cloud shell or vm) using python3 with standard library.
---
> First Create the bucket you want to download locally along with the said spicifications
---
![Image](https://github.com/Sri-krishna98/GCP/blob/master/Cloud%20Storage-SQL/Q2a.PNG?raw=true)
---
> Open cloud shell and create and open a name.py file using the following code
---
```
nano q1.py
```
---
> Use the q1.py code ![Link](https://github.com/Sri-krishna98/GCP/blob/master/Cloud%20Storage-SQL/q1.py) and run it using the following command
---
```
python3 q1.py
```
![Image](https://github.com/Sri-krishna98/GCP/blob/master/Cloud%20Storage-SQL/Q2b.PNG?raw=true)
---
> A local folder is then created
---
