from pytube import YouTube
import sys


# testing video id
# kOYcbod5J0w
# RuYC6U3LBRs

class VIDEO():
  
  def __init__(self,id:str):
    """
    This gives a better approaach to getting the info regarding the video and download it from different streams.
    : `id`  It is the youtube video id
    
    """
    self.link = "https://www.youtube.com/"+ id
    self.clip = YouTube( self.link )
    
    # General information about the video
    self.name = self.clip.title
    self.image = self.clip.thumbnail_url
    
    # Information about the 3 video's streams- audio, video and normal.
    self.audio = self.clip.streams.filter( only_audio = True )
    self.video = self.clip.streams.filter( only_video = True )
    self.normal = self.clip.streams.filter( progressive = True )
    
  def title( self ):
    print( self.name )
    
  def thumbnail( self ):
    print( self.image )  

  def stream_audio( self ):
    
    for id in stream:
      print(id,end="\n")

  def stream_video(samp):
    stream  = samp.streams.filter(only_video=True)
    for id in stream:
      print(id,end="\n")

  def NORMAL(samp):
    stream  = samp.streams.filter(progressive=True)
    for id in stream:
      print(id,end="\n")

  def DOWNLOAD(samp):
    tag=int(  input("\nEnter the tag number which you have taken by finding the progressive, audio and video streams\n")  )
    vd=samp.streams.get_by_itag(tag)

    vd.download(output_path='Videos/yt')
    print("Finished with the download")

  def options(chc,samp)->int:
    """This just maps the options given to the given functions."""

    if chc==0:
      print(TITLE(samp))

    elif chc==1:
      THUMBNAIL(samp)
    elif chc==2:
      AUDIO_STREAM(samp)
    elif chc==3:
      VIDEO_STREAM(samp)
    elif chc==4:
      NORMAL(samp)
    elif chc==5:
      DOWNLOAD(samp)
      print("Download Finished....")

    elif chc==6:
      print("\nFinishing with the current video.......\n---------------------------------------------------------------------------------------------------------------------------------------------------")
      return 0

    return 1


  # The Main Script
def main():
  """It takes in the id to the youtube video and returns some other information regarding to it."""

  num_arg = len(sys.argv)
  if(num_arg==1):
    print("There are no video id's provided")

  else:
    # Creating the link for the video
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    VIDEO()
    for i in range(1,num_arg):
      
      print(f"Checking for the video with the id number {i}............\n")
      inp=sys.argv[i]
      LINK="https://www.youtube.com/"+ inp

      try:
        video = yt(LINK)
      except:
        print("\nThe video id is not valid or there is some other error which is encountered.\n")
        continue

      print(f"Video:  {TITLE(video)}.\nThere are various options which you can enter and try:\n\n'title'   To get the title of the video.\n'thumb'  To get the thumbnail of the video.\n'video'  To get the options for only-video downloading.\n'audio'  To get options for only-audio downloading.\n'normal'  To get options for a file containing both audio and video.\n'download'  To download the video\n'stop'  To stop the processing for the current video.")
      dt={
        'title':0,  'thumb':1,  'audio':2,  'video':3,  'normal':4, 'stop':6, 'download':5
      }

      per=1
      c1=0
      while(per):
        opt=input("\nPlease Enter your option: ").lower()

        try:
          valid=options(dt[opt],video)
        except:
          print("Sorry, You have entered invalid command.\n")
          c1+=1
          if c1==5:
            per=0
        finally:
          try: per=valid; 
          except: per=0

  print("\nExiting the script...........................Done :)")

# Running the script
if __name__ == "__main__":
  main()