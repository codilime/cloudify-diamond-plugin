# coding=utf-8

"""
Collect swap memory statistics

#### Dependencies

 * psutil

 """

import psutil

import diamond.collector


class SwapCollector(diamond.collector.Collector):

    def get_default_config_help(self):
        config_help = super(SwapCollector, self).get_default_config_help()
        config_help.update({})
        return config_help

    def get_default_config(self):
        """
        Returns the default collector settings
        """
        config = super(SwapCollector, self).get_default_config()
        config.update({
            'path': 'swap',
            'swap_percentage_threshold': 1
        })
        return config

    def collect(self):
        swap_stats = psutil.swap_memory()
        if swap_stats.percent >= int(self.config['swap_percentage_threshold']):
            self.publish('swap_usage', swap_stats.percent)
