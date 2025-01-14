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

Component with nothing to document.

'''


import OpenRTM_aist
import os
import os.path
import RTC
import sys


class StdComp(OpenRTM_aist.DataFlowComponentBase):
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

    def onExecute(self, ec_id):
        return RTC.RTC_OK


comp_spec = ['implementation_id', 'Doc2',
        'type_name', 'Doc2',
        'description', 'Documentation component',
        'version', '1.0',
        'vendor', 'Geoffrey Biggs',
        'category', 'test',
        'activity_type', 'DataFlowComponent',
        'max_instance', '2',
        'language', 'Python',
        'lang_type', 'script',
        '']


def CompInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=comp_spec)
    manager.registerFactory(profile, StdComp, OpenRTM_aist.Delete)


def ModuleInit(manager):
    CompInit(manager)
    manager.createComponent('Doc2')


def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(ModuleInit)
    mgr.activateManager()
    mgr.runManager()


if __name__ == '__main__':
    main()

