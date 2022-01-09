#James Elliott
#2/16/2021

#Function of the below code is to take a whole directory of .midi files, and extend each midi file with a desired number of appends
import copy
import mido
from mido import MidiFile
import os

class midoExtend:
	def __init__(self,midiDir):
		self.midiDir = midiDir
	def _mergeCopy(self,midiFilePath, repeatLength = 3, outFile = r'MIDI_1001_extended\tmp\test.mid'):
		"""
		takes in one midi file, appends copies for desired repeatLength, and than saves to outFile
		"""
		mid1 = MidiFile(midiFilePath)
		mid_copies = []

		#setup midi instance for manipulation
		merged_mid = MidiFile()
		merged_mid.ticks_per_beat = mid1.ticks_per_beat
		merged_mid.tracks = mid1.tracks

		for i in range(repeatLength):
			mid_copies.append(copy.deepcopy(mid1))

		for cpy in mid_copies:
			merged_mid.tracks[0] += cpy.tracks[0]

		merged_mid.save(outFile)
	def _dirLoop(self):
		"""
		loops through the input directory of the class, and extends all midi files
		"""
		for subdir, dirs, files in os.walk(self.midiDir):
			for filename in files:
				read_path = subdir + os.sep + filename

				save_path = copy.deepcopy(read_path)
				save_path = save_path.replace("original","extended")

				#takes each file, creates extended version, and than saves to a new folder path with extended in name
				self._mergeCopy(midiFilePath=read_path,repeatLength=5,outFile=save_path)
			print("subdirComplete")
	def runMidiExtend(self):
		"""
		takes in the given directory and saves it to a copy called exntended
		"""
		self._dirLoop()


midi_dir_path_Original = r"F:\OneDrive\Documents\Coding Projects\MIDI_1001_original"
midi_file_path = r"F:\\OneDrive\\Documents\\Coding Projects\\MIDI_1001_original\\r_b progressions\\C\\C vi-IV-I-V [r_b].mid"

mid = midoExtend(midiDir=midi_dir_path_Original)
#mid.runMidiExtend()


#TO DO LIST

#create directory loop that accesses all Midi files & save midi file names for saving purposes

#place everything inside a class
	