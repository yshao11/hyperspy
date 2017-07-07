"""
The Signal class and its specilized subclasses:

    BaseSignal
        For generic data with arbitrary signal_dimension. All other signal
        classes inherit from this one. It should only be used with none of
        the others is appropriated.
    Signal1D
        For generic data with signal_dimension equal 1, i.e. spectral data of
        n-dimensions. The signal is unbinned by default.
    Signal2D
        For generic data with signal_dimension equal 2, i.e. image data of
        n-dimensions. The signal is unbinned by default.
    ComplexSignal
        For generic complex data with arbitrary signal_dimension.
    ComplexSignal1D
        For generic complex data with signal_dimension equal 1, i.e. spectral
        data of n-dimensions. The signal is unbinned by default.
    ComplexSignal2D
        For generic complex data with signal_dimension equal 2, i.e. image
        data of n-dimensions. The signal is unbinned by default.
    EELSSpectrum
        For electron energy-loss data with signal_dimension equal 1, i.e.
        spectral data of n-dimensions. The signal is binned by default.
    EDSTEMSpectrum
        For electron energy-dispersive X-rays data acquired in a transmission
        electron microscopy with signal_dimension equal 1, i.e.
        spectral data of n-dimensions. The signal is binned by default.
    EDSSEMSpectrum
        For electron energy-dispersive X-rays data acquired in a scanning
        electron microscopy with signal_dimension equal 1, i.e.
        spectral data of n-dimensions. The signal is binned by default.
    DielectricFunction
        For dielectric function data with signal_dimension equal 1. The signal
        is unbinned by default.
    HolographyImage
        For 2D-images taken via electron holography. Electron wave as
        ComplexSignal2D can be reconstructed from them.
"""

# -*- coding: utf-8 -*-
from hyperspy.signal import BaseSignal
from hyperspy._signals.signal1d import Signal1D
from hyperspy._signals.signal2d import Signal2D
from hyperspy._signals.eels import EELSSpectrum
from hyperspy._signals.eds_sem import EDSSEMSpectrum
from hyperspy._signals.eds_tem import EDSTEMSpectrum
from hyperspy._signals.complex_signal import ComplexSignal
from hyperspy._signals.complex_signal1d import ComplexSignal1D
from hyperspy._signals.complex_signal2d import ComplexSignal2D
from hyperspy._signals.dielectric_function import DielectricFunction
from hyperspy._signals.hologram_image import HologramImage
from hyperspy._signals.tem_cbed import CBEDTEM

