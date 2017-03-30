""" ietf_interfaces 

This module contains a collection of YANG definitions for
managing network interfaces.

Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 7223; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class InterfaceTypeIdentity(object):
    """
    Base identity from which specific interface types are
    derived.
    
    

    """

    _prefix = 'if'
    _revision = '2014-05-08'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_interfaces as meta
        return meta._meta_table['InterfaceTypeIdentity']['meta_info']


class Interfaces(object):
    """
    Interface configuration parameters.
    
    .. attribute:: interface
    
    	The list of configured interfaces on the device.  The operational state of an interface is available in the /interfaces\-state/interface list.  If the configuration of a system\-controlled interface cannot be used by the system (e.g., the interface hardware present does not match the interface type), then the configuration is not applied to the system\-controlled interface shown in the /interfaces\-state/interface list.  If the configuration of a user\-controlled interface cannot be used by the system, the configured interface is not instantiated in the /interfaces\-state/interface list
    	**type**\: list of    :py:class:`Interface <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
    
    

    """

    _prefix = 'if'
    _revision = '2014-05-08'

    def __init__(self):
        self.interface = YList()
        self.interface.parent = self
        self.interface.name = 'interface'


    class Interface(object):
        """
        The list of configured interfaces on the device.
        
        The operational state of an interface is available in the
        /interfaces\-state/interface list.  If the configuration of a
        system\-controlled interface cannot be used by the system
        (e.g., the interface hardware present does not match the
        interface type), then the configuration is not applied to
        the system\-controlled interface shown in the
        /interfaces\-state/interface list.  If the configuration
        of a user\-controlled interface cannot be used by the system,
        the configured interface is not instantiated in the
        /interfaces\-state/interface list.
        
        .. attribute:: name  <key>
        
        	The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system\-controlled interfaces, this leaf is the device\-specific name of the interface.  The 'config false' list /interfaces\-state/interface contains the currently existing interfaces on the device.  If a client tries to create configuration for a system\-controlled interface that is not present in the /interfaces\-state/interface list, the server MAY reject the request if the implementation does not support pre\-provisioning of interfaces or if the name refers to an interface that can never exist in the system.  A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case.  If the device supports pre\-provisioning of interface configuration, the 'pre\-provisioning' feature is advertised.  If the device allows arbitrarily named user\-controlled interfaces, the 'arbitrary\-names' feature is advertised.  When a configured user\-controlled interface is created by the system, it is instantiated with the same name in the /interface\-state/interface list
        	**type**\:  str
        
        .. attribute:: description
        
        	A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non\-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports '\:startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy\-config from 'running' to 'startup'.  If the device does not support '\:startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore
        	**type**\:  str
        
        .. attribute:: enabled
        
        	This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.    Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: link_up_down_trap_enable
        
        	Controls whether linkUp/linkDown SNMP notifications should be generated for this interface.  If this node is not configured, the value 'enabled' is operationally used by the server for interfaces that do not operate on top of any other interface (i.e., there are no 'lower\-layer\-if' entries), and 'disabled' otherwise
        	**type**\:   :py:class:`LinkUpDownTrapEnableEnum <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.LinkUpDownTrapEnableEnum>`
        
        .. attribute:: optical_transport
        
        	Specific optical\-transport Data
        	**type**\:   :py:class:`OpticalTransport <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.OpticalTransport>`
        
        .. attribute:: optifochrsss
        
        	RsSs path configuration for an interface
        	**type**\:   :py:class:`Optifochrsss <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Optifochrsss>`
        
        .. attribute:: ppp
        
        	A ppp interface must specify the global parameters
        	**type**\:   :py:class:`Ppp <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ppp>`
        
        .. attribute:: qos_target_entry
        
        	policy target for inbound or outbound direction
        	**type**\: list of    :py:class:`QosTargetEntry <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.QosTargetEntry>`
        
        .. attribute:: type
        
        	The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case
        	**type**\:   :py:class:`InterfaceTypeIdentity <ydk.models.ietf.ietf_interfaces.InterfaceTypeIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'if'
        _revision = '2014-05-08'

        def __init__(self):
            self.parent = None
            self.name = None
            self.description = None
            self.enabled = None
            self.link_up_down_trap_enable = None
            self.optical_transport = Interfaces.Interface.OpticalTransport()
            self.optical_transport.parent = self
            self.optifochrsss = Interfaces.Interface.Optifochrsss()
            self.optifochrsss.parent = self
            self.ppp = Interfaces.Interface.Ppp()
            self.ppp.parent = self
            self.qos_target_entry = YList()
            self.qos_target_entry.parent = self
            self.qos_target_entry.name = 'qos_target_entry'
            self.type = None

        class LinkUpDownTrapEnableEnum(Enum):
            """
            LinkUpDownTrapEnableEnum

            Controls whether linkUp/linkDown SNMP notifications

            should be generated for this interface.

            If this node is not configured, the value 'enabled' is

            operationally used by the server for interfaces that do

            not operate on top of any other interface (i.e., there are

            no 'lower\-layer\-if' entries), and 'disabled' otherwise.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = 1

            disabled = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['Interfaces.Interface.LinkUpDownTrapEnableEnum']



        class QosTargetEntry(object):
            """
            policy target for inbound or outbound direction
            
            .. attribute:: direction  <key>
            
            	Direction fo the traffic flow either inbound or outbound
            	**type**\:   :py:class:`DirectionIdentity <ydk.models.ietf.ietf_qos_target.DirectionIdentity>`
            
            .. attribute:: policy_type  <key>
            
            	Policy entry type
            	**type**\:   :py:class:`PolicyTypeIdentity <ydk.models.ietf.ietf_qos_policy.PolicyTypeIdentity>`
            
            .. attribute:: policy_name
            
            	Policy entry name
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: qos_target_classifier_statistics
            
            	Statistics for each Classifier Entry in a Policy
            	**type**\: list of    :py:class:`QosTargetClassifierStatistics <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics>`
            
            

            """

            _prefix = 'target'
            _revision = '2016-06-15'

            def __init__(self):
                self.parent = None
                self.direction = None
                self.policy_type = None
                self.policy_name = None
                self.qos_target_classifier_statistics = YList()
                self.qos_target_classifier_statistics.parent = self
                self.qos_target_classifier_statistics.name = 'qos_target_classifier_statistics'


            class QosTargetClassifierStatistics(object):
                """
                Statistics for each Classifier Entry in a Policy
                
                .. attribute:: classifier_entry_name
                
                	Classifier Entry Name
                	**type**\:  str
                
                .. attribute:: classifier_entry_statistics
                
                	 This group defines the classifier filter statistics of each classifier entry 
                	**type**\:   :py:class:`ClassifierEntryStatistics <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.ClassifierEntryStatistics>`
                
                .. attribute:: diffserv_action_statistics
                
                	meter statistics
                	**type**\:   :py:class:`DiffservActionStatistics <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics>`
                
                

                """

                _prefix = 'target'
                _revision = '2016-06-15'

                def __init__(self):
                    self.parent = None
                    self.classifier_entry_name = None
                    self.classifier_entry_statistics = Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.ClassifierEntryStatistics()
                    self.classifier_entry_statistics.parent = self
                    self.diffserv_action_statistics = Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics()
                    self.diffserv_action_statistics.parent = self


                class ClassifierEntryStatistics(object):
                    """
                    
                    This group defines the classifier filter statistics of
                    each classifier entry
                    
                    
                    .. attribute:: classified_bytes
                    
                    	 Number of total bytes which filtered  to the classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_pkts
                    
                    	 Number of total packets which filtered  to the classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_rate
                    
                    	 Rate of average data flow through the  classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bits-per-second
                    
                    

                    """

                    _prefix = 'target'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.classified_bytes = None
                        self.classified_pkts = None
                        self.classified_rate = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-qos-target:classifier-entry-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.classified_bytes is not None:
                            return True

                        if self.classified_pkts is not None:
                            return True

                        if self.classified_rate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.ClassifierEntryStatistics']['meta_info']


                class DiffservActionStatistics(object):
                    """
                    meter statistics
                    
                    .. attribute:: one_rate_tri_color_meter_statistics
                    
                    	One rate tri color marker meter statistics
                    	**type**\:   :py:class:`OneRateTriColorMeterStatistics <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTriColorMeterStatistics>`
                    
                    .. attribute:: one_rate_two_color_meter_statistics
                    
                    	One rate two color marker meter statistics
                    	**type**\:   :py:class:`OneRateTwoColorMeterStatistics <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTwoColorMeterStatistics>`
                    
                    .. attribute:: two_rate_tri_color_meter_statistics
                    
                    	Two rate tri color marker meter statistics
                    	**type**\:   :py:class:`TwoRateTriColorMeterStatistics <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.TwoRateTriColorMeterStatistics>`
                    
                    

                    """

                    _prefix = 'diffserv'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.one_rate_tri_color_meter_statistics = Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTriColorMeterStatistics()
                        self.one_rate_tri_color_meter_statistics.parent = self
                        self.one_rate_two_color_meter_statistics = Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTwoColorMeterStatistics()
                        self.one_rate_two_color_meter_statistics.parent = self
                        self.two_rate_tri_color_meter_statistics = Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.TwoRateTriColorMeterStatistics()
                        self.two_rate_tri_color_meter_statistics.parent = self


                    class OneRateTwoColorMeterStatistics(object):
                        """
                        One rate two color marker meter statistics
                        
                        .. attribute:: conform_bytes
                        
                        	Bytes of conform packets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: conform_pkts
                        
                        	Number of conform packets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: conform_rate
                        
                        	Traffic Rate measured as conformimg
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        .. attribute:: exceed_bytes
                        
                        	Bytes of packets counted as exceeding
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: exceed_pkts
                        
                        	Number of packets counted as exceeding
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: exceed_rate
                        
                        	Traffic Rate measured as exceeding
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        

                        """

                        _prefix = 'diffserv'
                        _revision = '2016-06-15'

                        def __init__(self):
                            self.parent = None
                            self.conform_bytes = None
                            self.conform_pkts = None
                            self.conform_rate = None
                            self.exceed_bytes = None
                            self.exceed_pkts = None
                            self.exceed_rate = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-diffserv:one-rate-two-color-meter-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.conform_bytes is not None:
                                return True

                            if self.conform_pkts is not None:
                                return True

                            if self.conform_rate is not None:
                                return True

                            if self.exceed_bytes is not None:
                                return True

                            if self.exceed_pkts is not None:
                                return True

                            if self.exceed_rate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTwoColorMeterStatistics']['meta_info']


                    class OneRateTriColorMeterStatistics(object):
                        """
                        One rate tri color marker meter statistics
                        
                        .. attribute:: conform_bytes
                        
                        	Bytes of conform packets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: conform_pkts
                        
                        	Number of conform packets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: conform_rate
                        
                        	Traffic Rate measured as conformimg
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        .. attribute:: exceed_bytes
                        
                        	Bytes of packets counted as exceeding
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: exceed_pkts
                        
                        	Number of packets counted as exceeding
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: exceed_rate
                        
                        	Traffic Rate measured as exceeding
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        .. attribute:: violate_bytes
                        
                        	Bytes of packets counted as violating
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: violate_pkts
                        
                        	Number of packets counted as violating
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: violate_rate
                        
                        	Traffic Rate measured as violating
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        

                        """

                        _prefix = 'diffserv'
                        _revision = '2016-06-15'

                        def __init__(self):
                            self.parent = None
                            self.conform_bytes = None
                            self.conform_pkts = None
                            self.conform_rate = None
                            self.exceed_bytes = None
                            self.exceed_pkts = None
                            self.exceed_rate = None
                            self.violate_bytes = None
                            self.violate_pkts = None
                            self.violate_rate = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-diffserv:one-rate-tri-color-meter-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.conform_bytes is not None:
                                return True

                            if self.conform_pkts is not None:
                                return True

                            if self.conform_rate is not None:
                                return True

                            if self.exceed_bytes is not None:
                                return True

                            if self.exceed_pkts is not None:
                                return True

                            if self.exceed_rate is not None:
                                return True

                            if self.violate_bytes is not None:
                                return True

                            if self.violate_pkts is not None:
                                return True

                            if self.violate_rate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTriColorMeterStatistics']['meta_info']


                    class TwoRateTriColorMeterStatistics(object):
                        """
                        Two rate tri color marker meter statistics
                        
                        .. attribute:: conform_bytes
                        
                        	Bytes of conform packets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: conform_pkts
                        
                        	Number of conform packets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: conform_rate
                        
                        	Traffic Rate measured as conformimg
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        .. attribute:: exceed_bytes
                        
                        	Bytes of packets counted as exceeding
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: exceed_pkts
                        
                        	Number of packets counted as exceeding
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: exceed_rate
                        
                        	Traffic Rate measured as exceeding
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        .. attribute:: violate_bytes
                        
                        	Bytes of packets counted as violating
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: violate_pkts
                        
                        	Number of packets counted as violating
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: violate_rate
                        
                        	Traffic Rate measured as violating
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bits-per-second
                        
                        

                        """

                        _prefix = 'diffserv'
                        _revision = '2016-06-15'

                        def __init__(self):
                            self.parent = None
                            self.conform_bytes = None
                            self.conform_pkts = None
                            self.conform_rate = None
                            self.exceed_bytes = None
                            self.exceed_pkts = None
                            self.exceed_rate = None
                            self.violate_bytes = None
                            self.violate_pkts = None
                            self.violate_rate = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-diffserv:two-rate-tri-color-meter-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.conform_bytes is not None:
                                return True

                            if self.conform_pkts is not None:
                                return True

                            if self.conform_rate is not None:
                                return True

                            if self.exceed_bytes is not None:
                                return True

                            if self.exceed_pkts is not None:
                                return True

                            if self.exceed_rate is not None:
                                return True

                            if self.violate_bytes is not None:
                                return True

                            if self.violate_pkts is not None:
                                return True

                            if self.violate_rate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.TwoRateTriColorMeterStatistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-diffserv:diffserv-action-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.one_rate_tri_color_meter_statistics is not None and self.one_rate_tri_color_meter_statistics._has_data():
                            return True

                        if self.one_rate_two_color_meter_statistics is not None and self.one_rate_two_color_meter_statistics._has_data():
                            return True

                        if self.two_rate_tri_color_meter_statistics is not None and self.two_rate_tri_color_meter_statistics._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-qos-target:qos-target-classifier-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.classifier_entry_name is not None:
                        return True

                    if self.classifier_entry_statistics is not None and self.classifier_entry_statistics._has_data():
                        return True

                    if self.diffserv_action_statistics is not None and self.diffserv_action_statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.direction is None:
                    raise YPYModelError('Key property direction is None')
                if self.policy_type is None:
                    raise YPYModelError('Key property policy_type is None')

                return self.parent._common_path +'/ietf-qos-target:qos-target-entry[ietf-qos-target:direction = ' + str(self.direction) + '][ietf-qos-target:policy-type = ' + str(self.policy_type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.direction is not None:
                    return True

                if self.policy_type is not None:
                    return True

                if self.policy_name is not None:
                    return True

                if self.qos_target_classifier_statistics is not None:
                    for child_ref in self.qos_target_classifier_statistics:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['Interfaces.Interface.QosTargetEntry']['meta_info']


        class Optifochrsss(object):
            """
            RsSs path configuration for an interface
            
            .. attribute:: current_opt_if_och_mode_params
            
            	Current parameters of this interface
            	**type**\:   :py:class:`CurrentOptIfOchModeParams <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams>`
            
            .. attribute:: if_current_mode
            
            	Current mode template of the interface
            	**type**\:   :py:class:`IfCurrentMode <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Optifochrsss.IfCurrentMode>`
            
            .. attribute:: if_supported_mode
            
            	Supported mode list of this interface
            	**type**\:   :py:class:`IfSupportedMode <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Optifochrsss.IfSupportedMode>`
            
            

            """

            _prefix = 'ietf-ext-xponder-wdm-if'
            _revision = '2017-03-06'

            def __init__(self):
                self.parent = None
                self.current_opt_if_och_mode_params = Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams()
                self.current_opt_if_och_mode_params.parent = self
                self.if_current_mode = Interfaces.Interface.Optifochrsss.IfCurrentMode()
                self.if_current_mode.parent = self
                self.if_supported_mode = Interfaces.Interface.Optifochrsss.IfSupportedMode()
                self.if_supported_mode.parent = self


            class IfCurrentMode(object):
                """
                Current mode template of the
                interface
                
                .. attribute:: a_noise_variance
                
                	The Variance of the radial noise component for this mode
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: .001
                
                .. attribute:: bits_per_symbol
                
                	 This parameter the bits per symbol for  this mode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: fec_ber_exponent_threshold
                
                	 Exponent of the FEC BER threshold
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: fec_ber_mantissa_threshold
                
                	 Mantissa of the FEC BER threshold
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: fec_bitrate
                
                	Fec Overhead rate 
                	**type**\:  str
                
                	**length:** 1..255
                
                .. attribute:: fec_gain
                
                	Fec Overhead rate 
                	**type**\:  str
                
                	**length:** 1..255
                
                .. attribute:: fec_info
                
                	Fec Type \- eg GFEC
                	**type**\:  str
                
                	**length:** 1..255
                
                .. attribute:: i_center
                
                	The In\-phase coordinate of the selected constellation symbol for this mode
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: .0001
                
                .. attribute:: i_noise_variance
                
                	The Variance of the in\-phase noise component for this mode
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: .001
                
                .. attribute:: max_central_frequency
                
                	This parameter indicates the minimum  frequency for this template  
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_chromatic_dispersion
                
                	Maximum chromatic dispersion of this  mode for this interface
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: max_diff_group_delay
                
                	Maximum Differential group delay of this  mode for this interface
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: max_input_power
                
                	The maximum input power of this interface
                	**type**\:  Decimal64
                
                	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                
                .. attribute:: max_laser_temperature
                
                	Maximum Laser Temperature of this mode for   this interface
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: .01C
                
                .. attribute:: max_output_power
                
                	The maximum output power of this interface
                	**type**\:  Decimal64
                
                	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                
                .. attribute:: max_rx_optical_power
                
                	Maximum rx optical power of this mode for  this interface
                	**type**\:  Decimal64
                
                	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                
                .. attribute:: min_central_frequency
                
                	This parameter indicates the minimum  frequency for this template  
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: min_chromatic_dispersion
                
                	Minimum chromatic dispersion of this mode  for this interface
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: min_diff_group_delay
                
                	Minimum Differential group delay of this  mode for this interface
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: min_input_power
                
                	The minimum input power of this interface
                	**type**\:  Decimal64
                
                	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                
                .. attribute:: min_laser_temperature
                
                	Minimum Laser Temperature of this mode for   this interface
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: .01C
                
                .. attribute:: min_output_power
                
                	The minimum output power of this interface
                	**type**\:  Decimal64
                
                	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                
                .. attribute:: min_rx_optical_power
                
                	Minimum rx optical power of this mode for  this interface
                	**type**\:  Decimal64
                
                	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                
                .. attribute:: mode_id
                
                	Id for the OCh mode template
                	**type**\:  str
                
                	**length:** 1..255
                
                .. attribute:: modulation_format
                
                	Modulation format for this mode
                	**type**\:  str
                
                	**length:** 1..255
                
                .. attribute:: num_symbols_in_alphabet
                
                	 This parameter the bits per symbol for  this mode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_lanes
                
                	Number of optical lanes of this interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: osnr_margin
                
                	OSNR margin to FEC threshold
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: dB
                
                .. attribute:: p_noise_variance
                
                	The Variance of the phase noise component for this mode
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: .001
                
                .. attribute:: q_center
                
                	The Quadrature coordinate of the selected constellation symbol for this mode
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: .0001
                
                .. attribute:: q_margin
                
                	Q\-Factor margin to FEC threshold
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: dB
                
                .. attribute:: q_noise_variance
                
                	The Variance of the quadrature noise component for this mode
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: .001
                
                .. attribute:: symbols_index
                
                	 This parameter is the symbol index this  mode
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ietf-ext-xponder-wdm-if'
                _revision = '2017-03-06'

                def __init__(self):
                    self.parent = None
                    self.a_noise_variance = None
                    self.bits_per_symbol = None
                    self.fec_ber_exponent_threshold = None
                    self.fec_ber_mantissa_threshold = None
                    self.fec_bitrate = None
                    self.fec_gain = None
                    self.fec_info = None
                    self.i_center = None
                    self.i_noise_variance = None
                    self.max_central_frequency = None
                    self.max_chromatic_dispersion = None
                    self.max_diff_group_delay = None
                    self.max_input_power = None
                    self.max_laser_temperature = None
                    self.max_output_power = None
                    self.max_rx_optical_power = None
                    self.min_central_frequency = None
                    self.min_chromatic_dispersion = None
                    self.min_diff_group_delay = None
                    self.min_input_power = None
                    self.min_laser_temperature = None
                    self.min_output_power = None
                    self.min_rx_optical_power = None
                    self.mode_id = None
                    self.modulation_format = None
                    self.num_symbols_in_alphabet = None
                    self.number_of_lanes = None
                    self.osnr_margin = None
                    self.p_noise_variance = None
                    self.q_center = None
                    self.q_margin = None
                    self.q_noise_variance = None
                    self.symbols_index = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-ext-xponder-wdm-if:if-current-mode'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.a_noise_variance is not None:
                        return True

                    if self.bits_per_symbol is not None:
                        return True

                    if self.fec_ber_exponent_threshold is not None:
                        return True

                    if self.fec_ber_mantissa_threshold is not None:
                        return True

                    if self.fec_bitrate is not None:
                        return True

                    if self.fec_gain is not None:
                        return True

                    if self.fec_info is not None:
                        return True

                    if self.i_center is not None:
                        return True

                    if self.i_noise_variance is not None:
                        return True

                    if self.max_central_frequency is not None:
                        return True

                    if self.max_chromatic_dispersion is not None:
                        return True

                    if self.max_diff_group_delay is not None:
                        return True

                    if self.max_input_power is not None:
                        return True

                    if self.max_laser_temperature is not None:
                        return True

                    if self.max_output_power is not None:
                        return True

                    if self.max_rx_optical_power is not None:
                        return True

                    if self.min_central_frequency is not None:
                        return True

                    if self.min_chromatic_dispersion is not None:
                        return True

                    if self.min_diff_group_delay is not None:
                        return True

                    if self.min_input_power is not None:
                        return True

                    if self.min_laser_temperature is not None:
                        return True

                    if self.min_output_power is not None:
                        return True

                    if self.min_rx_optical_power is not None:
                        return True

                    if self.mode_id is not None:
                        return True

                    if self.modulation_format is not None:
                        return True

                    if self.num_symbols_in_alphabet is not None:
                        return True

                    if self.number_of_lanes is not None:
                        return True

                    if self.osnr_margin is not None:
                        return True

                    if self.p_noise_variance is not None:
                        return True

                    if self.q_center is not None:
                        return True

                    if self.q_margin is not None:
                        return True

                    if self.q_noise_variance is not None:
                        return True

                    if self.symbols_index is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Optifochrsss.IfCurrentMode']['meta_info']


            class IfSupportedMode(object):
                """
                Supported mode list of
                this interface
                
                .. attribute:: mode_list
                
                	List of the modes 
                	**type**\: list of    :py:class:`ModeList <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Optifochrsss.IfSupportedMode.ModeList>`
                
                .. attribute:: number_of_modes_supported
                
                	Number of modes supported by this interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ietf-ext-xponder-wdm-if'
                _revision = '2017-03-06'

                def __init__(self):
                    self.parent = None
                    self.mode_list = YList()
                    self.mode_list.parent = self
                    self.mode_list.name = 'mode_list'
                    self.number_of_modes_supported = None


                class ModeList(object):
                    """
                    List of the modes 
                    
                    .. attribute:: mode_id  <key>
                    
                    	Id for the OCh mode template
                    	**type**\:  str
                    
                    	**length:** 1..255
                    
                    .. attribute:: a_noise_variance
                    
                    	The Variance of the radial noise component for this mode
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: .001
                    
                    .. attribute:: bits_per_symbol
                    
                    	 This parameter the bits per symbol for  this mode
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: fec_ber_exponent_threshold
                    
                    	 Exponent of the FEC BER threshold
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: fec_ber_mantissa_threshold
                    
                    	 Mantissa of the FEC BER threshold
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: fec_bitrate
                    
                    	Fec Overhead rate 
                    	**type**\:  str
                    
                    	**length:** 1..255
                    
                    .. attribute:: fec_gain
                    
                    	Fec Overhead rate 
                    	**type**\:  str
                    
                    	**length:** 1..255
                    
                    .. attribute:: fec_info
                    
                    	Fec Type \- eg GFEC
                    	**type**\:  str
                    
                    	**length:** 1..255
                    
                    .. attribute:: i_center
                    
                    	The In\-phase coordinate of the selected constellation symbol for this mode
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: .0001
                    
                    .. attribute:: i_noise_variance
                    
                    	The Variance of the in\-phase noise component for this mode
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: .001
                    
                    .. attribute:: max_central_frequency
                    
                    	This parameter indicates the minimum  frequency for this template  
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_chromatic_dispersion
                    
                    	Maximum chromatic dispersion of this  mode for this interface
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: max_diff_group_delay
                    
                    	Maximum Differential group delay of this  mode for this interface
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: max_input_power
                    
                    	The maximum input power of this interface
                    	**type**\:  Decimal64
                    
                    	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                    
                    .. attribute:: max_laser_temperature
                    
                    	Maximum Laser Temperature of this mode for   this interface
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: .01C
                    
                    .. attribute:: max_output_power
                    
                    	The maximum output power of this interface
                    	**type**\:  Decimal64
                    
                    	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                    
                    .. attribute:: max_rx_optical_power
                    
                    	Maximum rx optical power of this mode for  this interface
                    	**type**\:  Decimal64
                    
                    	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                    
                    .. attribute:: min_central_frequency
                    
                    	This parameter indicates the minimum  frequency for this template  
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min_chromatic_dispersion
                    
                    	Minimum chromatic dispersion of this mode  for this interface
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: min_diff_group_delay
                    
                    	Minimum Differential group delay of this  mode for this interface
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: min_input_power
                    
                    	The minimum input power of this interface
                    	**type**\:  Decimal64
                    
                    	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                    
                    .. attribute:: min_laser_temperature
                    
                    	Minimum Laser Temperature of this mode for   this interface
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: .01C
                    
                    .. attribute:: min_output_power
                    
                    	The minimum output power of this interface
                    	**type**\:  Decimal64
                    
                    	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                    
                    .. attribute:: min_rx_optical_power
                    
                    	Minimum rx optical power of this mode for  this interface
                    	**type**\:  Decimal64
                    
                    	**range:** \-50..\-30 \| \-10..5 \| 10000000..None
                    
                    .. attribute:: modulation_format
                    
                    	Modulation format for this mode
                    	**type**\:  str
                    
                    	**length:** 1..255
                    
                    .. attribute:: num_symbols_in_alphabet
                    
                    	 This parameter the bits per symbol for  this mode
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_lanes
                    
                    	Number of optical lanes of this interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: osnr_margin
                    
                    	OSNR margin to FEC threshold
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: dB
                    
                    .. attribute:: p_noise_variance
                    
                    	The Variance of the phase noise component for this mode
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: .001
                    
                    .. attribute:: q_center
                    
                    	The Quadrature coordinate of the selected constellation symbol for this mode
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: .0001
                    
                    .. attribute:: q_margin
                    
                    	Q\-Factor margin to FEC threshold
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: dB
                    
                    .. attribute:: q_noise_variance
                    
                    	The Variance of the quadrature noise component for this mode
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: .001
                    
                    .. attribute:: symbols_index
                    
                    	 This parameter is the symbol index this  mode
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ietf-ext-xponder-wdm-if'
                    _revision = '2017-03-06'

                    def __init__(self):
                        self.parent = None
                        self.mode_id = None
                        self.a_noise_variance = None
                        self.bits_per_symbol = None
                        self.fec_ber_exponent_threshold = None
                        self.fec_ber_mantissa_threshold = None
                        self.fec_bitrate = None
                        self.fec_gain = None
                        self.fec_info = None
                        self.i_center = None
                        self.i_noise_variance = None
                        self.max_central_frequency = None
                        self.max_chromatic_dispersion = None
                        self.max_diff_group_delay = None
                        self.max_input_power = None
                        self.max_laser_temperature = None
                        self.max_output_power = None
                        self.max_rx_optical_power = None
                        self.min_central_frequency = None
                        self.min_chromatic_dispersion = None
                        self.min_diff_group_delay = None
                        self.min_input_power = None
                        self.min_laser_temperature = None
                        self.min_output_power = None
                        self.min_rx_optical_power = None
                        self.modulation_format = None
                        self.num_symbols_in_alphabet = None
                        self.number_of_lanes = None
                        self.osnr_margin = None
                        self.p_noise_variance = None
                        self.q_center = None
                        self.q_margin = None
                        self.q_noise_variance = None
                        self.symbols_index = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.mode_id is None:
                            raise YPYModelError('Key property mode_id is None')

                        return self.parent._common_path +'/ietf-ext-xponder-wdm-if:mode-list[ietf-ext-xponder-wdm-if:mode-id = ' + str(self.mode_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.mode_id is not None:
                            return True

                        if self.a_noise_variance is not None:
                            return True

                        if self.bits_per_symbol is not None:
                            return True

                        if self.fec_ber_exponent_threshold is not None:
                            return True

                        if self.fec_ber_mantissa_threshold is not None:
                            return True

                        if self.fec_bitrate is not None:
                            return True

                        if self.fec_gain is not None:
                            return True

                        if self.fec_info is not None:
                            return True

                        if self.i_center is not None:
                            return True

                        if self.i_noise_variance is not None:
                            return True

                        if self.max_central_frequency is not None:
                            return True

                        if self.max_chromatic_dispersion is not None:
                            return True

                        if self.max_diff_group_delay is not None:
                            return True

                        if self.max_input_power is not None:
                            return True

                        if self.max_laser_temperature is not None:
                            return True

                        if self.max_output_power is not None:
                            return True

                        if self.max_rx_optical_power is not None:
                            return True

                        if self.min_central_frequency is not None:
                            return True

                        if self.min_chromatic_dispersion is not None:
                            return True

                        if self.min_diff_group_delay is not None:
                            return True

                        if self.min_input_power is not None:
                            return True

                        if self.min_laser_temperature is not None:
                            return True

                        if self.min_output_power is not None:
                            return True

                        if self.min_rx_optical_power is not None:
                            return True

                        if self.modulation_format is not None:
                            return True

                        if self.num_symbols_in_alphabet is not None:
                            return True

                        if self.number_of_lanes is not None:
                            return True

                        if self.osnr_margin is not None:
                            return True

                        if self.p_noise_variance is not None:
                            return True

                        if self.q_center is not None:
                            return True

                        if self.q_margin is not None:
                            return True

                        if self.q_noise_variance is not None:
                            return True

                        if self.symbols_index is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Optifochrsss.IfSupportedMode.ModeList']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-ext-xponder-wdm-if:if-supported-mode'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mode_list is not None:
                        for child_ref in self.mode_list:
                            if child_ref._has_data():
                                return True

                    if self.number_of_modes_supported is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Optifochrsss.IfSupportedMode']['meta_info']


            class CurrentOptIfOchModeParams(object):
                """
                Current parameters of
                this interface
                
                .. attribute:: central_frequency
                
                	 This parameter indicates the frequency  of this interface 
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: cur_osnr
                
                	 OSNR margin to FEC threshold
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: dB
                
                .. attribute:: cur_q_factor
                
                	 Q\-Factor of the interface
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: dB
                
                .. attribute:: fec_ber_exponent
                
                	 Pre fec FEC errored words exponent
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: fec_ber_mantissa
                
                	 Pre fec FEC errored words mantissa
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_power
                
                	The current input power of this interface
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: .01dbm
                
                .. attribute:: max_fec_ber_exponent_threshold
                
                	 Max Exponent of the FEC BER threshold
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: max_fec_ber_mantissa_threshold
                
                	 Max Mantissa of the FEC BER threshold
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: min_fec_ber_exponent_threshold
                
                	 Min Exponent of the FEC BER threshold
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: min_fec_ber_mantissa_threshold
                
                	 Min Mantissa of the FEC BER threshold
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mode_id
                
                	Id for the OCh mode template
                	**type**\:  str
                
                	**length:** 1..255
                
                .. attribute:: mode_list
                
                	List of the tcas
                	**type**\: list of    :py:class:`ModeList <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams.ModeList>`
                
                .. attribute:: number_of_tcas_supported
                
                	Number of tcas supported by this interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: osnr_margin
                
                	 OSNR margin to FEC threshold
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: dB
                
                .. attribute:: output_power
                
                	The output power for this interface  in .01 dBm.  The setting of the output power is   optional
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: .01dbm
                
                .. attribute:: q_margin
                
                	 Q\-Factor margin to FEC threshold
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: dB
                
                .. attribute:: uncorrected_words
                
                	 Post FEC errored words
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ietf-ext-xponder-wdm-if'
                _revision = '2017-03-06'

                def __init__(self):
                    self.parent = None
                    self.central_frequency = None
                    self.cur_osnr = None
                    self.cur_q_factor = None
                    self.fec_ber_exponent = None
                    self.fec_ber_mantissa = None
                    self.input_power = None
                    self.max_fec_ber_exponent_threshold = None
                    self.max_fec_ber_mantissa_threshold = None
                    self.min_fec_ber_exponent_threshold = None
                    self.min_fec_ber_mantissa_threshold = None
                    self.mode_id = None
                    self.mode_list = YList()
                    self.mode_list.parent = self
                    self.mode_list.name = 'mode_list'
                    self.number_of_tcas_supported = None
                    self.osnr_margin = None
                    self.output_power = None
                    self.q_margin = None
                    self.uncorrected_words = None


                class ModeList(object):
                    """
                    List of the tcas
                    
                    .. attribute:: tca_type  <key>
                    
                    	type of the TCA eg TX Power
                    	**type**\:   :py:class:`OptIfOchTcaTypesEnum <ydk.models.ietf.ietf_ext_xponder_wdm_if.OptIfOchTcaTypesEnum>`
                    
                    .. attribute:: max_threshold
                    
                    	 A TCA is generated if the variable is  more than this value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: min_threshold
                    
                    	 A TCA is generated if the variable is  less than this value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ietf-ext-xponder-wdm-if'
                    _revision = '2017-03-06'

                    def __init__(self):
                        self.parent = None
                        self.tca_type = None
                        self.max_threshold = None
                        self.min_threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.tca_type is None:
                            raise YPYModelError('Key property tca_type is None')

                        return self.parent._common_path +'/ietf-ext-xponder-wdm-if:mode-list[ietf-ext-xponder-wdm-if:tca-type = ' + str(self.tca_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.tca_type is not None:
                            return True

                        if self.max_threshold is not None:
                            return True

                        if self.min_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams.ModeList']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-ext-xponder-wdm-if:current-opt-if-och-mode-params'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.central_frequency is not None:
                        return True

                    if self.cur_osnr is not None:
                        return True

                    if self.cur_q_factor is not None:
                        return True

                    if self.fec_ber_exponent is not None:
                        return True

                    if self.fec_ber_mantissa is not None:
                        return True

                    if self.input_power is not None:
                        return True

                    if self.max_fec_ber_exponent_threshold is not None:
                        return True

                    if self.max_fec_ber_mantissa_threshold is not None:
                        return True

                    if self.min_fec_ber_exponent_threshold is not None:
                        return True

                    if self.min_fec_ber_mantissa_threshold is not None:
                        return True

                    if self.mode_id is not None:
                        return True

                    if self.mode_list is not None:
                        for child_ref in self.mode_list:
                            if child_ref._has_data():
                                return True

                    if self.number_of_tcas_supported is not None:
                        return True

                    if self.osnr_margin is not None:
                        return True

                    if self.output_power is not None:
                        return True

                    if self.q_margin is not None:
                        return True

                    if self.uncorrected_words is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ext-xponder-wdm-if:optIfOChRsSs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.current_opt_if_och_mode_params is not None and self.current_opt_if_och_mode_params._has_data():
                    return True

                if self.if_current_mode is not None and self.if_current_mode._has_data():
                    return True

                if self.if_supported_mode is not None and self.if_supported_mode._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['Interfaces.Interface.Optifochrsss']['meta_info']


        class OpticalTransport(object):
            """
            Specific optical\-transport Data
            
            .. attribute:: attenuator_value
            
            	External attenuator value 
            	**type**\:  Decimal64
            
            	**range:** \-15..\-5
            
            .. attribute:: channel_power_ref
            
            	Optical power per channel
            	**type**\:  Decimal64
            
            	**range:** \-10..15
            
            .. attribute:: offset
            
            	Raman and power amplifiers offset
            	**type**\:  Decimal64
            
            	**range:** \-30..30
            
            .. attribute:: tilt_calibration
            
            	Amplifier Tilt tuning
            	**type**\:  Decimal64
            
            	**range:** \-5..5
            
            

            """

            _prefix = 'iietf-opt-parameters-wdm'
            _revision = '2016-10-30'

            def __init__(self):
                self.parent = None
                self.attenuator_value = None
                self.channel_power_ref = None
                self.offset = None
                self.tilt_calibration = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-opt-parameters-wdm:optical-transport'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.attenuator_value is not None:
                    return True

                if self.channel_power_ref is not None:
                    return True

                if self.offset is not None:
                    return True

                if self.tilt_calibration is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['Interfaces.Interface.OpticalTransport']['meta_info']


        class Ppp(object):
            """
            A ppp interface must specify the global parameters.
            
            .. attribute:: authentication
            
            	The authentication configuration subtree
            	**type**\:   :py:class:`Authentication <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ppp.Authentication>`
            
            	**presence node**\: True
            
            .. attribute:: enabled
            
            	This leaf contains the configured, desired state of the ppp link\-protocol
            	**type**\:  bool
            
            	**default value**\: true
            
            

            """

            _prefix = 'ppp'
            _revision = '2016-11-24'

            def __init__(self):
                self.parent = None
                self.authentication = None
                self.enabled = None


            class Authentication(object):
                """
                The authentication configuration subtree.
                
                .. attribute:: chap
                
                	Authentication pap for PPP
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: pap
                
                	Authentication pap for PPP
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: password
                
                	The password configuraiton sub\-tree
                	**type**\:   :py:class:`Password <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ppp.Authentication.Password>`
                
                	**presence node**\: True
                
                .. attribute:: user
                
                	the user name string identifying ppp
                	**type**\:  str
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ppp'
                _revision = '2016-11-24'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.chap = None
                    self.pap = None
                    self.password = None
                    self.user = None


                class Password(object):
                    """
                    The password configuraiton sub\-tree.
                    
                    .. attribute:: cipher
                    
                    	The password for cipher type
                    	**type**\:  str
                    
                    	**pattern:** $0$.\*\|$1$[a\-zA\-Z0\-9./]{1,8}$[a\-zA\-Z0\-9./]{22}\|$5$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{43}\|$6$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{86}
                    
                    .. attribute:: simple
                    
                    	The password for simple type
                    	**type**\:  str
                    
                    	**pattern:** $0$.\*\|$1$[a\-zA\-Z0\-9./]{1,8}$[a\-zA\-Z0\-9./]{22}\|$5$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{43}\|$6$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{86}
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ppp'
                    _revision = '2016-11-24'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.cipher = None
                        self.simple = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-if-ext-ppp:password'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self._is_presence:
                            return True
                        if self.cipher is not None:
                            return True

                        if self.simple is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Ppp.Authentication.Password']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-if-ext-ppp:authentication'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self._is_presence:
                        return True
                    if self.chap is not None:
                        return True

                    if self.pap is not None:
                        return True

                    if self.password is not None and self.password._has_data():
                        return True

                    if self.user is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Ppp.Authentication']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-if-ext-ppp:ppp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.authentication is not None and self.authentication._has_data():
                    return True

                if self.enabled is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['Interfaces.Interface.Ppp']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-interfaces:interfaces/ietf-interfaces:interface[ietf-interfaces:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.description is not None:
                return True

            if self.enabled is not None:
                return True

            if self.link_up_down_trap_enable is not None:
                return True

            if self.optical_transport is not None and self.optical_transport._has_data():
                return True

            if self.optifochrsss is not None and self.optifochrsss._has_data():
                return True

            if self.ppp is not None and self.ppp._has_data():
                return True

            if self.qos_target_entry is not None:
                for child_ref in self.qos_target_entry:
                    if child_ref._has_data():
                        return True

            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_interfaces as meta
            return meta._meta_table['Interfaces.Interface']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-interfaces:interfaces'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.interface is not None:
            for child_ref in self.interface:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_interfaces as meta
        return meta._meta_table['Interfaces']['meta_info']


class InterfacesState(object):
    """
    Data nodes for the operational state of interfaces.
    
    .. attribute:: interface
    
    	The list of interfaces on the device.  System\-controlled interfaces created by the system are always present in this list, whether they are configured or not
    	**type**\: list of    :py:class:`Interface <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
    
    

    """

    _prefix = 'if'
    _revision = '2014-05-08'

    def __init__(self):
        self.interface = YList()
        self.interface.parent = self
        self.interface.name = 'interface'


    class Interface(object):
        """
        The list of interfaces on the device.
        
        System\-controlled interfaces created by the system are
        always present in this list, whether they are configured or
        not.
        
        .. attribute:: name  <key>
        
        	The name of the interface.  A server implementation MAY map this leaf to the ifName MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifName.  The definition of such a mechanism is outside the scope of this document
        	**type**\:  str
        
        .. attribute:: admin_status
        
        	The desired state of the interface.  This leaf has the same read semantics as ifAdminStatus
        	**type**\:   :py:class:`AdminStatusEnum <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.AdminStatusEnum>`
        
        	**mandatory**\: True
        
        .. attribute:: higher_layer_if
        
        	A list of references to interfaces layered on top of this interface
        	**type**\:  list of str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
        
        .. attribute:: if_index
        
        	The ifIndex value for the ifEntry represented by this interface
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        	**mandatory**\: True
        
        .. attribute:: last_change
        
        	The time the interface entered its current operational state.  If the current state was entered prior to the last re\-initialization of the local network management subsystem, then this node is not present
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: lower_layer_if
        
        	A list of references to interfaces layered underneath this interface
        	**type**\:  list of str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
        
        .. attribute:: oper_status
        
        	The current operational state of the interface.  This leaf has the same semantics as ifOperStatus
        	**type**\:   :py:class:`OperStatusEnum <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.OperStatusEnum>`
        
        	**mandatory**\: True
        
        .. attribute:: phys_address
        
        	The interface's address at its protocol sub\-layer.  For example, for an 802.x interface, this object normally contains a Media Access Control (MAC) address.  The interface's media\-specific modules must define the bit   and byte ordering and the format of the value of this object.  For interfaces that do not have such an address (e.g., a serial line), this node is not present
        	**type**\:  str
        
        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
        
        .. attribute:: speed
        
        	An estimate of the interface's current bandwidth in bits per second.  For interfaces that do not vary in bandwidth or for those where no accurate estimation can be made, this node should contain the nominal bandwidth. For interfaces that have no concept of bandwidth, this node is not present
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bits/second
        
        .. attribute:: statistics
        
        	A collection of interface\-related statistics objects
        	**type**\:   :py:class:`Statistics <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Statistics>`
        
        .. attribute:: type
        
        	The type of the interface
        	**type**\:   :py:class:`InterfaceTypeIdentity <ydk.models.ietf.ietf_interfaces.InterfaceTypeIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'if'
        _revision = '2014-05-08'

        def __init__(self):
            self.parent = None
            self.name = None
            self.admin_status = None
            self.higher_layer_if = YLeafList()
            self.higher_layer_if.parent = self
            self.higher_layer_if.name = 'higher_layer_if'
            self.if_index = None
            self.last_change = None
            self.lower_layer_if = YLeafList()
            self.lower_layer_if.parent = self
            self.lower_layer_if.name = 'lower_layer_if'
            self.oper_status = None
            self.phys_address = None
            self.speed = None
            self.statistics = InterfacesState.Interface.Statistics()
            self.statistics.parent = self
            self.type = None

        class AdminStatusEnum(Enum):
            """
            AdminStatusEnum

            The desired state of the interface.

            This leaf has the same read semantics as ifAdminStatus.

            .. data:: up = 1

            	Ready to pass packets.

            .. data:: down = 2

            	Not ready to pass packets and not in some test mode.

            .. data:: testing = 3

            	In some test mode.

            """

            up = 1

            down = 2

            testing = 3


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.AdminStatusEnum']


        class OperStatusEnum(Enum):
            """
            OperStatusEnum

            The current operational state of the interface.

            This leaf has the same semantics as ifOperStatus.

            .. data:: up = 1

            	Ready to pass packets.

            .. data:: down = 2

            	The interface does not pass any packets.

            .. data:: testing = 3

            	In some test mode.  No operational packets can

            	be passed.

            .. data:: unknown = 4

            	Status cannot be determined for some reason.

            .. data:: dormant = 5

            	Waiting for some external event.

            .. data:: not_present = 6

            	Some component (typically hardware) is missing.

            .. data:: lower_layer_down = 7

            	Down due to state of lower-layer interface(s).

            """

            up = 1

            down = 2

            testing = 3

            unknown = 4

            dormant = 5

            not_present = 6

            lower_layer_down = 7


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.OperStatusEnum']



        class Statistics(object):
            """
            A collection of interface\-related statistics objects.
            
            .. attribute:: discontinuity_time
            
            	The time on the most recent occasion at which any one or more of this interface's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this node contains the time the local management subsystem re\-initialized itself
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            	**mandatory**\: True
            
            .. attribute:: in_broadcast_pkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_discards
            
            	The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_errors
            
            	For packet\-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol.  For character\- oriented or fixed\-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher\-layer protocol.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_multicast_pkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a multicast address at this sub\-layer.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_octets
            
            	The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_unicast_pkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were not addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_unknown_protos
            
            	For packet\-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character\-oriented or fixed\-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_broadcast_pkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_discards
            
            	The number of outbound packets that were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_errors
            
            	For packet\-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character\-oriented or fixed\-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.     Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_multicast_pkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_octets
            
            	The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_unicast_pkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and that were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'if'
            _revision = '2014-05-08'

            def __init__(self):
                self.parent = None
                self.discontinuity_time = None
                self.in_broadcast_pkts = None
                self.in_discards = None
                self.in_errors = None
                self.in_multicast_pkts = None
                self.in_octets = None
                self.in_unicast_pkts = None
                self.in_unknown_protos = None
                self.out_broadcast_pkts = None
                self.out_discards = None
                self.out_errors = None
                self.out_multicast_pkts = None
                self.out_octets = None
                self.out_unicast_pkts = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-interfaces:statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.discontinuity_time is not None:
                    return True

                if self.in_broadcast_pkts is not None:
                    return True

                if self.in_discards is not None:
                    return True

                if self.in_errors is not None:
                    return True

                if self.in_multicast_pkts is not None:
                    return True

                if self.in_octets is not None:
                    return True

                if self.in_unicast_pkts is not None:
                    return True

                if self.in_unknown_protos is not None:
                    return True

                if self.out_broadcast_pkts is not None:
                    return True

                if self.out_discards is not None:
                    return True

                if self.out_errors is not None:
                    return True

                if self.out_multicast_pkts is not None:
                    return True

                if self.out_octets is not None:
                    return True

                if self.out_unicast_pkts is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.Statistics']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-interfaces:interfaces-state/ietf-interfaces:interface[ietf-interfaces:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.admin_status is not None:
                return True

            if self.higher_layer_if is not None:
                for child in self.higher_layer_if:
                    if child is not None:
                        return True

            if self.if_index is not None:
                return True

            if self.last_change is not None:
                return True

            if self.lower_layer_if is not None:
                for child in self.lower_layer_if:
                    if child is not None:
                        return True

            if self.oper_status is not None:
                return True

            if self.phys_address is not None:
                return True

            if self.speed is not None:
                return True

            if self.statistics is not None and self.statistics._has_data():
                return True

            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_interfaces as meta
            return meta._meta_table['InterfacesState.Interface']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-interfaces:interfaces-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.interface is not None:
            for child_ref in self.interface:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_interfaces as meta
        return meta._meta_table['InterfacesState']['meta_info']


