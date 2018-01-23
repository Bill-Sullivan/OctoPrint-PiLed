# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.
import os
import octoprint.plugin
#os.system('python test.py')
class PiledPlugin(octoprint.plugin.SettingsPlugin,
                  octoprint.plugin.AssetPlugin,
                  octoprint.plugin.TemplatePlugin,
		 octoprint.plugin.ProgressPlugin,
       		octoprint.plugin.StartupPlugin):
	
	 # adds num as a template variable. May not be needed
	def get_template_configs(self):
		return dict(type="settings", custom_bindings=False)
	def get_settings_defaults(self):
		return dict(num="10")
	def on_after_startup(self):
		import os
		print "Here"
		os.system('sudo python ./templates/strip.py 10 20')
		self._logger.info("Got Here")
	def on_print_progress(storage, path, progress):
		os.system('sudo python strip.py '+str(num)+' '+str(progress))
	##~~ AssetPlugin mixin
	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			#js=["js/piled.js"],
			#css=["css/piled.css"],
			#less=["less/piled.less"]
		)
				
	##~~ Softwareupdate hook
	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			piled=dict(
				displayName="Piled Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="Quad14",
				repo="OctoPrint-Piled",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/Quad14/OctoPrint-Piled/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Piled Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = PiledPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

