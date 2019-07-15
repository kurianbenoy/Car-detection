import numpy as np
import pandas as pd
import logging
import cv2
import os
import pathlib

class CarDataset:
    def __init__(self, root, transform=None, target_transform=None):
		"""Dataset for VOC data.
		Args:
				root: the root of the VOC2007 or VOC2012 dataset, the directory contains the following sub-directories:
						Annotations, ImageSets, JPEGImages, SegmentationClass, SegmentationObject.
		"""
		self.root = pathlib.Path(root)
		self.transform = transform
		self.target_transform = target_transform	
        logging.info("No labels file, using default VOC classes.")
        self.class_names = ('Car', 'Truck', 'Pedestrian','BACKGROUND')
		self.class_dict = {class_name: i for i,
						   class_name in enumerate(self.class_names)}
        df = pd.read_csv('object-detection-crowdai/labels.csv')
		imagelist = df['Frame'].unique().tolist()
		boxes = {}
		labels = {}
		for i in imagelist:
			count = i
			li = int(count.split('.')[0])
			data = df[df["Frame"] == count]
		
			boxes[li] = (data.iloc[:,:4].values)
			labels[li] = data.iloc[:,5].values
			box_l = len(boxes)
		
		# remove ids
		#self.remove_ids() 

    def __getitem__(self, index):
		image_id = self.ids[index]
		boxes, labels = self._get_annotation(image_id)
        
        boxes = 
        labels = df['Labels']
		# if not self.keep_difficult:
		# 	boxes = boxes[is_difficult == 0]
		# 	labels = labels[is_difficult == 0]
		image = self._read_image(image_id)
		#print(image.shape)
		#print(boxes.shape)
		if self.transform:
			image, boxes, labels = self.transform(image, boxes, labels)
		if self.target_transform:
			boxes, labels = self.target_transform(boxes, labels)

		return image, boxes, labels