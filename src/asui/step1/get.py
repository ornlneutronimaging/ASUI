import glob
import os

from ..utilities.get import Get as MasterGet


class Get(MasterGet):

	def list_of_ipts(self, instrument):
		"""
		return the list of IPTS for the specified instrument
		ex: ['IPTS-0001', 'IPTS-0002']
		"""
		home_folder = self.parent.homepath
		full_path_list_ipts = glob.glob(os.path.join(home_folder, instrument + '/IPTS-*'))
		list_ipts = [os.path.basename(_folder) for _folder in full_path_list_ipts]
		return list_ipts