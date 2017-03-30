


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'InterfaceTypeIdentity' : {
        'meta_info' : _MetaInfoClass('InterfaceTypeIdentity',
            False, 
            [
            ],
            'ietf-interfaces',
            'interface-type',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.ClassifierEntryStatistics' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.ClassifierEntryStatistics',
            False, 
            [
            _MetaInfoClassMember('classified-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Number of total bytes which filtered
                 to the classifier-entry
                ''',
                'classified_bytes',
                'ietf-qos-target', False),
            _MetaInfoClassMember('classified-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Number of total packets which filtered
                 to the classifier-entry
                ''',
                'classified_pkts',
                'ietf-qos-target', False),
            _MetaInfoClassMember('classified-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Rate of average data flow through the
                 classifier-entry
                ''',
                'classified_rate',
                'ietf-qos-target', False),
            ],
            'ietf-qos-target',
            'classifier-entry-statistics',
            _yang_ns._namespaces['ietf-qos-target'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTwoColorMeterStatistics' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTwoColorMeterStatistics',
            False, 
            [
            _MetaInfoClassMember('conform-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of conform packets
                ''',
                'conform_bytes',
                'ietf-diffserv', False),
            _MetaInfoClassMember('conform-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of conform packets
                ''',
                'conform_pkts',
                'ietf-diffserv', False),
            _MetaInfoClassMember('conform-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic Rate measured as conformimg
                ''',
                'conform_rate',
                'ietf-diffserv', False),
            _MetaInfoClassMember('exceed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of packets counted as exceeding
                ''',
                'exceed_bytes',
                'ietf-diffserv', False),
            _MetaInfoClassMember('exceed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets counted as exceeding
                ''',
                'exceed_pkts',
                'ietf-diffserv', False),
            _MetaInfoClassMember('exceed-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic Rate measured as exceeding
                ''',
                'exceed_rate',
                'ietf-diffserv', False),
            ],
            'ietf-diffserv',
            'one-rate-two-color-meter-statistics',
            _yang_ns._namespaces['ietf-diffserv'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTriColorMeterStatistics' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTriColorMeterStatistics',
            False, 
            [
            _MetaInfoClassMember('conform-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of conform packets
                ''',
                'conform_bytes',
                'ietf-diffserv', False),
            _MetaInfoClassMember('conform-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of conform packets
                ''',
                'conform_pkts',
                'ietf-diffserv', False),
            _MetaInfoClassMember('conform-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic Rate measured as conformimg
                ''',
                'conform_rate',
                'ietf-diffserv', False),
            _MetaInfoClassMember('exceed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of packets counted as exceeding
                ''',
                'exceed_bytes',
                'ietf-diffserv', False),
            _MetaInfoClassMember('exceed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets counted as exceeding
                ''',
                'exceed_pkts',
                'ietf-diffserv', False),
            _MetaInfoClassMember('exceed-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic Rate measured as exceeding
                ''',
                'exceed_rate',
                'ietf-diffserv', False),
            _MetaInfoClassMember('violate-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of packets counted as violating
                ''',
                'violate_bytes',
                'ietf-diffserv', False),
            _MetaInfoClassMember('violate-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets counted as violating
                ''',
                'violate_pkts',
                'ietf-diffserv', False),
            _MetaInfoClassMember('violate-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic Rate measured as violating
                ''',
                'violate_rate',
                'ietf-diffserv', False),
            ],
            'ietf-diffserv',
            'one-rate-tri-color-meter-statistics',
            _yang_ns._namespaces['ietf-diffserv'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.TwoRateTriColorMeterStatistics' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.TwoRateTriColorMeterStatistics',
            False, 
            [
            _MetaInfoClassMember('conform-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of conform packets
                ''',
                'conform_bytes',
                'ietf-diffserv', False),
            _MetaInfoClassMember('conform-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of conform packets
                ''',
                'conform_pkts',
                'ietf-diffserv', False),
            _MetaInfoClassMember('conform-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic Rate measured as conformimg
                ''',
                'conform_rate',
                'ietf-diffserv', False),
            _MetaInfoClassMember('exceed-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of packets counted as exceeding
                ''',
                'exceed_bytes',
                'ietf-diffserv', False),
            _MetaInfoClassMember('exceed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets counted as exceeding
                ''',
                'exceed_pkts',
                'ietf-diffserv', False),
            _MetaInfoClassMember('exceed-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic Rate measured as exceeding
                ''',
                'exceed_rate',
                'ietf-diffserv', False),
            _MetaInfoClassMember('violate-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes of packets counted as violating
                ''',
                'violate_bytes',
                'ietf-diffserv', False),
            _MetaInfoClassMember('violate-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets counted as violating
                ''',
                'violate_pkts',
                'ietf-diffserv', False),
            _MetaInfoClassMember('violate-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Traffic Rate measured as violating
                ''',
                'violate_rate',
                'ietf-diffserv', False),
            ],
            'ietf-diffserv',
            'two-rate-tri-color-meter-statistics',
            _yang_ns._namespaces['ietf-diffserv'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics',
            False, 
            [
            _MetaInfoClassMember('one-rate-tri-color-meter-statistics', REFERENCE_CLASS, 'OneRateTriColorMeterStatistics' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTriColorMeterStatistics', 
                [], [], 
                '''                One rate tri color marker meter statistics
                ''',
                'one_rate_tri_color_meter_statistics',
                'ietf-diffserv', False),
            _MetaInfoClassMember('one-rate-two-color-meter-statistics', REFERENCE_CLASS, 'OneRateTwoColorMeterStatistics' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTwoColorMeterStatistics', 
                [], [], 
                '''                One rate two color marker meter statistics
                ''',
                'one_rate_two_color_meter_statistics',
                'ietf-diffserv', False),
            _MetaInfoClassMember('two-rate-tri-color-meter-statistics', REFERENCE_CLASS, 'TwoRateTriColorMeterStatistics' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.TwoRateTriColorMeterStatistics', 
                [], [], 
                '''                Two rate tri color marker meter statistics
                ''',
                'two_rate_tri_color_meter_statistics',
                'ietf-diffserv', False),
            ],
            'ietf-diffserv',
            'diffserv-action-statistics',
            _yang_ns._namespaces['ietf-diffserv'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics',
            False, 
            [
            _MetaInfoClassMember('classifier-entry-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Classifier Entry Name
                ''',
                'classifier_entry_name',
                'ietf-qos-target', False),
            _MetaInfoClassMember('classifier-entry-statistics', REFERENCE_CLASS, 'ClassifierEntryStatistics' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.ClassifierEntryStatistics', 
                [], [], 
                '''                
                This group defines the classifier filter statistics of
                each classifier entry
                
                ''',
                'classifier_entry_statistics',
                'ietf-qos-target', False),
            _MetaInfoClassMember('diffserv-action-statistics', REFERENCE_CLASS, 'DiffservActionStatistics' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics', 
                [], [], 
                '''                meter statistics
                ''',
                'diffserv_action_statistics',
                'ietf-diffserv', False),
            ],
            'ietf-qos-target',
            'qos-target-classifier-statistics',
            _yang_ns._namespaces['ietf-qos-target'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.QosTargetEntry' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.QosTargetEntry',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_IDENTITY_CLASS, 'DirectionIdentity' , 'ydk.models.ietf.ietf_qos_target', 'DirectionIdentity', 
                [], [], 
                '''                Direction fo the traffic flow either inbound or outbound
                ''',
                'direction',
                'ietf-qos-target', True),
            _MetaInfoClassMember('policy-type', REFERENCE_IDENTITY_CLASS, 'PolicyTypeIdentity' , 'ydk.models.ietf.ietf_qos_policy', 'PolicyTypeIdentity', 
                [], [], 
                '''                Policy entry type
                ''',
                'policy_type',
                'ietf-qos-target', True),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy entry name
                ''',
                'policy_name',
                'ietf-qos-target', False),
            _MetaInfoClassMember('qos-target-classifier-statistics', REFERENCE_LIST, 'QosTargetClassifierStatistics' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics', 
                [], [], 
                '''                Statistics for each Classifier Entry in a Policy
                ''',
                'qos_target_classifier_statistics',
                'ietf-qos-target', False),
            ],
            'ietf-qos-target',
            'qos-target-entry',
            _yang_ns._namespaces['ietf-qos-target'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Optifochrsss.IfCurrentMode' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Optifochrsss.IfCurrentMode',
            False, 
            [
            _MetaInfoClassMember('a-noise-variance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Variance of the radial noise
                component for this mode
                ''',
                'a_noise_variance',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('bits-per-symbol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 This parameter the bits per symbol for
                 this mode.
                ''',
                'bits_per_symbol',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-ber-exponent-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 Exponent of the FEC BER threshold
                ''',
                'fec_ber_exponent_threshold',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-ber-mantissa-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Mantissa of the FEC BER threshold
                ''',
                'fec_ber_mantissa_threshold',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-bitrate', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Fec Overhead rate 
                ''',
                'fec_bitrate',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-gain', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Fec Overhead rate 
                ''',
                'fec_gain',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-info', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Fec Type - eg GFEC
                ''',
                'fec_info',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('i-center', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The In-phase coordinate of the selected
                constellation symbol for this mode
                ''',
                'i_center',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('i-noise-variance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Variance of the in-phase noise
                component for this mode
                ''',
                'i_noise_variance',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-central-frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This parameter indicates the minimum
                 frequency for this template  
                ''',
                'max_central_frequency',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-chromatic-dispersion', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum chromatic dispersion of this
                 mode for this interface
                ''',
                'max_chromatic_dispersion',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-diff-group-delay', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum Differential group delay of this
                 mode for this interface
                ''',
                'max_diff_group_delay',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-input-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                The maximum input power of this
                interface
                ''',
                'max_input_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-laser-temperature', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum Laser Temperature of this mode for
                  this interface
                ''',
                'max_laser_temperature',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-output-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                The maximum output power of this
                interface
                ''',
                'max_output_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-rx-optical-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                Maximum rx optical power of this mode for
                 this interface
                ''',
                'max_rx_optical_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-central-frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This parameter indicates the minimum
                 frequency for this template  
                ''',
                'min_central_frequency',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-chromatic-dispersion', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Minimum chromatic dispersion of this mode
                 for this interface
                ''',
                'min_chromatic_dispersion',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-diff-group-delay', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Minimum Differential group delay of this
                 mode for this interface
                ''',
                'min_diff_group_delay',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-input-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                The minimum input power of this
                interface
                ''',
                'min_input_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-laser-temperature', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Minimum Laser Temperature of this mode for
                  this interface
                ''',
                'min_laser_temperature',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-output-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                The minimum output power of this
                interface
                ''',
                'min_output_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-rx-optical-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                Minimum rx optical power of this mode for
                 this interface
                ''',
                'min_rx_optical_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('mode-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Id for the OCh mode template
                ''',
                'mode_id',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('modulation-format', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Modulation format for this mode
                ''',
                'modulation_format',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('num-symbols-in-alphabet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 This parameter the bits per symbol for
                 this mode.
                ''',
                'num_symbols_in_alphabet',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('number-of-lanes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of optical lanes of this interface
                ''',
                'number_of_lanes',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('osnr-margin', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                OSNR margin to FEC threshold
                ''',
                'osnr_margin',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('p-noise-variance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Variance of the phase noise
                component for this mode
                ''',
                'p_noise_variance',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('q-center', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Quadrature coordinate of the selected
                constellation symbol for this mode
                ''',
                'q_center',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('q-margin', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Q-Factor margin to FEC threshold
                ''',
                'q_margin',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('q-noise-variance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Variance of the quadrature noise
                component for this mode
                ''',
                'q_noise_variance',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('symbols-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 This parameter is the symbol index this
                 mode.
                ''',
                'symbols_index',
                'ietf-ext-xponder-wdm-if', False),
            ],
            'ietf-ext-xponder-wdm-if',
            'if-current-mode',
            _yang_ns._namespaces['ietf-ext-xponder-wdm-if'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Optifochrsss.IfSupportedMode.ModeList' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Optifochrsss.IfSupportedMode.ModeList',
            False, 
            [
            _MetaInfoClassMember('mode-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Id for the OCh mode template
                ''',
                'mode_id',
                'ietf-ext-xponder-wdm-if', True),
            _MetaInfoClassMember('a-noise-variance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Variance of the radial noise
                component for this mode
                ''',
                'a_noise_variance',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('bits-per-symbol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 This parameter the bits per symbol for
                 this mode.
                ''',
                'bits_per_symbol',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-ber-exponent-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 Exponent of the FEC BER threshold
                ''',
                'fec_ber_exponent_threshold',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-ber-mantissa-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Mantissa of the FEC BER threshold
                ''',
                'fec_ber_mantissa_threshold',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-bitrate', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Fec Overhead rate 
                ''',
                'fec_bitrate',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-gain', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Fec Overhead rate 
                ''',
                'fec_gain',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-info', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Fec Type - eg GFEC
                ''',
                'fec_info',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('i-center', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The In-phase coordinate of the selected
                constellation symbol for this mode
                ''',
                'i_center',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('i-noise-variance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Variance of the in-phase noise
                component for this mode
                ''',
                'i_noise_variance',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-central-frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This parameter indicates the minimum
                 frequency for this template  
                ''',
                'max_central_frequency',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-chromatic-dispersion', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum chromatic dispersion of this
                 mode for this interface
                ''',
                'max_chromatic_dispersion',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-diff-group-delay', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum Differential group delay of this
                 mode for this interface
                ''',
                'max_diff_group_delay',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-input-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                The maximum input power of this
                interface
                ''',
                'max_input_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-laser-temperature', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum Laser Temperature of this mode for
                  this interface
                ''',
                'max_laser_temperature',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-output-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                The maximum output power of this
                interface
                ''',
                'max_output_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-rx-optical-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                Maximum rx optical power of this mode for
                 this interface
                ''',
                'max_rx_optical_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-central-frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This parameter indicates the minimum
                 frequency for this template  
                ''',
                'min_central_frequency',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-chromatic-dispersion', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Minimum chromatic dispersion of this mode
                 for this interface
                ''',
                'min_chromatic_dispersion',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-diff-group-delay', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Minimum Differential group delay of this
                 mode for this interface
                ''',
                'min_diff_group_delay',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-input-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                The minimum input power of this
                interface
                ''',
                'min_input_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-laser-temperature', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Minimum Laser Temperature of this mode for
                  this interface
                ''',
                'min_laser_temperature',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-output-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                The minimum output power of this
                interface
                ''',
                'min_output_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-rx-optical-power', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-50', '-30'), ('-10', '5'), ('10000000', 'None')], [], 
                '''                Minimum rx optical power of this mode for
                 this interface
                ''',
                'min_rx_optical_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('modulation-format', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Modulation format for this mode
                ''',
                'modulation_format',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('num-symbols-in-alphabet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 This parameter the bits per symbol for
                 this mode.
                ''',
                'num_symbols_in_alphabet',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('number-of-lanes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of optical lanes of this interface
                ''',
                'number_of_lanes',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('osnr-margin', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                OSNR margin to FEC threshold
                ''',
                'osnr_margin',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('p-noise-variance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Variance of the phase noise
                component for this mode
                ''',
                'p_noise_variance',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('q-center', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Quadrature coordinate of the selected
                constellation symbol for this mode
                ''',
                'q_center',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('q-margin', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Q-Factor margin to FEC threshold
                ''',
                'q_margin',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('q-noise-variance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Variance of the quadrature noise
                component for this mode
                ''',
                'q_noise_variance',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('symbols-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 This parameter is the symbol index this
                 mode.
                ''',
                'symbols_index',
                'ietf-ext-xponder-wdm-if', False),
            ],
            'ietf-ext-xponder-wdm-if',
            'mode-list',
            _yang_ns._namespaces['ietf-ext-xponder-wdm-if'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Optifochrsss.IfSupportedMode' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Optifochrsss.IfSupportedMode',
            False, 
            [
            _MetaInfoClassMember('mode-list', REFERENCE_LIST, 'ModeList' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Optifochrsss.IfSupportedMode.ModeList', 
                [], [], 
                '''                List of the modes 
                ''',
                'mode_list',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('number-of-modes-supported', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of modes
                supported by this interface
                ''',
                'number_of_modes_supported',
                'ietf-ext-xponder-wdm-if', False),
            ],
            'ietf-ext-xponder-wdm-if',
            'if-supported-mode',
            _yang_ns._namespaces['ietf-ext-xponder-wdm-if'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams.ModeList' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams.ModeList',
            False, 
            [
            _MetaInfoClassMember('tca-type', REFERENCE_ENUM_CLASS, 'OptIfOchTcaTypesEnum' , 'ydk.models.ietf.ietf_ext_xponder_wdm_if', 'OptIfOchTcaTypesEnum', 
                [], [], 
                '''                type of the TCA eg TX Power
                ''',
                'tca_type',
                'ietf-ext-xponder-wdm-if', True),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 A TCA is generated if the variable is
                 more than this value
                ''',
                'max_threshold',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 A TCA is generated if the variable is
                 less than this value
                ''',
                'min_threshold',
                'ietf-ext-xponder-wdm-if', False),
            ],
            'ietf-ext-xponder-wdm-if',
            'mode-list',
            _yang_ns._namespaces['ietf-ext-xponder-wdm-if'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams',
            False, 
            [
            _MetaInfoClassMember('central-frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 This parameter indicates the frequency
                 of this interface 
                ''',
                'central_frequency',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('cur-osnr', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 OSNR margin to FEC threshold
                ''',
                'cur_osnr',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('cur-q-factor', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 Q-Factor of the interface
                ''',
                'cur_q_factor',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-ber-exponent', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 Pre fec FEC errored words exponent
                ''',
                'fec_ber_exponent',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('fec-ber-mantissa', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Pre fec FEC errored words mantissa
                ''',
                'fec_ber_mantissa',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('input-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The current input power of this
                interface
                ''',
                'input_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-fec-ber-exponent-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 Max Exponent of the FEC BER threshold
                ''',
                'max_fec_ber_exponent_threshold',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('max-fec-ber-mantissa-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Max Mantissa of the FEC BER threshold
                ''',
                'max_fec_ber_mantissa_threshold',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-fec-ber-exponent-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 Min Exponent of the FEC BER threshold
                ''',
                'min_fec_ber_exponent_threshold',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('min-fec-ber-mantissa-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Min Mantissa of the FEC BER threshold
                ''',
                'min_fec_ber_mantissa_threshold',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('mode-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Id for the OCh mode template
                ''',
                'mode_id',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('mode-list', REFERENCE_LIST, 'ModeList' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams.ModeList', 
                [], [], 
                '''                List of the tcas
                ''',
                'mode_list',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('number-of-tcas-supported', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tcas
                supported by this interface
                ''',
                'number_of_tcas_supported',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('osnr-margin', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 OSNR margin to FEC threshold
                ''',
                'osnr_margin',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('output-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The output power for this interface
                 in .01 dBm.
                 The setting of the output power is
                  optional
                ''',
                'output_power',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('q-margin', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 Q-Factor margin to FEC threshold
                ''',
                'q_margin',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('uncorrected-words', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Post FEC errored words
                ''',
                'uncorrected_words',
                'ietf-ext-xponder-wdm-if', False),
            ],
            'ietf-ext-xponder-wdm-if',
            'current-opt-if-och-mode-params',
            _yang_ns._namespaces['ietf-ext-xponder-wdm-if'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Optifochrsss' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Optifochrsss',
            False, 
            [
            _MetaInfoClassMember('current-opt-if-och-mode-params', REFERENCE_CLASS, 'CurrentOptIfOchModeParams' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams', 
                [], [], 
                '''                Current parameters of
                this interface
                ''',
                'current_opt_if_och_mode_params',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('if-current-mode', REFERENCE_CLASS, 'IfCurrentMode' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Optifochrsss.IfCurrentMode', 
                [], [], 
                '''                Current mode template of the
                interface
                ''',
                'if_current_mode',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('if-supported-mode', REFERENCE_CLASS, 'IfSupportedMode' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Optifochrsss.IfSupportedMode', 
                [], [], 
                '''                Supported mode list of
                this interface
                ''',
                'if_supported_mode',
                'ietf-ext-xponder-wdm-if', False),
            ],
            'ietf-ext-xponder-wdm-if',
            'optIfOChRsSs',
            _yang_ns._namespaces['ietf-ext-xponder-wdm-if'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.OpticalTransport' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.OpticalTransport',
            False, 
            [
            _MetaInfoClassMember('attenuator-value', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-15', '-5')], [], 
                '''                External attenuator value 
                ''',
                'attenuator_value',
                'ietf-opt-parameters-wdm', False),
            _MetaInfoClassMember('channel-power-ref', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-10', '15')], [], 
                '''                Optical power per channel
                ''',
                'channel_power_ref',
                'ietf-opt-parameters-wdm', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-30', '30')], [], 
                '''                Raman and power amplifiers offset
                ''',
                'offset',
                'ietf-opt-parameters-wdm', False),
            _MetaInfoClassMember('tilt-calibration', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-5', '5')], [], 
                '''                Amplifier Tilt tuning
                ''',
                'tilt_calibration',
                'ietf-opt-parameters-wdm', False),
            ],
            'ietf-opt-parameters-wdm',
            'optical-transport',
            _yang_ns._namespaces['ietf-opt-parameters-wdm'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ppp.Authentication.Password' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ppp.Authentication.Password',
            False, 
            [
            _MetaInfoClassMember('cipher', ATTRIBUTE, 'str' , None, None, 
                [], ['$0$.*|$1$[a-zA-Z0-9./]{1,8}$[a-zA-Z0-9./]{22}|$5$(rounds=\\d+$)?[a-zA-Z0-9./]{1,16}$[a-zA-Z0-9./]{43}|$6$(rounds=\\d+$)?[a-zA-Z0-9./]{1,16}$[a-zA-Z0-9./]{86}'], 
                '''                The password for cipher type.
                ''',
                'cipher',
                'ietf-if-ext-ppp', False),
            _MetaInfoClassMember('simple', ATTRIBUTE, 'str' , None, None, 
                [], ['$0$.*|$1$[a-zA-Z0-9./]{1,8}$[a-zA-Z0-9./]{22}|$5$(rounds=\\d+$)?[a-zA-Z0-9./]{1,16}$[a-zA-Z0-9./]{43}|$6$(rounds=\\d+$)?[a-zA-Z0-9./]{1,16}$[a-zA-Z0-9./]{86}'], 
                '''                The password for simple type.
                ''',
                'simple',
                'ietf-if-ext-ppp', False),
            ],
            'ietf-if-ext-ppp',
            'password',
            _yang_ns._namespaces['ietf-if-ext-ppp'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ppp.Authentication' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ppp.Authentication',
            False, 
            [
            _MetaInfoClassMember('chap', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Authentication pap for PPP.
                ''',
                'chap',
                'ietf-if-ext-ppp', False),
            _MetaInfoClassMember('pap', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Authentication pap for PPP.
                ''',
                'pap',
                'ietf-if-ext-ppp', False),
            _MetaInfoClassMember('password', REFERENCE_CLASS, 'Password' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ppp.Authentication.Password', 
                [], [], 
                '''                The password configuraiton sub-tree.
                ''',
                'password',
                'ietf-if-ext-ppp', False),
            _MetaInfoClassMember('user', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                the user name string identifying ppp
                ''',
                'user',
                'ietf-if-ext-ppp', False),
            ],
            'ietf-if-ext-ppp',
            'authentication',
            _yang_ns._namespaces['ietf-if-ext-ppp'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.Ppp' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface.Ppp',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ppp.Authentication', 
                [], [], 
                '''                The authentication configuration subtree.
                ''',
                'authentication',
                'ietf-if-ext-ppp', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf contains the configured, desired state of the
                ppp link-protocol.
                ''',
                'enabled',
                'ietf-if-ext-ppp', False),
            ],
            'ietf-if-ext-ppp',
            'ppp',
            _yang_ns._namespaces['ietf-if-ext-ppp'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces.Interface.LinkUpDownTrapEnableEnum' : _MetaInfoEnum('LinkUpDownTrapEnableEnum', 'ydk.models.ietf.ietf_interfaces',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'ietf-interfaces', _yang_ns._namespaces['ietf-interfaces']),
    'Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                
                A device MAY restrict the allowed values for this leaf,
                possibly depending on the type of the interface.
                For system-controlled interfaces, this leaf is the
                device-specific name of the interface.  The 'config false'
                list /interfaces-state/interface contains the currently
                existing interfaces on the device.
                
                If a client tries to create configuration for a
                system-controlled interface that is not present in the
                /interfaces-state/interface list, the server MAY reject
                the request if the implementation does not support
                pre-provisioning of interfaces or if the name refers to
                an interface that can never exist in the system.  A
                NETCONF server MUST reply with an rpc-error with the
                error-tag 'invalid-value' in this case.
                
                If the device supports pre-provisioning of interface
                configuration, the 'pre-provisioning' feature is
                advertised.
                
                If the device allows arbitrarily named user-controlled
                interfaces, the 'arbitrary-names' feature is advertised.
                
                When a configured user-controlled interface is created by
                the system, it is instantiated with the same name in the
                /interface-state/interface list.
                ''',
                'name',
                'ietf-interfaces', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual description of the interface.
                
                A server implementation MAY map this leaf to the ifAlias
                MIB object.  Such an implementation needs to use some
                mechanism to handle the differences in size and characters
                allowed between this leaf and ifAlias.  The definition of
                such a mechanism is outside the scope of this document.
                
                Since ifAlias is defined to be stored in non-volatile
                storage, the MIB implementation MUST map ifAlias to the
                value of 'description' in the persistently stored
                datastore.
                
                Specifically, if the device supports ':startup', when
                ifAlias is read the device MUST return the value of
                'description' in the 'startup' datastore, and when it is
                written, it MUST be written to the 'running' and 'startup'
                datastores.  Note that it is up to the implementation to
                
                decide whether to modify this single leaf in 'startup' or
                perform an implicit copy-config from 'running' to
                'startup'.
                
                If the device does not support ':startup', ifAlias MUST
                be mapped to the 'description' leaf in the 'running'
                datastore.
                ''',
                'description',
                'ietf-interfaces', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf contains the configured, desired state of the
                interface.
                
                Systems that implement the IF-MIB use the value of this
                leaf in the 'running' datastore to set
                IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
                has been initialized, as described in RFC 2863.
                
                
                
                Changes in this leaf in the 'running' datastore are
                reflected in ifAdminStatus, but if ifAdminStatus is
                changed over SNMP, this leaf is not affected.
                ''',
                'enabled',
                'ietf-interfaces', False),
            _MetaInfoClassMember('link-up-down-trap-enable', REFERENCE_ENUM_CLASS, 'LinkUpDownTrapEnableEnum' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.LinkUpDownTrapEnableEnum', 
                [], [], 
                '''                Controls whether linkUp/linkDown SNMP notifications
                should be generated for this interface.
                
                If this node is not configured, the value 'enabled' is
                operationally used by the server for interfaces that do
                not operate on top of any other interface (i.e., there are
                no 'lower-layer-if' entries), and 'disabled' otherwise.
                ''',
                'link_up_down_trap_enable',
                'ietf-interfaces', False),
            _MetaInfoClassMember('optical-transport', REFERENCE_CLASS, 'OpticalTransport' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.OpticalTransport', 
                [], [], 
                '''                Specific optical-transport Data
                ''',
                'optical_transport',
                'ietf-opt-parameters-wdm', False),
            _MetaInfoClassMember('optIfOChRsSs', REFERENCE_CLASS, 'Optifochrsss' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Optifochrsss', 
                [], [], 
                '''                RsSs path configuration for an interface
                ''',
                'optifochrsss',
                'ietf-ext-xponder-wdm-if', False),
            _MetaInfoClassMember('ppp', REFERENCE_CLASS, 'Ppp' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.Ppp', 
                [], [], 
                '''                A ppp interface must specify the global parameters.
                ''',
                'ppp',
                'ietf-if-ext-ppp', False),
            _MetaInfoClassMember('qos-target-entry', REFERENCE_LIST, 'QosTargetEntry' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface.QosTargetEntry', 
                [], [], 
                '''                policy target for inbound or outbound direction
                ''',
                'qos_target_entry',
                'ietf-qos-target', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'InterfaceTypeIdentity' , 'ydk.models.ietf.ietf_interfaces', 'InterfaceTypeIdentity', 
                [], [], 
                '''                The type of the interface.
                
                When an interface entry is created, a server MAY
                initialize the type leaf with a valid value, e.g., if it
                is possible to derive the type from the name of the
                interface.
                
                If a client tries to set the type of an interface to a
                value that can never be used by the system, e.g., if the
                type is not supported or if the type does not match the
                name of the interface, the server MUST reject the request.
                A NETCONF server MUST reply with an rpc-error with the
                error-tag 'invalid-value' in this case.
                ''',
                'type',
                'ietf-interfaces', False),
            ],
            'ietf-interfaces',
            'interface',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'Interfaces' : {
        'meta_info' : _MetaInfoClass('Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ietf.ietf_interfaces', 'Interfaces.Interface', 
                [], [], 
                '''                The list of configured interfaces on the device.
                
                The operational state of an interface is available in the
                /interfaces-state/interface list.  If the configuration of a
                system-controlled interface cannot be used by the system
                (e.g., the interface hardware present does not match the
                interface type), then the configuration is not applied to
                the system-controlled interface shown in the
                /interfaces-state/interface list.  If the configuration
                of a user-controlled interface cannot be used by the system,
                the configured interface is not instantiated in the
                /interfaces-state/interface list.
                ''',
                'interface',
                'ietf-interfaces', False),
            ],
            'ietf-interfaces',
            'interfaces',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.Statistics' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface.Statistics',
            False, 
            [
            _MetaInfoClassMember('discontinuity-time', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The time on the most recent occasion at which any one or
                more of this interface's counters suffered a
                discontinuity.  If no such discontinuities have occurred
                since the last re-initialization of the local management
                subsystem, then this node contains the time the local
                management subsystem re-initialized itself.
                ''',
                'discontinuity_time',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were addressed to a broadcast
                address at this sub-layer.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_broadcast_pkts',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-discards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of inbound packets that were chosen to be
                discarded even though no errors had been detected to
                prevent their being deliverable to a higher-layer
                protocol.  One possible reason for discarding such a
                packet could be to free up buffer space.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_discards',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                For packet-oriented interfaces, the number of inbound
                packets that contained errors preventing them from being
                deliverable to a higher-layer protocol.  For character-
                oriented or fixed-length interfaces, the number of
                inbound transmission units that contained errors
                preventing them from being deliverable to a higher-layer
                protocol.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_errors',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were addressed to a multicast
                address at this sub-layer.  For a MAC-layer protocol,
                this includes both Group and Functional addresses.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_multicast_pkts',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets received on the interface,
                including framing characters.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_octets',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-unicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets, delivered by this sub-layer to a
                higher (sub-)layer, that were not addressed to a
                multicast or broadcast address at this sub-layer.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_unicast_pkts',
                'ietf-interfaces', False),
            _MetaInfoClassMember('in-unknown-protos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                For packet-oriented interfaces, the number of packets
                received via the interface that were discarded because
                of an unknown or unsupported protocol.  For
                character-oriented or fixed-length interfaces that
                support protocol multiplexing, the number of
                transmission units received via the interface that were
                discarded because of an unknown or unsupported protocol.
                For any interface that does not support protocol
                multiplexing, this counter is not present.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_unknown_protos',
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-broadcast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and that were addressed to a
                broadcast address at this sub-layer, including those
                that were discarded or not sent.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_broadcast_pkts',
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-discards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of outbound packets that were chosen to be
                discarded even though no errors had been detected to
                prevent their being transmitted.  One possible reason
                for discarding such a packet could be to free up buffer
                space.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_discards',
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                For packet-oriented interfaces, the number of outbound
                packets that could not be transmitted because of errors.
                For character-oriented or fixed-length interfaces, the
                number of outbound transmission units that could not be
                transmitted because of errors.
                
                
                
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_errors',
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-multicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and that were addressed to a
                multicast address at this sub-layer, including those
                that were discarded or not sent.  For a MAC-layer
                protocol, this includes both Group and Functional
                addresses.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_multicast_pkts',
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets transmitted out of the
                interface, including framing characters.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_octets',
                'ietf-interfaces', False),
            _MetaInfoClassMember('out-unicast-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets that higher-level protocols
                requested be transmitted, and that were not addressed
                to a multicast or broadcast address at this sub-layer,
                including those that were discarded or not sent.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_unicast_pkts',
                'ietf-interfaces', False),
            ],
            'ietf-interfaces',
            'statistics',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState.Interface.AdminStatusEnum' : _MetaInfoEnum('AdminStatusEnum', 'ydk.models.ietf.ietf_interfaces',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
        }, 'ietf-interfaces', _yang_ns._namespaces['ietf-interfaces']),
    'InterfacesState.Interface.OperStatusEnum' : _MetaInfoEnum('OperStatusEnum', 'ydk.models.ietf.ietf_interfaces',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
            'unknown':'unknown',
            'dormant':'dormant',
            'not-present':'not_present',
            'lower-layer-down':'lower_layer_down',
        }, 'ietf-interfaces', _yang_ns._namespaces['ietf-interfaces']),
    'InterfacesState.Interface' : {
        'meta_info' : _MetaInfoClass('InterfacesState.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                
                A server implementation MAY map this leaf to the ifName
                MIB object.  Such an implementation needs to use some
                mechanism to handle the differences in size and characters
                allowed between this leaf and ifName.  The definition of
                such a mechanism is outside the scope of this document.
                ''',
                'name',
                'ietf-interfaces', True),
            _MetaInfoClassMember('admin-status', REFERENCE_ENUM_CLASS, 'AdminStatusEnum' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.AdminStatusEnum', 
                [], [], 
                '''                The desired state of the interface.
                
                This leaf has the same read semantics as ifAdminStatus.
                ''',
                'admin_status',
                'ietf-interfaces', False),
            _MetaInfoClassMember('higher-layer-if', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                A list of references to interfaces layered on top of this
                interface.
                ''',
                'higher_layer_if',
                'ietf-interfaces', False),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ifIndex value for the ifEntry represented by this
                interface.
                ''',
                'if_index',
                'ietf-interfaces', False),
            _MetaInfoClassMember('last-change', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The time the interface entered its current operational
                state.  If the current state was entered prior to the
                last re-initialization of the local network management
                subsystem, then this node is not present.
                ''',
                'last_change',
                'ietf-interfaces', False),
            _MetaInfoClassMember('lower-layer-if', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                A list of references to interfaces layered underneath this
                interface.
                ''',
                'lower_layer_if',
                'ietf-interfaces', False),
            _MetaInfoClassMember('oper-status', REFERENCE_ENUM_CLASS, 'OperStatusEnum' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.OperStatusEnum', 
                [], [], 
                '''                The current operational state of the interface.
                
                This leaf has the same semantics as ifOperStatus.
                ''',
                'oper_status',
                'ietf-interfaces', False),
            _MetaInfoClassMember('phys-address', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The interface's address at its protocol sub-layer.  For
                example, for an 802.x interface, this object normally
                contains a Media Access Control (MAC) address.  The
                interface's media-specific modules must define the bit
                
                
                and byte ordering and the format of the value of this
                object.  For interfaces that do not have such an address
                (e.g., a serial line), this node is not present.
                ''',
                'phys_address',
                'ietf-interfaces', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                An estimate of the interface's current bandwidth in bits
                per second.  For interfaces that do not vary in
                bandwidth or for those where no accurate estimation can
                be made, this node should contain the nominal bandwidth.
                For interfaces that have no concept of bandwidth, this
                node is not present.
                ''',
                'speed',
                'ietf-interfaces', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface.Statistics', 
                [], [], 
                '''                A collection of interface-related statistics objects.
                ''',
                'statistics',
                'ietf-interfaces', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'InterfaceTypeIdentity' , 'ydk.models.ietf.ietf_interfaces', 'InterfaceTypeIdentity', 
                [], [], 
                '''                The type of the interface.
                ''',
                'type',
                'ietf-interfaces', False),
            ],
            'ietf-interfaces',
            'interface',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
    'InterfacesState' : {
        'meta_info' : _MetaInfoClass('InterfacesState',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ietf.ietf_interfaces', 'InterfacesState.Interface', 
                [], [], 
                '''                The list of interfaces on the device.
                
                System-controlled interfaces created by the system are
                always present in this list, whether they are configured or
                not.
                ''',
                'interface',
                'ietf-interfaces', False),
            ],
            'ietf-interfaces',
            'interfaces-state',
            _yang_ns._namespaces['ietf-interfaces'],
        'ydk.models.ietf.ietf_interfaces'
        ),
    },
}
_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTwoColorMeterStatistics']['meta_info'].parent =_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics']['meta_info']
_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.OneRateTriColorMeterStatistics']['meta_info'].parent =_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics']['meta_info']
_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics.TwoRateTriColorMeterStatistics']['meta_info'].parent =_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics']['meta_info']
_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.ClassifierEntryStatistics']['meta_info'].parent =_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics']['meta_info']
_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics.DiffservActionStatistics']['meta_info'].parent =_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics']['meta_info']
_meta_table['Interfaces.Interface.QosTargetEntry.QosTargetClassifierStatistics']['meta_info'].parent =_meta_table['Interfaces.Interface.QosTargetEntry']['meta_info']
_meta_table['Interfaces.Interface.Optifochrsss.IfSupportedMode.ModeList']['meta_info'].parent =_meta_table['Interfaces.Interface.Optifochrsss.IfSupportedMode']['meta_info']
_meta_table['Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams.ModeList']['meta_info'].parent =_meta_table['Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams']['meta_info']
_meta_table['Interfaces.Interface.Optifochrsss.IfCurrentMode']['meta_info'].parent =_meta_table['Interfaces.Interface.Optifochrsss']['meta_info']
_meta_table['Interfaces.Interface.Optifochrsss.IfSupportedMode']['meta_info'].parent =_meta_table['Interfaces.Interface.Optifochrsss']['meta_info']
_meta_table['Interfaces.Interface.Optifochrsss.CurrentOptIfOchModeParams']['meta_info'].parent =_meta_table['Interfaces.Interface.Optifochrsss']['meta_info']
_meta_table['Interfaces.Interface.Ppp.Authentication.Password']['meta_info'].parent =_meta_table['Interfaces.Interface.Ppp.Authentication']['meta_info']
_meta_table['Interfaces.Interface.Ppp.Authentication']['meta_info'].parent =_meta_table['Interfaces.Interface.Ppp']['meta_info']
_meta_table['Interfaces.Interface.QosTargetEntry']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.Optifochrsss']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.OpticalTransport']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface.Ppp']['meta_info'].parent =_meta_table['Interfaces.Interface']['meta_info']
_meta_table['Interfaces.Interface']['meta_info'].parent =_meta_table['Interfaces']['meta_info']
_meta_table['InterfacesState.Interface.Statistics']['meta_info'].parent =_meta_table['InterfacesState.Interface']['meta_info']
_meta_table['InterfacesState.Interface']['meta_info'].parent =_meta_table['InterfacesState']['meta_info']
