#!/usr/bin/python

from pytube import YouTube
import sys
from prettytable import PrettyTable
from time import sleep
from os import getcwd, chdir

class Video():
  
  def __init__(self , id:str , path:str ):
    """
    This gives a better approaach to getting the info regarding the video and download it from different streams.
    : `id`   It is the youtube video id
    : 'path' The absolute path( starting with ~/ ) where you want to save your videos
    """
    
    # Setting up the general information and obtaining the video. 
    self.link = "https://www.youtube.com/"+ id
    self.clip = YouTube( self.link )
    self.save_path=path 
      
    sleep(0.2)
    
    # General information about the video
    self.name = self.clip.title
    self.image = self.clip.thumbnail_url
    
    # Information about the 3 video's streams- audio, video and normal.
    self.audio = self.clip.streams.filter( only_audio = True )
    self.video = self.clip.streams.filter( only_video = True )
    self.normal = self.clip.streams.filter( progressive = True )

  def options(self):
      """This just maps the options given to the given functions."""

      dt_opt = {
          'title' : self.title , 'thumbnail' : self.thumbnail ,  'audio' : self.stream_audio , 'video' : self.stream_video ,  'normal': self.stream_normal , 'stop': self.stop , 'download' : self.download , 'options' : self.display_options
        }

      self.display_options()
      checker1=1

      while( checker1 ):

        print("\n")
        # Input for entering the options
        opt = self.input_comp( "Enter the option" )
        

        if opt not in dt_opt.keys():
          print( "\nSorry, the option which you have entered is incorrect. Try again" )
        else:
          
          # Calling function through the mapping
          ans=dt_opt[opt]()     
          checker1 = ans
        
        self.line()

      print("\nExiting the script for the current video id...........................Done :)\n")

  def display_options(self):
    """This displays different options which can used with the script."""
    dt = PrettyTable( ['Option' , 'Function'] )
    dt.align='c'
    
    dt.add_rows([
      [ 'title' , 'To show the title of the video' ],
      [ 'thumbnail' , 'It gives a link to the video\'s thummbnail' ],
      [ 'video' , 'To show properties of the only video format files' ],
      [ 'audio' , 'To show properties of the only audio format files' ],
      [ 'normal' , 'To show properties of both audio and video format files' ],
      [ 'download' , 'To download the video with the given tag.' ],
      [ 'stop' , 'To quit the options for the current video' ],
      [ 'options' , 'To display options']
    ] )
    
    print("\nThere are different options which you can try. The list of options is given below.")
    print( dt )
    
    return 1

  def input_comp( self , message )->str:
    """It is used to counter some of the errors which can be encountered during the entering of the options or the download link."""
    
    try:
      inp = input(f"{message}: ")
      inp = inp.strip()
      
      return inp
    except KeyboardInterrupt:
      print( "\nYou have interrupted the program. Run the script again to get information about downloading the video" )
      self.stop()
    except EOFError:
      print( "Please enter something in the options bar." )

  def title( self ):
    """This shows the title of the video"""
    
    print( "\n" + self.name )
    return 1
  
  def thumbnail( self ):
    """This gives the link to the thumbnail file"""
        
    print( "\n" + self.image )
    return 1

  def stream_audio( self ):
    """This prints the available options for audio streams."""
    
    dt=PrettyTable(  ['Tag'  , 'Type' , 'Average bit rate (abr)' , 'acodec']  )
    dt.align='c'
    
    for elm in self.audio:
      dt.add_row( [ elm.itag  , elm.type , elm.abr , elm.audio_codec ]  )
    
    print( "\n" , dt )
    
    return 1

  def stream_video(self):
    """This prints the available options for video streams and their properties."""
    
    dt = PrettyTable(  ['Tag' , 'Type' , 'Resolution' , 'Video Codec']  )
    dt.align='c'
    
    for elm in self.video:
      dt.add_row( [ elm.itag , elm.type , elm.resolution , elm.video_codec ]  )

    print( "\n" , dt )
    
    return 1

  def stream_normal( self ):
    """This displays the options for normal video format."""
    
    dt=PrettyTable(  ['Tag' , 'Type' , 'Frames/sec' , 'Resolution' , 'Video Codec' , 'Audio Codec' ]  )
    dt.align='c'
    
    for elm in self.normal:
      dt.add_row( [ elm.itag , 'Normal' , elm.fps , elm.resolution , elm.video_codec , elm.audio_codec ] )
      
    print( "\n" , dt )
    
    return 1

  def download( self ):
    tag=int(  self.input_comp( message = "\nEnter the tag number which you have taken by finding the progressive, audio and video streams" ) )
    vd = self.clip.streams.get_by_itag(tag)

    vd.download(output_path = self.save_path)
    print("\nFinished with the download")

    return 1

  def line(self):
    """It simply provides an ASCII line separator."""
    
    print("\n---------------------------------------------------------------------------------------------------", end="\n" )

  def stop(self)->int:
    """It stops the program from running further."""
    
    return 0

# The Main Script
def main():
  """It takes in the id to the youtube video and returns some other information regarding to it."""
  num_arg = len(sys.argv)
  if(num_arg==1):
    print("There are no options provided")
  else:

    option=sys.argv[1]
    if( option !='-h' and option!='--help'):
      # Getting the path to the home (~) directory
      abs_path=getcwd()
      data=abs_path.split('/')
      try:
        base_path=f"/{data[1]}/{data[2]}"
      except:
        print("You are in a directory which is not home.")

      path_from_home= input("Enter the path from the directory where you want to save the files: ")
      final_path=base_path+"/"+path_from_home
    

    if(option=='-i' or option=='--id'):
      
      if(num_arg==2):
        print("There were no id's given. Type -h or --help for help.")
        return

      for i in range(2,num_arg):

        print(f"Checking for the video with the id number {i-1}............\n")
        ID = sys.argv[i]

        # Checking for the error when the wrong video id is provided
        try:
          vid = Video( ID , final_path )
        except:
          raise Exception( "Sorry, An error has occured. Please check the video id or the video might not be available. Proceeding on to the next video." )
          continue
        
        print( f"Video:  {vid.name}." )
        vid.options()
    
    elif( option=='-r' or option=='--read'):
      
      read_file= abs_path + "/"+sys.argv[2]

      with open(read_file,'r') as videos:
        
        video_id=videos.readlines()
        lines= len(video_id)

        for i in range(0,lines):
          
          print(f"Checking for the video with the id on line number {i+1}............\n")
          ID = video_id[i]

          # Checking for the error when the wrong video id is provided
          try:
            vid = Video( ID , final_path )
          except:
            raise Exception( "Sorry, An error has occured. Please check the video id or the video might not be available. Proceeding on to the next video." )
            continue
        
        print( f"Video:  {vid.name}." )
        vid.options()

    elif( option=='-h' or option=='--help'):
      print("\nThese are the following options:\n   -i or --id\n     Shows general options such as thumbnail link, download options for all the video ids given.\n   -r or --read\n     Show all the available options for the videos id written in separate lines in the file. Takes the files name as the arguement\n   -h or --help\n     Show the help for the command.\n")
      

# Running the script
if __name__ == "__main__":
  main()
