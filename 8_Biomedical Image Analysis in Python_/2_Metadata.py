#Metadata
#ImageIO reads in data as Image objects. These are standard NumPy arrays with a dictionary of metadata.
#
#Metadata can be quite rich in medical images and can include:
#
#Patient demographics: name, age, sex, clinical information
#Acquisition information: image shape, sampling rates, data type, modality (such as X-Ray, CT or MRI)
#Start this exercise by reading in the chest image and listing the available fields in the meta dictionary.
#
#After reading in the image, use im.meta to select the true statement from the list below.

# Import ImageIO and load image
import imageio
im = imageio.imread('chest-220.dcm')

# Print the available metadata fields
print(im.meta.keys())

#Answer

#odict_keys(['TransferSyntaxUID', 'SOPClassUID', 'SOPInstanceUID', 'StudyDate', 'SeriesDate', 'ContentDate', 'StudyTime', 'SeriesTime', 'ContentTime', 'Modality', 'Manufacturer', 'StudyDescription', 'SeriesDescription', 'PatientName', 'PatientID', 'PatientBirthDate', 'PatientSex', 'PatientWeight', 'StudyInstanceUID', 'SeriesInstanceUID', 'SeriesNumber', 'AcquisitionNumber', 'InstanceNumber', 'ImagePositionPatient', 'ImageOrientationPatient', 'SamplesPerPixel', 'Rows', 'Columns', 'PixelSpacing', 'BitsAllocated', 'BitsStored', 'HighBit', 'PixelRepresentation', 'RescaleIntercept', 'RescaleSlope', 'PixelData', 'shape', 'sampling'])

#Great job! DICOM files have rich information related to patient and acquisition information, but other image formats can have helpful information as well.