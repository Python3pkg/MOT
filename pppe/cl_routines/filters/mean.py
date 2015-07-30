from .base import AbstractFilter, AbstractFilterWorker
from ...utils import get_cl_double_extension_definer

__author__ = 'Robbert Harms'
__date__ = "2014-04-26"
__license__ = "LGPL v3"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class MeanFilter(AbstractFilter):

    def _get_worker(self, *args):
        """Create the worker that we will use in the computations.

        This is supposed to be overwritten by the implementing filterer.

        Returns:
            the worker object
        """
        return _MeanFilterWorker(self, *args)


class _MeanFilterWorker(AbstractFilterWorker):

    def _get_kernel_source(self):
        kernel_source = get_cl_double_extension_definer(self._cl_environment.platform)
        kernel_source += self._get_ks_sub2ind_func(self._volume_shape)
        kernel_source += '''
            __kernel void filter(
                global double* volume,
                ''' + ('global char* mask,' if self._use_mask else '') + '''
                global double* results
                ){
                    ''' + self._get_ks_dimension_inits(len(self._volume_shape)) + '''
                    int ind = ''' + self._get_ks_sub2ind_func_call(len(self._volume_shape)) + ''';

                    ''' + ('if(mask[ind] > 0){' if self._use_mask else 'if(true){') + '''
                        ''' + self._get_ks_dimension_sizes(self._volume_shape) + '''

                        double sum = 0.0;
                        int count = 0;

                        ''' + self._get_ks_loop(self._volume_shape) + '''

                        results[ind] = sum/count;
                    }
            }
        '''
        return kernel_source

    def _get_ks_loop(self, volume_shape):
        s = ''
        for i in range(len(volume_shape)):
            s += 'for(dim' + repr(i) + ' = dim' + repr(i) + '_start; dim' + repr(i) + \
                 ' < dim' + repr(i) + '_end; dim' + repr(i) + '++){' + "\n"

        if self._use_mask:
            s += 'if(mask[' + self._get_ks_sub2ind_func_call(len(volume_shape)) + '] > 0){' + "\n"

        s += 'sum += volume[' + self._get_ks_sub2ind_func_call(len(volume_shape)) + '];' + "\n"
        s += 'count++;' + "\n"

        if self._use_mask:
            s += '}' + "\n"

        for i in range(len(volume_shape)):
            s += '}' + "\n"
        return s