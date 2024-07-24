#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import fec
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx



from gnuradio import qtgui

class new(gr.top_block, Qt.QWidget):

    def __init__(self, MTU=1500, puncpat='11'):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "new")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.MTU = MTU
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.k = k = 7
        self.samp_rate = samp_rate = 32000
        self.rep_0 = rep_0 = 3
        self.rep = rep = 3
        self.rate_0 = rate_0 = 2
        self.polys_0 = polys_0 = [109, 79]
        self.k_0 = k_0 = 7
        self.file_name = file_name = '/home/mihiran/Documents/bin10k.bin'
        self.enc_cc_0 = enc_cc_0 = fec.cc_encoder_make(MTU*8,k, rate, polys, 0, fec.CC_TERMINATED, True)
        self.enc_cc = enc_cc = fec.cc_encoder_make(MTU*8,k, rate, polys, 0, fec.CC_TERMINATED, True)
        self.dec_cc_0 = dec_cc_0 = list(map( (lambda a: fec.cc_decoder.make(MTU*8,k, rate, polys, 0, -1, fec.CC_TERMINATED, True)),range(0,1)))
        self.dec_cc = dec_cc = list(map( (lambda a: fec.cc_decoder.make(MTU*8,k, rate, polys, 0, -1, fec.CC_TERMINATED, True)),range(0,1)))
        self.bpsk = bpsk = digital.constellation_bpsk().base()

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 300)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self._file_name_tool_bar = Qt.QToolBar(self)
        self._file_name_tool_bar.addWidget(Qt.QLabel("'file_name'" + ": "))
        self._file_name_line_edit = Qt.QLineEdit(str(self.file_name))
        self._file_name_tool_bar.addWidget(self._file_name_line_edit)
        self._file_name_line_edit.returnPressed.connect(
            lambda: self.set_file_name(str(str(self._file_name_line_edit.text()))))
        self.top_layout.addWidget(self._file_name_tool_bar)
        self.fec_extended_tagged_encoder_0_1 = fec.extended_tagged_encoder(encoder_obj_list=enc_cc, puncpat='11', lentagname="packet_len", mtu=MTU)
        self.fec_extended_tagged_decoder_2 = self.fec_extended_tagged_decoder_2 = fec_extended_tagged_decoder_2 = fec.extended_tagged_decoder(decoder_obj_list=dec_cc, ann=None, puncpat=puncpat, integration_period=10000, lentagname="packet_len", mtu=MTU)
        self.digital_map_bb_0_0 = digital.map_bb([-1, 1])
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 20, "packet_len")
        self.blocks_repack_bits_bb_1_0 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, 'packet_len', False, gr.GR_LSB_FIRST)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, './sound.mp3', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, './output.png', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_char_to_float_1_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_char_to_float_1_1, 0), (self.fec_extended_tagged_decoder_2, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.fec_extended_tagged_encoder_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_char_to_float_1_1, 0))
        self.connect((self.fec_extended_tagged_decoder_2, 0), (self.blocks_repack_bits_bb_1, 0))
        self.connect((self.fec_extended_tagged_encoder_0_1, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0_1, 0), (self.blocks_repack_bits_bb_1_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "new")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_MTU(self):
        return self.MTU

    def set_MTU(self, MTU):
        self.MTU = MTU

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_rep_0(self):
        return self.rep_0

    def set_rep_0(self, rep_0):
        self.rep_0 = rep_0

    def get_rep(self):
        return self.rep

    def set_rep(self, rep):
        self.rep = rep

    def get_rate_0(self):
        return self.rate_0

    def set_rate_0(self, rate_0):
        self.rate_0 = rate_0

    def get_polys_0(self):
        return self.polys_0

    def set_polys_0(self, polys_0):
        self.polys_0 = polys_0

    def get_k_0(self):
        return self.k_0

    def set_k_0(self, k_0):
        self.k_0 = k_0

    def get_file_name(self):
        return self.file_name

    def set_file_name(self, file_name):
        self.file_name = file_name
        Qt.QMetaObject.invokeMethod(self._file_name_line_edit, "setText", Qt.Q_ARG("QString", str(self.file_name)))

    def get_enc_cc_0(self):
        return self.enc_cc_0

    def set_enc_cc_0(self, enc_cc_0):
        self.enc_cc_0 = enc_cc_0

    def get_enc_cc(self):
        return self.enc_cc

    def set_enc_cc(self, enc_cc):
        self.enc_cc = enc_cc

    def get_dec_cc_0(self):
        return self.dec_cc_0

    def set_dec_cc_0(self, dec_cc_0):
        self.dec_cc_0 = dec_cc_0

    def get_dec_cc(self):
        return self.dec_cc

    def set_dec_cc(self, dec_cc):
        self.dec_cc = dec_cc

    def get_bpsk(self):
        return self.bpsk

    def set_bpsk(self, bpsk):
        self.bpsk = bpsk



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--MTU", dest="MTU", type=intx, default=1500,
        help="Set MTU [default=%(default)r]")
    return parser


def main(top_block_cls=new, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(MTU=options.MTU)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
