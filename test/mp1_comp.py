#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Python -*-


'''rtshell

Copyright (C) 2009-2015
    Geoffrey Biggs
    RT-Synthesis Research Group
    Intelligent Systems Research Institute,
    National Institute of Advanced Industrial Science and Technology (AIST),
    Japan
    All rights reserved.
Licensed under the GNU Lesser General Public License version 3.
http://www.gnu.org/licenses/lgpl-3.0.en.html

Component with multiple ports for tests.

'''


import OpenRTM_aist
import os
import os.path
import RTC
import sys


class MPComp(OpenRTM_aist.DataFlowComponentBase):
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

    def onInitialize(self):
        self._in_data = RTC.TimedLong(RTC.Time(0, 0), 0)
        self._inport = OpenRTM_aist.InPort('in', self._in_data)
        self.addInPort('in', self._inport)
        self._out_data = RTC.TimedLong(RTC.Time(0, 0), 0)
        self._outport = OpenRTM_aist.OutPort('out', self._out_data)
        self.addOutPort('out', self._outport)
        return RTC.RTC_OK

    def onExecute(self, ec_id):
        return RTC.RTC_OK


comp_spec = ['implementation_id', 'MP',
        'type_name', 'MP',
        'description', 'Standard component',
        'version', '1.0',
        'vendor', 'Geoffrey Biggs',
        'category', 'test',
        'activity_type', 'DataFlowComponent',
        'max_instance', '2',
        'language', 'Python',
        'lang_type', 'script',
        'conf.default.param', '0',
        '']


def CompInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=comp_spec)
    manager.registerFactory(profile, MPComp, OpenRTM_aist.Delete)


def ModuleInit(manager):
    CompInit(manager)
    manager.createComponent('MP')


def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(ModuleInit)
    mgr.activateManager()
    mgr.runManager()


if __name__ == '__main__':
    main()

