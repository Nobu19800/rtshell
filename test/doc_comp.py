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

Component with lots of documentation.

'''


import OpenRTM_aist
import os
import os.path
import RTC
import sys


class StdComp(OpenRTM_aist.DataFlowComponentBase):
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
        self._param = [0]
        self._df = './test/std_rcvd'

    def onInitialize(self):
        self._data = RTC.TimedLong(RTC.Time(0, 0), 0)
        self._inport = OpenRTM_aist.InPort('in', self._data)
        self._inport.addProperty('description', 'This port receives stuff.')
        self.addInPort('in', self._inport)
        self.bindParameter('param', self._param, "0")
        if os.path.exists(self._df):
            os.remove(self._df)
        return RTC.RTC_OK

    def onExecute(self, ec_id):
        if self._inport.isNew():
            d = self._inport.read().data
            with open(self._df, 'a+') as f:
                f.write('{0}\n'.format(d))
            print(d)
        return RTC.RTC_OK


comp_spec = ['implementation_id', 'Doc',
        'type_name', 'Doc',
        'description', 'Documentation component',
        'version', '1.0',
        'vendor', 'Geoffrey Biggs',
        'category', 'test',
        'activity_type', 'DataFlowComponent',
        'max_instance', '2',
        'language', 'Python',
        'lang_type', 'script',
        'conf.__doc__.__order__', '',
        'conf.__doc__.__license__', 'LGPL3',
        'conf.__doc__.__contact__', 'a@example.com',
        'conf.__doc__.__url__', 'http://www.openrtm.org',
        'conf.__doc__.intro', 'This is the introduction.',
        'conf.__doc__.reqs', 'This component requires nothing.',
        'conf.__doc__.install', 'You cannot install this component.',
        'conf.__doc__.usage', 'You cannot use it, either.',
        'conf.__doc__.misc', 'Miscellaneous is hard to spell.',
        'conf.__doc__.changelog', 'No changes.',
        'conf.__doc__.Another', 'Another section.',
        'conf.default.param', '0',
        'conf.__description__.param', 'A test parameter.',
        '']


def CompInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=comp_spec)
    manager.registerFactory(profile, StdComp, OpenRTM_aist.Delete)


def ModuleInit(manager):
    CompInit(manager)
    manager.createComponent('Doc')


def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(ModuleInit)
    mgr.activateManager()
    mgr.runManager()


if __name__ == '__main__':
    main()

